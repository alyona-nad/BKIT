from random import randint


gen_random = lambda num_count, begin, end: (randint(begin, end) for i in range(num_count))


def gen_random_(num_count: int, begin: int, end: int):
    for _ in range(num_count):
        yield randint(begin, end)


if __name__ == '__main__':
    g = gen_random_(5, 1, 3)
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
