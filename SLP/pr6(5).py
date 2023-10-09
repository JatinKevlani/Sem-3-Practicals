import random

def count_max_1(lists):
    counts = []
    for row in lists:
        count1 = row.count(1)
        counts.append(count1)
    maxi = counts[0]
    for i in range(len(counts)):
        maxi = max(maxi, counts[i])
    print(counts)
    print(counts.index(maxi) + 1)
    return (counts.index(maxi) + 1)

matrix = [[random.randint(0, 1) for _ in range(4)] for _ in range(4)]
print("Matrix :")
for row in matrix:
    print(row)
print(f"Maximum number of 1s appears in {count_max_1(matrix)}th row.")
cols = []
for i in range(4):
    col = []
    for j in range(4):
        col.append(matrix[j][i])
    cols.append(col)
print("Column wise matrix : ")
for row in cols:
    print(row)
print(f"Maximum number of 1s appears in {count_max_1(cols)}th column.")