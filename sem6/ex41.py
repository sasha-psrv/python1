# Задача №41. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.

import random


def create_items():
    len_items = input('введите длину массива: ')
    items = [random.randint(0, 20) for _ in range(int(len_items))]
    return items


def count_element(items_2):
    count = 0
    for i in range(1, len(items_2)-1):
        if items_2[i - 1] < items_2[i] > items_2[i+1]:
            count += 1
    return count

print(new_list:= create_items())
print(count_element(new_list))        
