def insertion_sort(array):
    # Begins a loop at index 1 that runs through the entire array. The variable index stores the current index
    for index in range(1, len(array)):

        # Position stores the current index. The value at that index is stored in temp_value.
        position = index
        temp_value = array[index]

        # An inner while loop, that checks whether the value to the left of position is greater than temp_value. If so, array[position] = array[position - 1] is used to shift the left value to the right, and decrease position by one (position being the index). Then the value to the left of the new position is checked to see if it's greater than temp_value, and the process is repeated until a value is found that is less than temp_value.
        while position>0 and array[position - 1] > temp_value:
            array[position] = array[position - 1]
            position = position - 1

        # the temp_value is placed in the gap within the array
        array[position] = temp_value
    return array
if __name__ == "__main__":
    array_one = [5,9,22,3,1]
    print(array_one)
    insertion_sort(array_one)
    print(array_one)