# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным 
# значением дробной части элементов.

from decimal import Decimal as dec

list = [12.54, 54.32, 76.01, 23.22, 72.02]
doubleList = []
for i in list:
    decimal = round(i - i // 1, 5)
    doubleList.append(decimal)

difference = round(dec(max(doubleList)) - dec(min(doubleList)), 2)

doubleList.sort()
print(difference)
