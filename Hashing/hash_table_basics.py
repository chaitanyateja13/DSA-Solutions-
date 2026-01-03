# Using Python dictionary as hash table
hash_table = {}

# Insert
hash_table["apple"] = 10
hash_table["banana"] = 20

# Access
print(hash_table["apple"])

# Delete
del hash_table["banana"]

# Check existence
print("banana" in hash_table)
print("apple" in hash_table)
