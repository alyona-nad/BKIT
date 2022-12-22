import json
from print_result import print_result
from cm_timer import cm_timer
from unique import Unique
from gen_random import gen_random


@print_result
def f1(arg):
    return sorted(Unique([row['job-name'] for row in arg], case_ignore=True), key=lambda row: row.lower())


@print_result
def f2(arg):
    return list(filter(lambda s: 'программист' in s.lower(), arg))


@print_result
def f3(arg):
    return (lambda job: list(map(lambda s: s + ' с опытом Python', job)))(arg)


@print_result
def f4(arg):
    job_with_sal = zip(arg, [f'зарплата {rand_sel} руб.' for rand_sel in gen_random(len(arg), 100000, 200000)])
    return list(map(lambda s: ', '.join(s), job_with_sal))


if __name__ == '__main__':
    with open('data_light.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    with cm_timer():
        f4(f3(f2(f1(data))))
