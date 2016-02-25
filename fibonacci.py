# coding: utf-8

def fib_one(n):
    a, b = 0, 1
    while b < n: # 返回小于n的fibonacci数列
        a, b = b, a+b
        print(a,'', end='')

# 下面的这个是一个生成器
def fib_two():
    a, b = 0, 1
    yield b
    while True:
        a, b = b, a+b
        yield b 

for i in fib_two():
    if i > 100: break
    print(i,'', end='')
print()

fib_one(100)
