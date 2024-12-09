N = int(input())
lst = []
for i in range(N):
    a = int(input())
    lst.append(a)


# сортировка вставками  T(N) = O(N^2) // устойчива
# Необходимо реализовать сортировку вставками по неубыванию
#
# Формат ввода
# В первой строке вводится число N - количество чисел, которые надо будет отсортировать.
#
# На следующих N строчках следуют числа.

for i in range(N - 1):
        j = i + 1
        while j > 0 and lst[j] < lst[j - 1]:
            t = lst[j]
            lst[j] = lst[j - 1]
            lst[j - 1] = t
            j = j - 1

def InsertionSort(arr: list):
    n = len(arr)
    for i in range(n - 1):
        j = i + 1
        while j > 0 and arr[j] < arr[j - 1]:
            t = arr[j]
            arr[j] = arr[j - 1]
            arr[j - 1] = t
            j = j - 1


InsertionSort(lst)


# #сортировка выбором // T(N) = O(N^2) // неустойчива
#
# Необходимо реализовать сортировку выбором по неубыванию
#
# Формат ввода
# В первой строке вводится число N - количество чисел, которые надо будет отсортировать.
#
# На следующих N строчках следуют числа.


for k in range(N):
    for i in range(N):
        if lst[i] > lst[k]:
            t = lst[k]
            lst[k] = lst[i]
            lst[i] = t

def SelectionSort(arr: list):
    n = len(arr)
    for k in range(n):
        for i in range(n):
            if arr[i] > arr[k]:
                t = arr[k]
                arr[k] = arr[i]
                arr[i] = t


SelectionSort(lst)

#сортировка пузырьком // T(N) = O(N^2) // Устойчива
#
# Необходимо реализовать сортировку выбором по невозрастанию
#
# Формат ввода
# В первой строке вводится число N - количество чисел, которые надо будет отсортировать.
#
# На следующих N строчках следуют числа.


for i in range(N):
    for j in range(N - 1):
        if lst[j] < lst[j + 1]:
            t = lst[j]
            lst[j] = lst[j + 1]
            lst[j + 1] = t

def BubbleSort(arr: list):
    n = len(arr)
    for i in range(n):
        for j in range(n - 1):
            if arr[j] < arr[j + 1]:
                t = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = t


BubbleSort(lst)

for elem in lst:
    print(elem)
