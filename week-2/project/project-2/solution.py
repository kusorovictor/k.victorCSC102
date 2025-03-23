import math
import cmath 

def solve_cubic(a, b, c, d):
    # Convert to depressed cubic form
    p = (3 * a * c - b**2) / (3 * a**2)
    q = (2 * b**3 - 9 * a * b * c + 27 * a**2 * d) / (27 * a**3)

    # Compute the discriminant 
    delta = (q / 2) ** 2 + (p / 3) ** 3

    # Solve based on the discriminant
    if delta > 0:
        A = (-q / 2 + math.sqrt(delta)) ** (1/3)
        B = (-q / 2 - math.sqrt(delta)) ** (1/3)
        t1 = A + B
        t2 = complex(-0.5 * (A + B), (math.sqrt(3) / 2) * (A - B))
        t3 = complex(-0.5 * (A + B), -(math.sqrt(3) / 2) * (A - B))

    elif delta == 0:
        A = (-q / 2) ** (1/3)
        t1 = 2 * A
        t2 = -A
        t3 = -A

    else:
        r = math.sqrt(-p / 3)
        theta = math.acos(-q / (2 * r**3))

        t1 = 2 * r * math.cos(theta / 3)
        t2 = 2 * r * math.cos((theta + 2 * math.pi) / 3)
        t3 = 2 * r * math.cos((theta + 4 * math.pi) / 3)

    x1 = t1 - b / (3 * a)
    x2 = t2 - b / (3 * a)
    x3 = t3 - b / (3 * a)

    return x1, x2, x3



a = int(input("Enter the coefficient of x^3: "))
b = int(input("Enter the coefficient of x^2: "))
c = int(input("Enter the coefficient of x: "))
d = int(input("Enter the constant term: "))

roots = solve_cubic(a, b, c, d)
print("The roots are:", roots)
