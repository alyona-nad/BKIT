from gen_random import gen_random

class Unique(object):
    def __init__(self, items, **kwargs):
        self.used_elements = set()
        self.items = list(items)
        self.index = 0
        try:
            self.case_ignore = kwargs['case_ignore']
        except KeyError:
            self.case_ignore = False

    def __next__(self):
        while True:
            if len(self.items) > self.index:
                current = self.items[self.index]
                self.index += 1

                current_ = current.lower() if self.case_ignore else current

                if current_ not in self.used_elements:
                    self.used_elements.add(current_)
                    return current
            else:
                raise StopIteration

    def __iter__(self):
        return self

if __name__ == '__main__':
    data = ['a', 'A', 'B', 'a', 'b']
    print(*Unique(data, case_ignore=True))

    data = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    print(*Unique(data))

    data = gen_random(10, 1, 3)
    print(*Unique(data))
