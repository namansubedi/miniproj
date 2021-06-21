Iterative approach
binarySearch(arr, size)
		   loop until beg is not equal to end
    midIndex = (beg + end)/2
    if (item == arr[midIndex] )
        return midIndex
    else if (item > arr[midIndex] ) 
        beg = midIndex + 1
    else                       
        end = midIndex - 1
Recursive approach
binarySearch(arr, item, beg, end)
    if beg<=end
        midIndex = (beg + end) / 2 
        if item == arr[midIndex]
            return midIndex
        else if item < arr[midIndex]        
            return binarySearch(arr, item, midIndex + 1, end)
        else                              
            return binarySearch(arr, item, beg, midIndex - 1)
    
    return -1
