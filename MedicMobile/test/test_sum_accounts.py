import pytest
import mock
from .. import sum_accounts

input_str = """Alex,Beatrice,101.32
Beatrice,Alex,1.20
Carl,Alex,45
Carl,Beatrice,12.50
Alex,Beatrice,19.22
Beatrice,Carl,67.90
Carl,Beatrice,12.80
Carl,Alex,15.88
Beatrice,Carl,71.42
Beatrice,Alex,4.54
Beatrice,Carl,28.76
"""
input_lines = input_str.splitlines()


def test_read_line_file():
    """ Test the read line generator"""
    with mock.patch('builtins.open', mock.mock_open(read_data=input_str)) as mock_open:
        idx = 0
        for idx, out in enumerate(sum_accounts.read_line('input.csv')):
            assert out == input_lines[idx].split(',')
        mock_open.assert_called_with('input.csv', newline='')
        assert idx == len(input_lines) - 1, 'there was nothing to iterate over, generator is broken'


def test_read_line_stdin():
    with mock.patch.object(sum_accounts.sys, 'stdin', input_lines), \
            mock.patch.object(sum_accounts.csv, 'reader', lambda x: x):
        idx = 0
        for idx, out in enumerate(sum_accounts.read_line(None)):
            assert out == input_lines[idx]
        assert idx == len(input_lines) - 1, 'there was nothing to iterate over, generator is broken'



@pytest.mark.parametrize('input, out', [
    ({('A', 'B'): 15.4, ('C', 'D'): -20}, {('A', 'B'): 15.4, ('D', 'C'): 20}),
    ({('A', 'B'): 15.4, ('C', 'D'): 20}, {('A', 'B'): 15.4, ('C', 'D'): 20}),
    ({('A', 'B'): -15.4, ('C', 'D'): -20}, {('B', 'A'): 15.4, ('D', 'C'): 20}),
])
def test_reverse_negatives(input, out):
    """ Test the negative accounts are correctly moved to positives
    """
    assert out == sum_accounts.reverse_negatives(input)


@pytest.mark.parametrize('in_d', [
    {('A', 'B'): 5, ('3', '#$'): -6},
])
def test_write_csv_file(in_d):
    """ Test the CSV writer"""
    csv_w = mock.MagicMock()
    csv_w.writerow = mock.MagicMock()
    with mock.patch('builtins.open', mock.mock_open()) as mock_open, \
            mock.patch.object(sum_accounts.csv, 'writer', return_value=csv_w):
        sum_accounts.write_csv(in_d, 'file_name', 2)
        csv_w.writerow.assert_has_calls([mock.call([k[0], k[1], v]) for k, v in in_d.items()])


@pytest.mark.parametrize('in_d', [
    {('A', 'B'): 5, ('3', '#$'): -6},
])
def test_write_csv_stdout(in_d):
    """ Test the CSV writer"""
    csv_w = mock.MagicMock()
    csv_w.writerow = mock.MagicMock()
    with mock.patch.object(sum_accounts.sys, 'stdout') as mock_stdout, \
            mock.patch.object(sum_accounts.csv, 'writer', return_value=csv_w) as mock_writer:
        sum_accounts.write_csv(in_d, None, 2)
        csv_w.writerow.assert_has_calls([mock.call([k[0], k[1], v]) for k, v in in_d.items()])
        mock_writer.assert_called_once_with(mock_stdout)


@pytest.mark.parametrize('lines, output_dict, resolve', [
    (input_lines, {
        ('Alex', 'Beatrice'): 120.54,
        ('Beatrice', 'Alex'): 5.74,
        ('Beatrice', 'Carl'): 168.08,
        ('Carl', 'Alex'): 60.88,
        ('Carl', 'Beatrice'): 25.30}, False),
    (input_lines, {
        ('Alex', 'Beatrice'): 120.54-5.74,
        ('Carl', 'Beatrice'): -168.08+25.30,
        ('Carl', 'Alex'): 60.88}, True),
])
def test_sum_accounts(lines, output_dict, resolve):
    """ Test the summation of the accounts
    """
    with mock.patch.object(sum_accounts, 'read_line', return_value=(r.split(',') for r in lines)), \
            mock.patch.object(sum_accounts, 'reverse_negatives', lambda x: x), \
            mock.patch.object(sum_accounts, 'write_csv') as mock_w_csv:
        assert 0 == sum_accounts.sum_accounts('in_file', 'out_file', resolve)
        assert mock_w_csv.call_args[0][1] == 'out_file'
        for k, v in mock_w_csv.call_args[0][0].items():
            assert round(output_dict[k], 2) == round(v, ndigits=2)


@pytest.mark.parametrize('lines, error_value', [
    (['Beatrice,Alex,10', 'Alex,10,Beatrice'], 'Beatrice'),
    (['Beatrice,Alex,10', 'Alex,Beatrice,5+j3'], '5+j3'),
    (['Beatrice,Alex,10', 'Alex,Beatrice,0x10'], '0x10'),
    (['Beatrice,Alex,10', 'Alex,Beatrice,0b10'], '0b10'),
])
def test_sum_accounts_value_error(lines, error_value):
    """ Test stderr triggers as expected for unrecognizable value"""
    with mock.patch.object(sum_accounts, 'read_line', return_value=(r.split(',') for r in lines)), \
            mock.patch('sys.stderr') as mock_err:
        assert 1 == sum_accounts.sum_accounts('in_file', 'out_file')
        mock_err.write.assert_called_once_with(f'Error: Unable to convert to Float the received input value: "{error_value}"')


@pytest.mark.parametrize('lines, error_value', [
    (['Beatrice,Alex,10', 'Alex,Beatrice'], '[\'Alex\', \'Beatrice\']'),
    (['Beatrice,Alex,10', 'Alex,Beatrice,10,Matt'], '[\'Alex\', \'Beatrice\', \'10\', \'Matt\']'),
    (['Beatrice,Alex,10', 'Alex,Beatrice,Carl,Matt'], '[\'Alex\', \'Beatrice\', \'Carl\', \'Matt\']'),
])
def test_sum_accounts_index_error(lines, error_value):
    with mock.patch.object(sum_accounts, 'read_line', return_value=(r.split(',') for r in lines)), \
            mock.patch('sys.stderr') as mock_err:
        assert 1 == sum_accounts.sum_accounts('in_file', 'out_file')
        mock_err.write.assert_called_once_with(f'Error: Unrecognized input format. Expected format: "Name1,Name2,Float",'
                                               f' received: "{error_value}"')
