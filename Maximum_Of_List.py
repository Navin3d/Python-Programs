def maximum(listarg, comparator):
    return_value = []
    for i in listarg:
        if i > comparator:
            return_value.append(i)

    return return_value

listin = [1, 2, 3, 4, 5, 6]
num = 2

print("The Max values are: ", maximum(listin, num))
