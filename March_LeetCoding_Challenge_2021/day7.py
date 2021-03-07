"""
Question.
Design a HashMap without using any built-in hash table libraries.
To be specific, your design should include these functions:
- put(key, value) : Insert a (key, value) pair into the HashMap. If the value already exists in the HashMap, update the value.
- get(key): Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
- remove(key) : Remove the mapping for the value key if this map contains the mapping for the key.

Note:
- All keys and values will be in the range of [0, 1000000].
- The number of operations will be in the range of [1, 10000].
- Please do not use the built-in HashMap library.
"""
class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash = []

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        counter = len(self.hash)
        if counter > 0:
            for i in range(counter):
                counter -= 1
                if key == self.hash[i][0]:
                    self.hash[i][1] = value
                    return
        if counter == 0:
            self.hash.append([key, value])

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """ 
        counter = len(self.hash)
        if counter > 0:
            for i in range(counter):
                if key == self.hash[i][0]:
                    return self.hash[i][1]
                counter -= 1
        if counter == 0:
            return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        counter = len(self.hash)
        if counter > 0:
            for i in range(counter):
                counter -= 1
                if key == self.hash[i][0]:
                    self.hash.pop(i)
                    return
        if counter == 0:
            return

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)