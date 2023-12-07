class Node:
    def __init__(self,key,val):
        self.key = key
        self.val  = val
        self.prev = None
        self.next = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.hash = dict()
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.hash:
            node = self.hash[key]
            k = node.val
            self.bringfront(node)
            return k
        else:
            return -1
        
    def addElement(self,key,val):
        p = Node(key,val)
        self.hash[key] = p
        p.next = self.head.next
        self.head.next.prev = p
        p.prev = self.head
        self.head.next = p


    def bringfront(self,node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = self.head 
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        

    def removeLRU(self):
        nodeVal = self.tail.prev.key
        del self.hash[nodeVal]
        self.tail.prev.prev.next = self.tail
        self.tail.prev = self.tail.prev.prev

        
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.hash:
            self.bringfront(self.hash[key])
            self.hash[key].val = value
        elif len(self.hash) == self.capacity:
            self.removeLRU()
            self.addElement(key,value)
        else:
            self.addElement(key,value)

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
