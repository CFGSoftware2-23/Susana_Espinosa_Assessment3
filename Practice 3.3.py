# Create a hash table with a size of 5
hash_table = HashTable(5)

# Insert key-value pairs that result in hash collisions
hash_table.insert("sunny", "clear skies")
hash_table.insert("rainy", "wet and cloudy")
hash_table.insert("cloudy", "overcast")
hash_table.insert("foggy", "misty and hazy")
hash_table.insert("stormy", "thunder and lightning")

# Get values using keys that cause a collision
sunny_description = hash_table.get("sunny")
stormy_description = hash_table.get("stormy")

# Print the retrieved values
print("Sunny:", sunny_description)
print("Stormy:", stormy_description)

# In this example there is a hash collision due to the keys "sunny" and "stormy." Even though these weather conditions
# are quite distinct, the basic_hash_function and the chosen table size might result in a collision. The hash table handles
# this collision through separate chaining. As a result, the hash table correctly retrieves the descriptions associated with the
# keys using separate chaining.

