numbers = [1, 2, 4, 4, 7, 8, 90, 92]
search = int(input("Enter a element to search : "))

for i in range(len(numbers)):
    if numbers[i] == search:
        print(f"The search element {search} was found at index {i}.")
else:
    print("Unable to locate search element in the list...")
