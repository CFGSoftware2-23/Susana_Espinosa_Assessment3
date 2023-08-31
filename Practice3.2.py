# Example where thee is no hash collision based on previous answer

#---continues from Practice 3.1---

hash_table = HashTable(10)

# Insert key-value pairs
hash_table.insert("name", "Susana")
hash_table.insert("age", 34)
hash_table.insert("city", "Murcia")

# Get values using keys
name_value = hash_table.get("name")
age_value = hash_table.get("age")
city_value = hash_table.get("city")

# Print the retrieved values
print("Name:", name_value)
print("Age:", age_value)
print("City:", city_value)

# In the code above there are no hash collisions as each key is hashed and maps to a different index in the hash table.
# when the values are retrieved the corresponding keys we get the correct values without issues. The basic_hash_function
# computes the hash values in ASCII values of the characters in the keys and uses modulo arithmetic to map them to indices
# within the hash table. Since the keys ("name," "age," and "city") have distinct characters and lengths, they result in different hash
# values and map to different indices, preventing any collisions in this scenario.