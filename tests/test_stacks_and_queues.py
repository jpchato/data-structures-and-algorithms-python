# # import pytest
# # from data_structures.linked_list.stacks_and_queues.stacks_and_queues import Stack, Queue

# # 1. Can successfully push onto a stack
# def test_push():
#     test_stack = Stack()
#     test_stack.push(1)
#     test_stack.push(2)
#     assert test_stack.head.element == 2

# # 2. Can successfully push multiple values onto a stack
# def test_multiple_nodes():
#     test_stack = Stack()
#     test_stack.push(1)
#     test_stack.push(2)
#     test_stack.push(3)
#     assert test_stack.size == 3

# # 3. Can successfully pop off the stack
# def test_pop():
#     test_stack = Stack()
#     test_stack.push(1)
#     test_stack.push(2)
#     test_stack.push(3)
#     poppin = test_stack.pop()
#     assert poppin == 3
#     assert test_stack.size == 2
#     assert test_stack.head.element == 2

# # 4. Can successfully empt a stack after multiple pops
# def test_multi_pop():
#     test_stack = Stack()
#     test_stack.push(1)
#     test_stack.push(2)
#     test_stack.push(3)
#     test_stack.pop()
#     test_stack.pop()
#     test_stack.pop()
#     assert test_stack.size == 0

# # 5. Can successfully peek the next item on the stack
# def test_peek():
#     test_stack = Stack()
#     test_stack.push(1)
#     test_stack.push(2)
#     test_stack.push(3)
#     assert test_stack.peek() == 3

# # 6. Can successfully instantiate an empty stack
# def test_empty_stack():
#     test_stack = Stack()
#     # w3schools - The isinstance() function returns True if the specified objet is of the specified type, otherwise False
#     assert isinstance(test_stack, Stack)

# # 7. Calling pop or peek on empty stack raises exception
# # def test_Exception_empty():
# #     test_stack = Stack()
# #     assert test_stack == IsEmptyError



