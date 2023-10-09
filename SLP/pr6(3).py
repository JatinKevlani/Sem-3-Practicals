string = input("Enter a string : ")
counts = {}
for char in string:
    if char.isdigit():
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
for key, values in counts.items():
    print(f"{key} : {values} times")