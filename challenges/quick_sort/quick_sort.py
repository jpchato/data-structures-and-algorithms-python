# reference: https://www.geeksforgeeks.org/quick-sort/
# This function makes the last element in the array as the pivot point
# Places the pivot point at its correct position in the sorted array
# Places all smaller elements than pivot to pivot's left
# Places all larger elements than pivot to pivot's right

def partition(arr, low, high):
    # index value of smallest element
    i = (low - 1)
    # sets the value of pivot to the index value of rightmost element
    pivot = arr[high]
    
    # for each element(j) in the range from low to high
    for j in range(low, high):

        # if the current element is smaller than the pivot, execute code below
        if arr[j] < pivot:
            
            # incrementing the index of the smaller element
            i = i + 1
            # swapping the values because???
            arr[i], arr[j] = arr[j], arr[i]

    # swapping the values again
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    # returns pivot index point
    return (i + 1)

# Quicksort parameters
# arr[] is the array to be sorted
# low is the starting index(leftmost)
# high is the ending index(rightmost)

def quick_sort(arr, low, high):
    # if the ending index is larger than the beginning index, execute the code below
    if low < high:
        # p is the partitioning index, arr[p] is in now in correct place
        p = partition(arr, low, high) 
        # Separately sort elements before partition and after partition, sorting the two halves
        quick_sort(arr, low, p-1)
        quick_sort(arr, p+1, high)
    # return sorted array for testing
    return arr

if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    n = len(arr) 
    print('unsorted array is', arr)
    quick_sort(arr,0,n-1) 
    print ('sorted array is', arr) 

