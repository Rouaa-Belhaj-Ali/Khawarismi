import math

print("Enter the coefficients of the quadratic equation ax^2 + bx + c = 0: ")
a, b, c = map(float, input().split())

discriminant = b**2 - 4*a*c

if discriminant > 0:
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    print("The roots are:", root1, "and", root2)
elif discriminant == 0:
    root = -b / (2*a)
    print("The root is:", root)
else:
    real_part = -b / (2*a)
    imag_part = math.sqrt(-discriminant) / (2*a)
    print("The roots are complex numbers:", real_part + imag_part, "and", real_part - imag_part)


