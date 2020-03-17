"""
Written in python 3.8.1

For help execute:
python sum_accounts.py -h

Example of usage:
python sum_accounts.py -csv test\billing.csv

To run test, pytest and mock libraries have been used:
python -m pytest ./

"""
# The Scenario
#
# The client periodically generates a large CSV file containing a list of monetary debts, which they manually summarize and turn into a second CSV.
#
# The input CSV should look like this:
#
# Alex,Beatrice,101.32
# Beatrice,Alex,1.20
# Carl,Alex,45
# Carl,Beatrice,12.50
# Alex,Beatrice,19.22
# Beatrice,Carl,67.90
# Carl,Beatrice,12.80
# Carl,Alex,15.88
# Beatrice,Carl,71.42
# Beatrice,Alex,4.54
# Beatrice,Carl,28.76
#
# The first line states that Alex owes Beatrice $101.32.
#
# Currently, an intern is manually summarizing this data. If they used the above example, their result would look like this:
#
# Alex,Beatrice,120.54
# Beatrice,Alex,5.74
# Beatrice,Carl,168.08
# Carl,Alex,60.88
# Carl,Beatrice,25.30
#
# The client would like to automate this process, especially since these CSVs can get quite large!
#
# Your job is to create a unix-friendly command line application that performs this summarizing efficiently and correctly.


import csv
import sys
import argparse
from collections import defaultdict


def parse_arguments():
    parser = argparse.ArgumentParser(add_help="This script will traverse a given CSV file of format:\nA,B,C\n "
                                              "where A owes the amount C to B.")
    parser.add_argument('-csv', '--csv_file', required=True,
                        help='Path to the CSV file to process.')
    parser.add_argument('-o', '--output', default='output.csv',
                        help='Output file, by default ./output.csv is used.')
    parser.add_argument('-R', '--resolve_pairs', action='store_true', default=False,
                        help='Resolve pairs of accounts (A owes B and B owes A) to only show the one.')
    parser.add_argument('-rd', '--round_digits', default=2, type=int,
                        help='Round the output sum on N decimal digits, by default 2.')
    return parser.parse_args()


def read_line(file_name: str):
    """Generator reading the given file line per line.

    Args:
        file_name(str): path to the text file to read

    Returns: yields one line per call till EOF

    """
    with open(file_name, newline='') as FH:
        for row in csv.reader(FH):
            yield row


def reverse_negatives(accounts: dict):
    """ If the value is negative exchange the values in the key tuple and save the positive value

    Args:
        accounts(dict): dictionary of format {('A', 'B'): <float>}

    Returns(dict): same dictionary with the keys and values of the negative float numbers updated.
     """
    negatives = [k for k, v in accounts.items() if v < 0]

    for k in negatives:
        benefactor, payee = k
        accounts[(payee, benefactor)] = -accounts.pop(k)
    return accounts


def write_csv(accounts: dict, outfile: str, round_digits: int):
    """ Write the account dictionary in in CSV format in to the outfile.

    Args:
        accounts(dict): dictionary of format {('A', 'B'): <float>}
        outfile(str): file path
        round_digits(int): set the rounding to improve readability of the CSV file

    """
    with open(outfile, 'w', newline='') as FH:
        csv_writer = csv.writer(FH)
        for key, value in accounts.items():
            payee, benefactor = key
            csv_writer.writerow([payee, benefactor, round(value, ndigits=round_digits)])


def sum_accounts(csv_file: str, output: str, resolve_pairs=False, round_digits=2):
    """ Reads the csv_file line by line and keeps track of pairs of transaction. Adding up repeated transactions. If
    resolve_pairs is set it will also recognise reverse transactions (A->B and B->A).

    Args:
        csv_file(str): input CSV file path
        output(str): output CSV file to generate
        resolve_pairs(boolean): if True will recognise reverse transactions (A->B 1, B->A, 3 => B->A 2)
        round_digits(int): before printing the accounts the values are rounded to round_digits decimals

    Returns(int): 0

    """
    accounts = defaultdict(int)
    for payee, benefactor, amount in read_line(csv_file):
        if resolve_pairs and (benefactor, payee) in accounts.keys():
            accounts[(benefactor, payee)] -= float(amount)
        else:
            accounts[(payee, benefactor)] += float(amount)

    accounts = reverse_negatives(accounts) if resolve_pairs else accounts
    write_csv(accounts, output, round_digits)
    return 0


if __name__ == '__main__':
    args = parse_arguments()
    sys.exit(sum_accounts(args.csv_file, args.output, args.resolve_pairs, args.round_digits))
