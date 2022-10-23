
import sys
import math


def get_coef(index, prompt):
    try:
        coef_str = sys.argv[index]
    except:
        print(prompt)
        coef_str = input()
    try:
        coef = float(coef_str)
        if index == 1 and coef == 0:
            raise ValueError('Not biquadratic equation')
    except:
        print('Неккоректная форма аргумента. Пожалуйста, введите аргумент в виде действительного числа')
        return get_coef('not console input', prompt)
    return coef


def get_roots(a, b, c):
    roots = []
    D = b * b - 4 * a * c
    if D == 0.0:
        root = -b / (2.0 * a)
        if root >= 0:
            roots.append(root)
    elif D > 0.0:
        sqD = math.sqrt(D)
        root1 = (-b + sqD) / (2.0 * a)
        root2 = (-b - sqD) / (2.0 * a)
        roots.append(root1)
        roots.append(root2)
    result = []
    for i in roots:
        if i > 0:
            result.append(math.sqrt(i))
            result.append(-1 * math.sqrt(i))
        if i == 0:
            result.append(i)
    return result


def main():
    a = get_coef(1, 'Введите коэффициент А:')
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')
    roots = get_roots(a, b, c)
    len_roots = len(roots)
    if len_roots == 0:
        print('Нет корней')
    elif len_roots == 1:
        print('Один корень: {}'.format(roots[0]))
    elif len_roots == 2:
        print('Два корня: {} и {}'.format(roots[0], roots[1]))
    elif len_roots == 3:
        print('Три корня: {} и {} и {}'.format(roots[0], roots[1], roots[2]))
    elif len_roots == 4:
        print('Четыре  корня: {} и {} и {} и {}'.format(roots[0], roots[1], roots[2], roots[3]))


if __name__ == "__main__":
    main()
