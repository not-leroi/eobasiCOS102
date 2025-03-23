import cmath  # For handling complex numbers


def quadratic_roots(a, b, c):
    d = b ** 2 - 4 * a * c
    if d >= 0:
        root1 = (-b + cmath.sqrt(d)) / (2 * a)
        root2 = (-b - cmath.sqrt(d)) / (2 * a)
        return f"Quadratic roots: {root1}, {root2}"
    else:
        root1 = (-b + cmath.sqrt(d)) / (2 * a)
        root2 = (-b - cmath.sqrt(d)) / (2 * a)
        return f"Quadratic roots (complex): {root1}, {root2}"


def cubic_roots(a, b, c, d):
    # Using Cardano's method for solving cubic equations
    f = ((3 * c / a) - (b ** 2 / a ** 2)) / 3
    g = ((2 * b ** 3 / a ** 3) - (9 * b * c / a ** 2) + (27 * d / a)) / 27
    h = (g ** 2 / 4) + (f ** 3 / 27)

    if h > 0:
        R = -(g / 2) + cmath.sqrt(h)
        S = R ** (1 / 3)
        T = -(g / 2) - cmath.sqrt(h)
        U = T ** (1 / 3)
        root1 = (S + U) - (b / (3 * a))
        return f"One real root: {root1}"

    elif f == 0 and g == 0 and h == 0:
        root = (-d / a) ** (1 / 3)
        return f"All roots are real and equal: {root}"

    else:
        i = cmath.sqrt((g ** 2 / 4) - h)
        j = i ** (1 / 3)
        k = cmath.acos(-(g / (2 * i)))
        L = -j
        M = cmath.cos(k / 3)
        N = cmath.sqrt(3) * cmath.sin(k / 3)
        P = -b / (3 * a)

        root1 = 2 * j * cmath.cos(k / 3) - (b / (3 * a))
        root2 = L * (M + N) + P
        root3 = L * (M - N) + P
        return f"Three real roots: {root1}, {root2}, {root3}"


def quartic_roots(a, b, c, d, e):
    return "Quartic equation solving without NumPy is very complex. Use an advanced numerical method."


def main():
    print("Choose the type of equation:")
    print("2 - Quadratic (Ax² + Bx + C = 0)")
    print("3 - Cubic (Ax³ + Bx² + Cx + D = 0)")
    print("4 - Quartic (Ax⁴ + Bx³ + Cx² + Dx + E = 0)")

    degree = int(input("Enter 2, 3, or 4: "))

    if degree == 2:
        a, b, c = [float(input(f"Coefficient for x^{i}: ")) for i in range(2, -1, -1)]
        print(quadratic_roots(a, b, c))

    elif degree == 3:
        a, b, c, d = [float(input(f"Coefficient for x^{i}: ")) for i in range(3, -1, -1)]
        print(cubic_roots(a, b, c, d))

    elif degree == 4:
        print(quartic_roots(0, 0, 0, 0, 0))  # Placeholder
    else:
        print("Invalid choice.")


main()
