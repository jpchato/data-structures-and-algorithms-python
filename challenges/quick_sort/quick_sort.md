# Quick Sort
* [Reference](https://www.goodreads.com/book/show/34695800-a-common-sense-guide-to-data-structures-and-algorithms)
* [Reference](https://www.geeksforgeeks.org/quick-sort/)
* [Visual](/assets/quick_sort.jpg)

* Quicksort is a divide and conquer algorithm.
* Picks an element as the pivot point and partitions the given array around the pivot point.
* Many different ways to implement quicksort that pick pivot points in different ways:
    1. Pick first element as pivot
    2. Pick last element as pivot
    3. Pick random element as pivot
    4. Pick median as pivot
* The key process in quicksort is partition()
* The target of partition is, given an array and an element x of array as pivot, put x at its correct position in sorted array and put all elements smaller than x before x, and put all elements greater than x after x.
* In my own words: First, we select the right most element as the pivot point. The remaining values in the array are compared to the pivot point. Those points that have a lower value than the pivot point's value are placed to the pivot point's left. Those points that have a larger value than the pivot point's value are placed to the pivot point's right.