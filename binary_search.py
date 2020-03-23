"""
# generic implementation
def search(array, integer, low, high, descending=False, debug=False):
    if high < low:
        if debug:
            print('dead end')
        return False
    mid = round((low + high) / 2)
    if debug:
        print(f'{low}:{mid}:{high} ', 'descending' if descending else 'ascending')
    if array[mid] < integer:
        if descending:
            return search(array, integer, descending=descending, low=low,     high=mid - 1)
        else:
            return search(array, integer, descending=descending, low=mid + 1, high=high)
    elif integer < array[mid]:
        if descending:
            return search(array, integer, descending=descending, low=mid + 1, high=high)
        else:
            return search(array, integer, descending=descending, low=low,     high=mid - 1)
    else:
        return mid
"""


# wrapper implementation
def search(array, integer, low, high, descending=False, debug=False):
    if descending:
        return search_descending(array, integer, low, high, debug)
    else:
        return search_ascending(array, integer, low, high, debug)


def search_descending(array, integer, low, high, debug=False):
    """Recursive binary search for 'integer' in the descending 'array' (array[i] >= array[i+1])."""
    if high < low:
        if debug:
            print('dead end')
        return False
    mid = round((low + high) / 2)
    if debug:
        print(f'{low}:{mid}:{high} ', 'descending')
    if array[mid] < integer:
        return search_descending(array, integer, low=low,     high=mid - 1)
    elif integer < array[mid]:
        return search_descending(array, integer, low=mid + 1, high=high)
    else:
        return mid


def search_ascending(array, integer, low, high, debug=False):
    """Recursive binary search for 'integer' in the ascending 'array' (array[i] <= array[i+1])."""
    if high < low:
        if debug:
            print('dead end')
        return False
    mid = round((low + high) / 2)
    if debug:
        print(f'{low}:{mid}:{high} ', 'ascending')
    if array[mid] < integer:
        return search_ascending(array, integer, low=mid + 1, high=high)
    elif integer < array[mid]:
        return search_ascending(array, integer, low=low,     high=mid - 1)
    else:
        return mid


class BinarySearch(list):
    """
    Returns an ordered list object equipped with the method 'has'. Method 'has' requires the list to be sorted. Changing
    the list elements will require you to make sure the elements are sorted before calling 'has'.
    """
    def __init__(self, *kargs, **kwargs):
        super().__init__(*kargs, **kwargs)
        self.sort()

    def has(self, integer, start=None, stop=None):
        """ Returns the found integer position in the array or False if it is not part of the array
        """
        low = start or 0
        high = stop if stop and stop < len(self) - 1 else len(self) - 1
        return search_ascending(self, integer, low, high)

