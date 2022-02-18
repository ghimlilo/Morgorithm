import random

hash_table = [0 for i in range(11)]

def save(key, value):

    index = hash(key) % len(hash_table)
    

    if hash_table[index] !=0:

        for data in hash_table[index]:
            if data[0] == key:
                data[1] = value
                return
        
        return hash_table[index].append([key, value])
    
    hash_table[index] = [[key, value]]
    return

key_candidates = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

for i in range(7):
    save(key_candidates[i], random.randint(1, 11))

print(hash_table)