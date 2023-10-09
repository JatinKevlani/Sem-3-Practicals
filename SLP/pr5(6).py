a = []
for x in range(1, 10001):
    x = sum([d for d in range(1, x) if x % d == 0])
    if x == x:
        a.append(x)
        if len(a) == 4:
            break
print("The first four perfect numbers up to 10,000 are:", *a)