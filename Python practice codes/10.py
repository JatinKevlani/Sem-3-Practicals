max = -999999999999
while True:
    user = input("Enter a number : ")
    if user.lower() == "done":
        break
    if max < int(user):
        max = int(user)
print(max)