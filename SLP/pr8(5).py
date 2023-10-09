def gcd(m, n):
    if m == 0:
        return n
    else:
        return gcd(n % m, m)

num1 = int(input("Enter number 1 : "))
num2 = int(input("Enter number 2 : "))
print(f"The GCD of {num1} and {num2} is {gcd(num1, num2)}")