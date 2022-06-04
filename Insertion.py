list = [1, 2, 34, 0, 89]
for i in list:
    j = list.index(i)
    print(j)
    while j > 0:
        print(j)
        if list[j-1] > list[j]:
            list[j-1], list[j] = list[j], list[j-1]
            j = j-1
        else:
            break
print(list)
