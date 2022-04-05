l = [1, 4, 1, 6, 'hello', 'a', 5, 'hello']
counter = {}

for i in l:
    counter[i] = counter.get(i, 0) + 1

l_repro = {i: count for i, count in counter.items() if count > 1}

print(l_repro)