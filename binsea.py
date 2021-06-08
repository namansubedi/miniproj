def find(L, target):
    start = 0
    end = len(L) - 1

    while start <= end:
        middle = (start + end)// 2
        midpoint = L[middle]
        if midpoint > target:
            end = middle - 1
        elif midpoint < target:
            start = middle + 1
        else:
            return middle

arr = []

file = open('list.txt', 'r')
for each in file:
    each = each.lower()
    arr.append(each)

#take search term
print("What value do you wanna find in the array?")
x = str(input("Enter your value: "))
x = x.lower()
x = x + "\n"
print(x)

result = find(arr, x)

if (result is None):
	print("Element not present in the list. Rerun program.")
else:
	print("Element found at line: " , result+1)