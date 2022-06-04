list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
list.sort()
search = int(input("Enter the element to search : "))
start = 0
stop = len(list)-1 
while start <= stop:
    mid = (start+stop)//2
    print("mid : ", mid)
    if search == list[mid]:
        print("The element is found at index : ", mid)
        break
    elif search < list[mid]:
        stop = mid-1
    else:
        start = mid+1
else:
    print("The element is not found...")
