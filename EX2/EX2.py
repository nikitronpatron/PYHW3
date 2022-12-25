# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(0, len(list) // 2):
    composition = list[i] * list[len(list) - 1 - i]
    print(composition)

if len(list) % 2 != 0:
    print(list[len(list) // 2])