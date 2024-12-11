# MERGE


# Реализуйте слияние двух отсортированных (по неубыванию) массивов.
#
# Необходимо реализовать слияние за O(N + M)
#
# Формат ввода
# Вводится число N. Количество элементов первого массива
#
# Далее следуют N строчек, на которых следуют отсортированные числа.
#
# На следующей строке вводится число M - количество элементов второго массива.
#
# Далее следуют M строчек, на которых следуют отсортированные числа второго массива.
#
# Формат вывода
# Выводится результат слияния двух массивов (длины N + M). Каждое число на новой строчке.


N = int(input())
lst1 = []
for i in range(N):
    a = int(input())
    lst1.append(a)

M = int(input())
lst2 = []
for i in range(M):
    b = int(input())
    lst2.append(b)


def Merge(arr1: list, arr2: list):
    arr = arr1 + arr2
    l = 0
    r = 0
    while l < len(arr1) and r < len(arr2):
        if arr1[l] >= arr2[r]:
            arr[l + r] = arr1[l]
            l += 1
        else:
            arr[l + r] = arr2[r]
            r += 1
    while l < len(arr1):
        arr[l + r] = arr1[l]
        l += 1
    while r < len(arr2):
        arr[l + r] = arr2[r]
        r += 1
    return arr


#

arr_final = Merge(lst1, lst2)

for elem in arr_final:
    print(elem)


# MERGE SORT
# Необходимо реализовать merge sort по невозрастанию
#
# Формат ввода
# В первой строке вводится число N - количество чисел, которые надо будет отсортировать. На следующих N строчках следуют числа.
#
# Формат вывода
# Вывести N отсортированных чисел, каждое с новой строки.

N = int(input())
lst = []
for i in range(N):
    a = int(input())
    lst.append(a)


def MergeSort(arr: list):
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2
    arr1 = MergeSort(arr[:mid])
    arr2 = MergeSort(arr[mid:])
    arr = Merge(arr1, arr2)
    return arr


arr_final = MergeSort(lst)

for elem in arr_final:
    print(elem)
