class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def _hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash_function(key)
        self.table[index] = value

    def search(self, key):
        index = self._hash_function(key)
        return self.table[index]

    def delete(self, key):
        index = self._hash_function(key)
        self.table[index] = None


# Example usage
hash_table = HashTable(10)
hash_table.insert("apple", 5)
hash_table.insert("banana", 10)
print(hash_table.search("apple"))  # Output: 5
hash_table.delete("apple")
print(hash_table.search("apple"))  # Output: None
