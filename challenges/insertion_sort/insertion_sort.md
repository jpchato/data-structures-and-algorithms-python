# Insertion Sort
* [A Common Sense Guide to Data Structures and Algorithms](https://www.google.com/books/edition/A_Common_Sense_Guide_to_Data_Structures/yA5QDwAAQBAJ?hl=en&gbpv=1&printsec=frontcover)
* [Visual](/assets/insertion_sort.jpg)
1. In the first passthrough, temporarily remove the value at index 1 and store it in a temporary variable. This leaves a gap at that index since it contains no value. In following passthroughs, remove the values at subsequent indexes.
2. Following this is the shifting phase, where each value to the left of the gap is compared to the value in the temporary variable. If the value to the left of the gap is greater than the temporary variable, the value is shifted to the right. As values are shifted to the right, the gap moves leftwards. When a value that is lower than the temporarily removed value is encountered, or the left end of the array is reached, the shifting phase is over.
3. The temporarily removed value is inserted into the current gap.
4. Repeat until fully sorted.