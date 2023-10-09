a = []
for i in range(10):
    n = int(input("Enter integer : "))
    a.append(n)
print("Combinations of picking two a from the list:")
n = len(a)
for i in range(n):
    for j in range(i + 1, n):
        print(a[i],a[j])