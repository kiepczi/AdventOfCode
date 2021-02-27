#Loading data
with open("day_6.txt", "r") as handle:
    joined = "".join(handle)
    group_data = joined.strip().split("\n\n")
    ans = [items.replace('\n', '') for items in group_data]
    


#PART 1

#sets of individual answers
singletons = []
for items in ans:
    sets = set(items)
    singletons.append(sets)

#Counting answers
counter = 0
for items in singletons:
    for char in items:
        counter += 1

print(counter)


#PART 2

#Loading data
with open("day_6.txt", "r") as handle:
    joined = "".join(handle)
    group_data = joined.strip().split("\n\n")
    ans = [items.split('\n') for items in group_data]

from collections import Counter

counter = 0
for item in ans:
    group_size = len(item)
    counts = Counter("".join(item))
    counts = Counter(list(counts.values()))[group_size]
    counter += counts
print(counter)

