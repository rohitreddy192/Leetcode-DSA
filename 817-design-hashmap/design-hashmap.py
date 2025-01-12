class Map:
    def __init__(self,key,val,next=None):
        self.key = key
        self.val = val
        self.next = next


class MyHashMap:

    def __init__(self):
        self.capacity = 100
        self.buckets = [None for _ in range(100)]

    def getBucketIndex(self,key):
        return hash(key) % self.capacity

    def put(self, key: int, value: int) -> None:
        idx = self.getBucketIndex(key)
        bucketNode = self.buckets[idx]
        if not bucketNode:
            self.buckets[idx] = Map(key,value)
        while bucketNode:
            if not bucketNode.next and bucketNode.key != key:
                bucketNode.next = Map(key,value)
                return
            if bucketNode.key == key:
                bucketNode.val = value
                return
            bucketNode = bucketNode.next


    def get(self, key: int) -> int:
        idx = self.getBucketIndex(key)
        bucketNode = self.buckets[idx]
        while bucketNode:
            if bucketNode.key==key:
                return bucketNode.val
            bucketNode = bucketNode.next
        return -1
        

    def remove(self, key: int) -> None:
        idx = self.getBucketIndex(key)
        bucketNode = self.buckets[idx]
        if not bucketNode:
            return  # Key not found

        # Handle removal of the head node
        if bucketNode.key == key:
            self.buckets[idx] = bucketNode.next
            return

        # Traverse the chain to find and remove the node
        prev = bucketNode
        curr = bucketNode.next
        while curr:
            if curr.key == key:
                prev.next = curr.next
                return
            prev, curr = curr, curr.next
