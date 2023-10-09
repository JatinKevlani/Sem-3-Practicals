n=int(input("Enter number of integers to find avg : "))
a=0
for i in range(n):
    a+=int(input("Number : "))
print(a//n)