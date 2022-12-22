from contextlib import contextmanager
from time import time, sleep


class CmTimer:
    def __init__(self):
        self.start_time = time()

    def __enter__(self):
        return 1

    def __exit__(self, exp_type, exp_value, traceback):
        if exp_type is not None:
            print(exp_type, exp_value, traceback)
        else:
            print(f'Время работы блока {time() - self.start_time:.4f} сек. (класс)')


@contextmanager
def cm_timer():
    start_time = time()
    yield 1
    print(f'Время работы блока {time() - start_time:.4f} сек. (функция)')

if __name__ == '__main__':
    with CmTimer():
        sleep(1.5)

    with cm_timer():
        sleep(1.5)
