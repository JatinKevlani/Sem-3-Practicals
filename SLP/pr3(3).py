amount = int(input("Enter principal amount : "))
roi = int(input("Enter rate of interest : "))
t = int(input("Enter time period : "))
print("Simple Interest :", (amount * roi * t) / 100)
n = int(input("Enter number of times interest applied per time period : "))
print("Compound Interest :", amount * ((1 + (roi / (100 * n))) ** (n * t)))