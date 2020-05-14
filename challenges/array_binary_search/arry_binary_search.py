def binary_search(x, y):
  if y not in x:
    return (-1)
  if y in x:
    index_finder = x.find(y)
    return index_finder
    print (index_finder)


binary_search([1,2,3], 1)