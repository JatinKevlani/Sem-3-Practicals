set1 = {"ABC", 1, True, 2, 7.8}
set2 = {"XYZ", 6, False, 8, 6.9, 1}
print(set1)
print(set2)
set1.remove("ABC")
print(set1)
print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))
print(set1.symmetric_difference(set2))
print(set1.issubset(set2))