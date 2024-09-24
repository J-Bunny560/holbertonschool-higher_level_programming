#!/usr/bin/python3

class CountedIterator:
    """
    An iterator that keeps a count of the number of items retrieved.

    Attributes:
        counter (int): The number of items that have been retrieved.
        iterator (iterator): The iterator of the iterable.
    """
    def __init__(self, iterable):
        """
        Initializes a new instance of CountedIterator.

        Args:
            iterable (iterable): The iterable to iterate over.
        """
        self.counter = 0
        self.iterator = iter(iterable)

    def get_count(self):
        """
        Returns the number of items that have been retrieved.
        """
        return self.counter

    def __next__(self):
        """
        Retrieves the next item from the iterator and increments the counter.

        Returns:
            The next item from the iterator.

        Raises:
            StopIteration: If there are no more items to retrieve.
        """
        next_item = next(self.iterator)
        self.counter += 1
        return next_item
