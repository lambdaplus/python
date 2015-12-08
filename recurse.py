def factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        m = factorial(n-1)*n
        return m

if __name__ == '__main__':
    n = int(input('n = '))
    print(factorial(n))
