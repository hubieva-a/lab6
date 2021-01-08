a = []
n = int(input("Number of elements: "))
for i in range(1, n):
    elemt = int(input("Please enter the numbers"))
    a.append(elemt)

a_min = a[0]
i_min = 0
for i, item in enumerate(a):
    i = abs(i)
    if i < a_min:
        i_min, a_min = i, item
print("Element with min absolute: " + str(a_min))
print("Index of the element: " + str(i_min))

a_otr = a[0]
i_otr = 0
for i, item in enumerate(a):
    if item < 0:
        i_otr, a_otr = i, item
        break
new_a = a[i_otr:n:1]
sum_new_a = sum(new_a)
print("The sum of the elements after the first negative number will be " + str(sum_new_a))

aa = int(input("a = "))
bb = int(input("b = "))
for i, item in enumerate(a):
    if item > aa and item < bb:
        a.pop(i)
count = 0
for item in a:
    count +=1
diff = n - count
for i in range(1, diff):
    a.append(0)
print("The final array will be: " + str(a))
