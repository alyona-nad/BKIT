data = [4, -30, 100, -100, 123, 1, 0, -1, -4]

if __name__ == '__main__':
    result = [i * j for i, j in sorted([(abs(i), i//abs(i)) if i != 0 else (0, 0) for i in data], reverse=True)]
    print(result)

    result_with_lambda = sorted(data, key=lambda x: -abs(x))
    print(result_with_lambda)
