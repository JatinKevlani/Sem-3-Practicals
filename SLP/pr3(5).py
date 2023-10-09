a = int(input("Enter value 1 : "))
b = int(input("Enter value 2 : "))
c = int(input("Enter value 3 : "))
print("Maximum number is :", a if(a > b and b > c) else (b if b > a and b > c else c))