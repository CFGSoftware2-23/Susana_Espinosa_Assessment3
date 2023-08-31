def basic_hash_function(key, table_size):
    hash_value = 0
    for char in key:
        hash_value += ord(char)  # Add ASCII value of each character
    return hash_value % table_size  # Modulo to fit within table size


table_size = 10  # Size of the hash table


#using separate chaining to handle collisions


class HashTable:
    def __init__(self, size):
        self.table_size = size
        self.table = [[] for _ in range(size)]  # Each index contains a list

    def insert(self, key, value):
        index = basic_hash_function(key, self.table_size)
        self.table[index].append((key, value))  # Append key-value pair to the list

    def get(self, key):
        index = basic_hash_function(key, self.table_size)
        for stored_key, value in self.table[index]:
            if stored_key == key:
                return value
        return None  # Key not found

# Example usage
hash_table = HashTable(table_size)
hash_table.insert("name", "Susana")
hash_table.insert("age", 34)

print(hash_table.get("name"))  # Output: John
print(hash_table.get("age"))   # Output: 25


