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
    
     # Use the discriminant to determine the number of roots and calculate the roots using the quadratic formula
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        print("The quadratic equation has two real roots: {0:.2f} and {1:.2f}".format(root1, root2))
    elif discriminant == 0:
        root = -b / (2*a)
        print("The quadratic equation has one real root: {0:.2f}".format(root))
    else:
        real_part = -b / (2*a)
        imag_part = math.sqrt(-discriminant) / (2*a)
        print("The quadratic equation has two complex roots: {0:.2f} + {1:.2f}i and {0:.2f} - {1:.2f}i".format(real_part, imag_part))










