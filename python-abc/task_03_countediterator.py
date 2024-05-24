#!/usr/bin/python3
class CountedIterator:
    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.counter = 0

    def get_count(self):
        return self.counter

    def __next__(self):
        self.counter += 1
        try:
            return next(self.iterator)
        except StopIteration:
            raise

def test_counted_iterator():
    counted_iter = CountedIterator([1, 2, 3, 4, 5])

    for i in range(3):
        next(counted_iter)
        assert counted_iter.get_count() == 3, "Count should match the number of items"

    iterator = iter(counted_iter)

    while True:
        try:
            next(iterator)  # This should raise StopIteration

        except StopIteration:

            break

        assert counted_iter.get_count() == 5, "Count should match the number of items"


#  Testing
if __name__ == "__main__":
    test_counted_iterator()
