def fibonacci(n):
    fib_series = []
    a, b = 0, 1
    for _ in range(n):
        fib_series.append(a)
        a, b = b, a + b
    return fib_series

n = int(input("Enter the number of terms for Fibonacci series: "))
fib_series = fibonacci(n)
print("Fibonacci series : ", fib_series)