class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity
        self.left,self.right = Node(-1,-1),Node(-1,-1)
        self.left.next,self.right.prev = self.right,self.left

    def add(self,node):
        pre,nxt = self.right.prev,self.right
        node.prev,pre.next = pre,node
        node.next,nxt.prev = nxt,node

    def remove(self,node):
        pre,nxt = node.prev,node.next
        pre.next,nxt.prev = nxt,pre

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        self.remove(self.cache[key])
        self.add(self.cache[key])
        return self.cache[key].val
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
            del self.cache[key]
        
        if self.cap==len(self.cache):
            node = self.left.next
            self.remove(node)
            del self.cache[node.key]

        self.cache[key] = Node(key,value)
        self.add(self.cache[key])


        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)