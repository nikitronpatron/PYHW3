# Задайте число. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов.

num = int(input())
list = []

def Fibonacci(n):
    if n in [-1, 1, 2]:
        return 1
    elif n == 0:
        return 0
    elif n == -2:
        return -1
    elif n < -2:
        fibN = Fibonacci(n-1) + Fibonacci(n-2)
        return fibN*(-1)**(n+1)
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

for i in range (-num, num + 1):
    list.append(Fibonacci(i))
print(list)