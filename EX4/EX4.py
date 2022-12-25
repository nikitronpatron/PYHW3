# Напишите программу, которая будет преобразовывать 
# десятичное число в двоичное.

num = int(input())
binNum = ""

while num > 0:
    binEl = num % 2
    num = num // 2
    binNum = str(binEl) + binNum
print(binNum)