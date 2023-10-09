def is_prime(number) :
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return False
    return True
print("Prime" if is_prime(int(input("Enter a number : "))) else "Not prime")