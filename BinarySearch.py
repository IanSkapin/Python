

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


class BinarySearch(list):
    """ bisekcija """
    def __init__(self, *kargs, **kwargs):
        super().__init__(*kargs, **kwargs)
        self.sort()

    def has(self, integer, start=None, stop=None):
        """

        Args:
            integer:
            start:
            stop:

        Returns:

        """
        low = start or 0
        high = stop if stop and stop < len(self) - 1 else len(self) - 1
        return self.__search__(integer, low, high)

    def __search__(self, integer, low, high):
        if high < low:
            return False
        mid = round((high + low) / 2)
        # print(f'{low}:{mid}:{high}')
        if self[mid] < integer:
            return self.__search__(integer, low=mid + 1, high=high)
        elif self[mid] > integer:
            return self.__search__(integer, low=low, high=mid - 1)
        else:
            return mid


