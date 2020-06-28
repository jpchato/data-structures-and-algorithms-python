# reference: (https://coderbook.com/@marcus/how-to-create-a-hash-table-from-scratch-in-python/)
# reference: (https://www.youtube.com/watch?v=9HFbhPscPU0)
# reference: (https://www.youtube.com/watch?v=0M_kIqhwbFo)
# reference: (http://blog.linebylinecode.com/2017/11/24/how-to-implement-a-hash-table-in-python)

class Hashtable:
    def __init__(self):
        # determines the size of internal array
        self.capacity = 97
        # number of elements have been inserted
        self.size = 0
        # the internal array which stores each inserted value in a bucket based on the provided key
        self.buckets = [None] * self.capacity

    def hash(self, key):
        """
        takes in an arbitary key and returns an index in the collection
        """
        # demo states that this hash function is arbitrary but provides an acceptable degree of uniformity. It is different from the hash function shown in lecture.
        hash_sum = 0
        # for each character in the key
        # enumerate allows us to loop over something and have an automatic counter
        for idx, c in enumerate(key):
            # add index and length of key and exponented by current character code
            hash_sum += (idx + len(key)) ** ord(c)
            # Perform modulus to keep hash_sum in range [0, self.capacity, -1]
            hash_sum = hash_sum % self.capacity
        return hash_sum

    def add(self, key, value):
        """
        takes in both the key and value. this method should hash the key, and add the key and value pair to the table, handling collisions as needed
        """
        #1 increment size
        self.size += 1
        #2 compute index of key
        index = self.hash(key)
        #3 go to the node corresponding to the hash
        node = self.buckets[index]
        # if bucket is empty, do this
        if node is None:
            # create node, add it, return
            self.buckets[index] = Node(key, value)
            return
        #4 collision, iterate to the end of linked list at provided index
        prev = node
        while node is not None:
            prev = node
            node = node.next
        # add a new node at the end of the list with provided key/value
        prev.next = Node(key, value)

    def get(self, key):
        """
        takes in the key and returns the value from the table
        """
        #1 compute hash
        index = self.hash(key)
        #2 go to first node in list at bucket
        node = self.buckets[index]
        #3 traverse the linked list at this node
        while node is not None and node.key != key:
            node = node.next
        #4 now, node is the requested key/value pair or None
        if node is None:
            # not found
            return None
        else:
            # found - return value
            return node.value 
    
    def contains(self, key):
        """
        takes in the key and returns a boolean, indicating if the key exists in the table already
        """
        if key in self.buckets:
            print('key is present')
            True
        else:
            print('key is not present')
            False

class Node:
    # nodes are used for collision resolution
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = next

if __name__ == "__main__":
    ht = Hashtable()
    ht.add('testing', 72)
    ht.add('test2', 34)
    ht.contains('testing')

    