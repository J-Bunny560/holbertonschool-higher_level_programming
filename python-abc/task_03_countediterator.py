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

# Testing
if __name__ == "__main__":
    counted_iter = CountedIterator([1, 2, 3, 4, 5])

    for _ in range(3):
        print(next(counted_iter))

    print("Number of items fetched:", counted_iter.get_count())
