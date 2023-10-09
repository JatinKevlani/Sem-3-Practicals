counter = 0
sum = 0
while True:
    user = input("Enter a number : ")
    if user.lower() == "exit":
        break
    counter += 1
    sum += int(user)
print("Average :", sum / counter)