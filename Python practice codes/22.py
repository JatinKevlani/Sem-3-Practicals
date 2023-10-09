my_list = [1, 1, 2, 3, 4, 4]
new_list = list(set(my_list))
counts = []
for item in new_list:
    counts.append(my_list.count(item))
print(counts)