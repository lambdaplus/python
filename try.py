def try_except(N):
    try:
        print('This is result')
        s = 10.0 / n
        print('result: %s') %s
    except ZeroDivisionError as e:
        print('except: %s') %e

if __name__ == '__main__':
    n = input('n = ')
    try_except(n)
