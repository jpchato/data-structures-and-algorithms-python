def mergeLists(self, other_list):
    list1_curr = self.head
    list2_curr = other_list.head

    # This line of code checks to ensure that there are available positions in curr
    while list1_curr != None and list2_curr != None

        # Save next pointers
        # Creating new variables which save next pointers
        list1_next = list1_curr.next
        list2_next = list2_curr.next

        # Makes list2_curr as next of list1_curr
        list2_curr.next = list1_next # changes the next pointer of list2_curr
        list1_curr.next = list2_curr # changes the next pointer of list1_curr

        # update current pointers for current iteration
        # In my own words, I think these lines below are resetting the values to their original values so we can loop again in the while
        list1_curr = list1_next
        list2_curr = list2_next
    other_list.head = list2_curr


