#!/usr/bin/python3

class CountedIterator:
    def __init__(self, iterable):
        self.iterable = iter(iterable)
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.count += 1
        return next(self.iterable)

    def get_count(self):
        return self.count

data = [1, 2, 3, 4]
counted_iter = CountedIterator(data)
