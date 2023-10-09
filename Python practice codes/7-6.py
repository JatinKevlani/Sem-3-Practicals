for i in range(1, 6):
    for space in range(6 - i - 1):
        print(" ", end="")
    for j in range(i):
        print(i, end="")
    print()