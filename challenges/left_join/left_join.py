# reference: https://stackoverflow.com/questions/17949517/join-two-python-dictionaries-based-on-same-value-but-different-key-name-like-sq
# reference: https://realpython.com/python-zip-function/

def left_join(hashmap_a, hashmap_b):

  output = []

  for word in hashmap_a:
      # Python String class has __contains__() function which we can use to check if it contains another string or not.
      # __contains__() is an instance method and returns boolean value True or False depending on whether the string object contains the specified string object or not.
    if hashmap_b.__contains__(word):
       antonym = hashmap_b.get(word)
       synonym = hashmap_a[word]
       output.append([word, synonym, antonym])
  
  print(output)
  return output


if __name__ == "__main__":
    list_one = ['fond', 'wrath', 'diligent', 'outfit', 'guide']
    list_two = ['enamored', 'anger', 'employed', 'garb', 'usher']
    list_three = ['fond', 'wrath', 'diligent', 'guide', 'flow']
    list_four = ['averse', 'delight', 'idle', 'follow','jam']

    # The function takes in iterables as arguments and returns an iterator. This iterator generates a series of tuples containing elements from each iterable. zip() can accept any type of iterable, such as files, lists, tuples, dictionaries, sets, and so on.
    hashmap_a = dict(zip(list_one, list_two))

    hashmap_b = dict(zip(list_three, list_four))

    left_join(hashmap_a, hashmap_b)