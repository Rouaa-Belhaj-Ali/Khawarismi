def khawarizmi():
    print("Enter the coefficients of the quadratic equation ax^2 + bx + c = 0: ")
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))

    discriminant = b**2 - 4*a*c

    if discriminant > 0:
        root1 = (-b + discriminant**0.5) / (2*a)
        root2 = (-b - discriminant**0.5) / (2*a)
        print("The roots are:", root1, "and", root2)
    elif discriminant == 0:
        root = -b / (2*a)
        print("The root is:", root)
    else:
        real_part = -b / (2*a)
        imag_part = (-discriminant)**0.5 / (2*a)
        print("The roots are complex numbers:", real_part + imag_part, "and", real_part - imag_part)



khawarizmi()
