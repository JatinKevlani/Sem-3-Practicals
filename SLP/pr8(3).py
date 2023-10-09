def fibonacci(num):
    if num == 0 or num == 1:
        return (num)
    else:
        return num * fibonacci(num - 1)
    
num = int(input("Enter a number : "))
print(fibonacci(num))