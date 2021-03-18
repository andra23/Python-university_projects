from ro.ubb.movierental.errors.errors import RepositoryError

class Repository:
    def __init__(self):
        self._elements = []
        self._counter = 0

    def __len__(self):
        return len(self._elements)

    def __iter__(self):
        return iter(self._elements)

    def __next__(self):
        try:
            new_list = self._elements[self._counter]
        except IndexError:
            raise StopIteration()
        self._counter += 1
        return new_list

    def add(self, element):
        """
        This function will insert an element into my list.
        """
        if element in self._elements:
            raise RepositoryError("This element already exists.")
        self._elements.append(element)

    def update (self, element):
        """
        This function will update an element with a given id.
        """
        if element not in self._elements:
            raise RepositoryError("This element doesn't exist, thus it can't be updated.")
        else:
            for index in range(len(self._elements)):
                if self._elements[index] == element:
                    self._elements[index] = element
                    return

    def remove (self, element):
        """
        Will remove a given element from my list.
        """
        if element not in self._elements:
            raise RepositoryError("The element you wanted to remove doesn't exist.")
        else:
            for index in range(len(self._elements)):
                if self._elements[index] == element:
                    del self._elements[index]
                    return

    def get_all(self):
        """
        Will return a list with all my elements.
        """
        return self._elements[:]