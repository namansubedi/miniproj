from time import perf_counter_ns
from rich import print

def binary_search(arr, low, high, x):
	
	if high >= low:
		mid = (high + low) // 2
		if arr[mid] == x:
			return mid

		elif arr[mid] > x:
			return binary_search(arr, low, mid - 1, x)

		else:
			return binary_search(arr, mid + 1, high, x)

	else:
		
		return -1

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


# Function call

t1_start = perf_counter_ns()
result = binary_search(arr, 0, len(arr)-1, x)
t1_stop = perf_counter_ns()




if result != -1:   
   print("Element is present at index", str(result+1))  
   
   print("______________________")
else:   
   print("Element is not present in array")  
   
t = t1_stop-t1_start
print("The runtime performance: " + str(t) + " ns.")
