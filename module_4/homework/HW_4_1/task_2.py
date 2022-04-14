
def insertion_sort(list0):
    for i in range(1, len(list0)):
        temp = list0[i]
        j = i - 1
        while j >= 0 and temp < list0[j]:
            list0[j + 1] = list0[j]
            j = j - 1
        list0[j + 1] = temp

list1 = input('Input the list of numbers: ').split()
list1 = [int(x) for x in list1]

insertion_sort(list1)
print('Sorted list: ', end='')
print(list1)