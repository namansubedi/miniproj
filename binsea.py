from time import perf_counter_ns

#performance compare function
def perf(arr):
    target = ["a", "matter", "yourself"]
    for tar in target:
        t1_start = perf_counter_ns()
        result = find(arr, tar+"\n")
        t1_stop = perf_counter_ns()
        t = t1_stop-t1_start
        print("To find " + str(tar) + " on index " + str(result) + " : " + str(t) + " ns. Jumps = " + str(jump))

def find(L, target):
    start = 0
    end = len(L) - 1
    #this jump is used to know how many times the program goes through while loop
    global jump
    jump = 0

    while start <= end:
        jump += 1
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

#run this to check and compare performance comment this to run program normally
#perf(arr)

t1_start = perf_counter_ns()
result = find(arr, x)
t1_stop = perf_counter_ns()

if (result is None):
	print("Element not present in the list. Rerun program.")
else:
	print("Element found at line: " , result+1)

t = t1_stop-t1_start
print("The runtime performance: " + str(t) + " ns. Jumps = " + str(jump))