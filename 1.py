a = []
n = int(input("Number of elements: "))
for i in range(1, n+1):
    elemt = int(input("Please enter a number: "))
    a.append(elemt)
arr1 = []
arr2 = []
arr3 = []
for i in a:
    if i % 5 == 0:
        arr1.append(i)
    elif i % 7 == 0:
        arr2.append(i)
    else:
        arr3.append(i)
print("Numbers multiple 5" + str(arr1))
print("Numbers multiple 7" + str(arr2))
print("Other numbers" + str(arr3))

