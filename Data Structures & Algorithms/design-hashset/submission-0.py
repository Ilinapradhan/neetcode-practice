class MyHashSet:

    def __init__(self):
        self.size = 1000
        # Create 1000 empty buckets
        self.table = [[] for _ in range(self.size)]

    def _hash(self, key):
        # Simple modulo math to find the bucket index
        return key % self.size

    def add(self, key: int) -> None:
        bucket_idx = self._hash(key)
        if key not in self.table[bucket_idx]:
            self.table[bucket_idx].append(key)

    def remove(self, key: int) -> None:
        bucket_idx = self._hash(key)
        if key in self.table[bucket_idx]:
            self.table[bucket_idx].remove(key)

    def contains(self, key: int) -> bool:
        bucket_idx = self._hash(key)
        return key in self.table[bucket_idx]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)