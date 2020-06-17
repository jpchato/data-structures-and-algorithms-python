# reference https://www.geeksforgeeks.org/merge-sort/
# reference https://www.pythoncentral.io/merge-sort-implementation-guide/

def merge_sort(arr):
    # If the length of the array is greater than 1, execute the code below
    if len(arr) > 1:
        # Finds the middle of the array using floor division(decimals removed)
        mid = len(arr)//2
        # Holds the values for the left half of the array
        l = arr[:mid]
        # Holds the values for the right half of the array
        r = arr[mid:]

        # recursively sorts the left half
        merge_sort(l) 
        # recursively sorts the right half
        merge_sort(r)

        # iteration values are all set to zero
        # same as writing 3 lines of code and setting each value to 0
        i = j = k = 0

        # While i and j are less than the length of their respective halves, execute the code below
        while i < len(l) and j < len(r):
            # if the value of the left half is less than the value of the right half, execute the code below
            if l[i] < r[j]:
                # The value in the array is set to the value at l[i]
                arr[k] = l[i]
                # iterate i once
                i += 1
            # If the above if statement is not true, that is the value at r[j] is not greater than the value at l[i], execute the code below
            else:
                # The value in the array is set to the value at r[j]
                arr[k] = r[j]
                # iterate j once
                j += 1
            # iterate k once, this helps us break out of our while loop
            k += 1

        # Rest of the code checks to see if any element was left
        # While the length of the left is greater than i, execute code below
        while i < len(l):
            # Sets the value of arr[k] to the value of l[i]
            arr[k] = l[i]
            # iterates i by 1
            i += 1
            # iterates k by 1
            k += 1

        # While the length of the right is greater than j, execute the code below
        while j < len(r):
            #  set the value of arr[k] to the value of r[j]
            arr[k] = r[j]
            # iterate j by 1
            j += 1
            # iterate k by 1
            k += 1
    # return the arr, important for testing
    return arr



if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print(merge_sort(arr))

    
