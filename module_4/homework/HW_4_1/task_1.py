
list2 = [12, 88, 229, 812, 77, 0, 12, 44, 19, 18]
list2.sort()
print(list2)

mid = len(list2) // 2
lower = 0
higher = len(list2) - 1
number = int(input('Input number for find his ID in that list: '))

while list2[mid] != number and lower <= higher:
    if number > list2[mid]:
        lower += mid
    else:
        higher -= mid
    mid = (lower + higher) // 2

if lower > higher:
    print('Number is not in list')
else:
    print('ID =', mid)