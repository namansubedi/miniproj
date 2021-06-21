from time import perf_counter_ns
from rich import print
import matplotlib.pyplot as plt

def make_plot(tick_label, height, title1):
    left = [1,2,3,4,5]
    plt.bar(left, height, tick_label = tick_label, width = 0.8, color = ['black'])
    plt.xlabel('Index')
    plt.ylabel('Time (in nanoseconds)')
    plt.title(title1)
    plt.show()

def search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

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
list = []
time = []
time1 = []

file = open('list.txt', 'r')

for each in file:
    each = each.lower()
    arr.append(each)

#take search term
x = ["a\n","economy\n","matter\n","see\n","yourself\n"]

for term in x:
    t1_start = perf_counter_ns()
    result = search(arr, term)
    t1_stop = perf_counter_ns()

    if (result < 0):
        print("Element not present in the list.")
    else:

        list.append(result+1)
        t = t1_stop-t1_start
        time.append(t)
        
        #from here for binary comparision

        t1_start = perf_counter_ns()
        result = find(arr, term)
        t1_stop = perf_counter_ns()
        if (result is None):
            print("Element not present in the list. Rerun program.")
        else:
            t = t1_stop-t1_start
            time1.append(t)

make_plot(list, time, "Linear Search")
make_plot(list, time1, "Binary Search")