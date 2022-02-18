import random

hash_table = [0 for i in range(11)]

def save(key, value):

    index = hash(key) % len(hash_table)
    
    for i in range(index, len(hash_table)):

        if hash_table[i] == 0:
            hash_table[i] = [key, value]
            return

        elif hash_table[i][0] == key:
            hash_table[i][1] = value
            return


key_candidates = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

for i in range(7):
    save(key_candidates[i], random.randint(1, 11))

print(hash_table)