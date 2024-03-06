from math_operations import calculator
from math_operations import geometry

result = calculator.add(5, 3)
print("Addition result:", result)

result = calculator.subtract(10, 4)
print("Subtraction result:", result)

result = geometry.rectangle(10,10)
print("Rectangle area result:", result)

result = geometry.triangle(10,10)
print("Trianglar area result:", result)

result = geometry.circle(10)
print("Circle area result:", result)