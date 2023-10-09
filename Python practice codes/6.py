def is_palindrome(number):
    number = str(number)
    if number == number[::-1]:
        return True
    return False
print("Palindrome" if is_palindrome(int(input("Enter a number : "))) else "Not palindrome")