goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'color': 'black'}
]

def field(lst, *args):
    assert len(args) > 0

    for subject in lst:
        res = dict()
        for key in args:
            if key in subject:
                res[key] = subject[key]
        yield res if len(args) > 1 else list(res.values())[0]


def field_(lst, *args):
    assert len(args) > 0
    if len(args) > 1:
        for subject in lst:
            res = dict()
            for key in args:
                if key in subject:
                    res[key] = subject[key]
            yield res
    else:
        for subject in lst:
            yield subject[args[0]]

if __name__ == '__main__':
    g_1 = field(goods, 'title')
    print(next(g_1))
    print(next(g_1))

    g_2 = field_(goods, 'title', 'price')
    print(next(g_2))
    print(next(g_2))
