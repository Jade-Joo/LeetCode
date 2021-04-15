from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        else:
            # refresh the entry with given key
            self.cache.move_to_end(key)
            
            return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            
            if len(self.cache) >= self.capacity :
                # pop the least used entry
                self.cache.popitem(last = False)

        else:
			# refresh the entry with given key
            self.cache.move_to_end(key)
        
        self.cache[key]  = value

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

'''
popitem(last=True)
The popitem() method for ordered dictionaries returns and removes a (key, value) pair. The pairs are returned in LIFO order if last is true or FIFO order if false.
'''