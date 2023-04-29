from random import *
# # a = [[1 for i in range(4)] for j in range(4)]
# # for i in range(4):
# #     for j in range(4):
# #         a[i][j] = randint(1,9)
# #         print(a[i][j], end=' ')
# # print()
# # print()
# # for i in range(4):
# #     for j in range(4):
# #         a[i][j] = randint(1,9)
# #         print(a[i][j], end=' ')
# #     print()
# # print()
# # SEN=-1
# # print('Principal Diagonal:', end=' ')
# # for i in range(4):
# #     for j in range(4):
# #         if a[i][i] != SEN:
# #             print(a[i][i], end=' ')
# #             a[i][i] = SEN
#
# # Selection sort in Python
#
#
def selectionSort(array, size):
    for step in range(size):
        min_idx = step
        for i in range(step + 1, size):
            if array[i] < array[min_idx]:
                min_idx = i
        (array[step], array[min_idx]) = (array[min_idx], array[step])
#
#
# data = [randint(0,9), randint(0,9), randint(0,9), randint(0,9), randint(0,9)]
# size = len(data)
# print(data)
# selectionSort(data, size)
# print('Sorted Array in Ascending Order:')
# print(data)

def task1():
    list1 = []
    for i in range(10):
        list1.append(randint(0, 9))
    print(f'list: {list1}')
    list2 = []
    for i in range(9,-1,-1):
        list2.append(list1[i])
    print(f'Reverse: {list2}')

def task2():
    list1 = []
    sum = 0
    for i in range(10):
        x = randint(0, 9)
        list1.append(x)
        sum += x
    print(f'Sum: {sum}')

def task3():
    x = [randint(1,10) for i in range(10)]
    y = [x[i] for i in range(len(x))]
    print(y)

def task4():
    list1 = []
    list2 = []
    list3 = []
    for i in range(5):
        list1.append(randint(0, 9))
        list2.append(randint(0, 9))
    selectionSort(list1,5)
    selectionSort(list2,5)
    for i in range(5):
        list3.append(list1[i])
        list3.append(list2[i])
    selectionSort(list3,10)
    print(list3)

def task5():
    list1 = []
    list_even = []
    list_odd = []
    for i in range(10):
        list1.append(randint(1, 9))
    for i in range(10):
        if list1[i] % 2 == 0:
            list_even.append(list1[i])
        elif list1[i] % 2 != 0:
            list_odd.append(list1[i])
    print(list1)
    print(list_even)
    print(list_odd)
    print()
    print()
    if len(list_even) > len(list_odd):
        for i in range(len(list_even)):
            list_even[i] += 1
    elif len(list_even) < len(list_odd):
        for i in range(len(list_odd)):
            list_odd[i] -= 1
    print(list1)
    print(list_even)
    print(list_odd)

def task6():
    list1 = []
    while len(list1) < 10:
        random_number = randint(1, 16)
        if random_number not in list1:
            list1.append(random_number)
    print(list1)

def task7():
    list1 = []
    for i in range(10):
        list1.append(randint(1, 9))

def task8():
    list1 = []
    list2 = []
    x = 1
    for i in range(20):
        x += randint(1,3)
        list1.append(x)
    print(list1)
    for i in range(1, list1[19]):
        if i not in list1:
            list2.append(i)
    print(list2)

def task9():
    list1 = [3,2,0,1,2,4,6,2,1,9,8,2,3,4,6,2,0,1,3,4]
    # for i in range(20):
    #     list1.append(randint(0, 9))
    print(list1)
    for i in range(2, len(list1)-2):
        x = (list1[i-2] + list1[i-1] + list1[i+1] + list1[i+2])//4
        list1[i] = x
    print(list1)

def task10():
    list1 = []
    for i in range(10):
        list1.append(randint(3, 7))
    print(list1)
    for i in range(len(list1)):
        n = list1[i]
        for j in range(n):
            print('*', end='')
        print()

def task11():
    list1 = []
    for i in range(10):
        list1.append(randint(0, 9))
    print(list1)
    for i in range(1, 11):
        for j in range(i):
            print(list1[j], end=' ')
        print()

def task12():
    list1 = []
    for i in range(10):
        list1.append(randint(0, 9))
    print(list1)
    for i in range(1, 11):
        sum = 0
        for j in range(i):
            x = list1[j]
            print(x, end=' ')
            sum += x
        print(f'= {sum}')


def task13():
    list1 = []
    for i in range(10):
        list1.append(randint(0, 9))
    print(list1)
    for i in range(8):
        for j in range(3):
            print(list1[i+j], end=' ')
        print()

def task14():
    list1 = [[randint(0, 9) for i in range(10)] for j in range(10)]
    for i in range(10):
        for j in range(10):
            print(list1[i][j], end='  ')
        print()

def task15():
    list1 = [[randint(0, 9) for i in range(10)] for j in range(10)]
    for i in range(10):
        for j in range(i):
            print(end='  ')
        print(list1[i][i], )

task3()
