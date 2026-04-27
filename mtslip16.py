#Q.1]
#1)
import matplotlib.pyplot as plt
fruits = ["Mango", "Grapes", "Banana", "Other"]
students = [65, 30, 20, 15]
plt.pie(students, labels=fruits, autopct='%1.1f%%')
plt.title("Students Favourite Fruits")
plt.show()
#2)
import matplotlib.pyplot as plt
x = [2, 5]
y = [4, 6]
plt.plot(x, y, color='green')
plt.xlabel("x")
plt.ylabel("y")
plt.title("Line joining two points")
plt.show()
#3)
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
x = np.linspace(-15, 15, 50)
y = np.linspace(-15, 15, 50)
X, Y = np.meshgrid(x, y)
Z = -X**3 - Y**3
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_wireframe(X, Y, Z, color='brown')
plt.title("Wireframe Plot")
plt.show()
#4)
from sympy import Point, Polygon
A = Point(6, 2)
B = Point(4, 8)
C = Point(12, 9)
D = Point(5, 3)
quad = Polygon(A, B, C, D)
print("Area =", quad.area)
print("Perimeter =", quad.perimeter)
#Q.2]
#1)
import matplotlib.pyplot as plt
# Original
x = [1, 4, 4, 2, 1]
y = [2, 2, 4, 5, 2]
# Shearing (x + 3y, y - 2x)
x_shear = [x[i] + 3*y[i] for i in range(len(x))]
y_shear = [y[i] - 2*x[i] for i in range(len(x))]
# Plot
plt.plot(x, y, label="Original")
plt.plot(x_shear, y_shear, label="Sheared")
# Axes
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.legend()
plt.title("Polygon Shearing")
plt.show()