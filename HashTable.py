
#Hashtable class that consist of insert and search function
class HashTable:
    def __init__(self, initial_capacity=10):
        self.table = [[] for _ in range(initial_capacity)]

    #Insert Function of hash_table
    #O(1) - Time complexity
    #O(n) - Space Complexity
    def insert(self, key, item):
        bucket =hash(key) % 10
        bucket_values = self.table[bucket]

    #if key already in the table, function updates the value
        for key_value in bucket_values:
            if key_value[0] == key:
                key_value[1] = item
                return True


    #if the key is not in the table, function appends key and values to the table
        key_value = [key, item]
        bucket_values.append(key_value)
        return True


    #Search Function of HasH_table that takes key as input and return values if key is found
    #O(1) Time complexity
    #O(1) Space Complexity
    def search(self, key):
        bucket =hash(key) % 10
        bucket_values = self.table[bucket]

        #search for the key and return the relative values
        for key_value in bucket_values:
            if key_value[0] == key:
                return key_value[1]

        #If value is not found it returns none
        return None



