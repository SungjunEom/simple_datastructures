def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

def fibonacci_tabulation(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    table = [0, 1]
    for i in range(n-1):
        table.append(table[-1]+table[-2])
    return table[-1]


if __name__ == '__main__':
    print(fibonacci(14))
    print(fibonacci_tabulation(14))