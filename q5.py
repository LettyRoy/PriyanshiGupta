import sympy as sp

# Define the variable
x = sp.symbols('x')

# Function 1: f(x) = x^3 + 5x^2 - 3x + 7 (Find Derivative)

f1 = x**3 + 5*x**2 - 3*x + 7
derivative_f1 = sp.diff(f1, x)
print("Derivative of f(x) = x^3 + 5x^2 - 3x + 7:", derivative_f1)

# Function 2: f(x) = 4x^3 - 2x + 6 (Find Integral)
f2 = 4*x**3 - 2*x + 6
integral_f2 = sp.integrate(f2, x)
print("Integral of f(x) = 4x^3 - 2x + 6:", integral_f2)
