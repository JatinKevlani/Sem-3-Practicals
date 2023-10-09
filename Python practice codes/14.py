import math

def calculate_quadratic_roots(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2 * a)
        return root
    else:
        real_part = -b / (2 * a)
        imaginary_part = math.sqrt(abs(discriminant)) / (2 * a)
        return complex(real_part, imaginary_part)
    
print(calculate_quadratic_roots(float(input("Enter the coefficient of x^2 (a) : ")), float(input("Enter the coefficient of x (b) : ")), float(input("Enter the constant term (c) : "))))