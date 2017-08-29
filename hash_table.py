class HashTable:
    def __init__(self):
        universe_of_keys = range(0,26)
        self.hash_table = []
        for i in universe_of_keys:
            self.hash_table.append([])

    def _hash(self, string):
        return ord(string[0]) - 97

    def insert(self, string):
        self.hash_table[self._hash(string)].append(string)

    def print(self):
        print(self.hash_table)

ht = HashTable()
ht.insert("hello")
ht.insert("zz")
ht.insert("abc")
ht.insert("abz")
ht.print()