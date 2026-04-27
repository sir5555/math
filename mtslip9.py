#Q.1]
#1)
import numpy as np
import matplotlib.pyplot as plt
# f(x) = sin(x^2)
x1 = np.linspace(-10, 10, 100)
y1 = np.sin(x1**2)
# g(x) = cos(x^2)
x2 = np.linspace(0, np.pi, 100)
y2 = np.cos(x2**2)
plt.subplot(2, 1, 1)
plt.plot(x1, y1)
plt.title("f(x) = sin(x^2)")
plt.subplot(2, 1, 2)
plt.plot(x2, y2)
plt.title("g(x) = cos(x^2)")
plt.tight_layout()
plt.show()
#2)
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-10, 10, 100)
y = x**2 + np.exp(2*x + 5)
plt.plot(x, y, 'r-.')
plt.xlabel("x")
plt.ylabel("y")
plt.title("y = x^2 + e^(2x+5)")
plt.show()
#3)
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
x = np.linspace(-20, 20, 50)
y = np.linspace(-20, 20, 50)
X, Y = np.meshgrid(x, y)
Z = X**3 + Y**3
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, color='pink')
plt.title("Surface Plot")
plt.show()
#4)
from sympy import Point, Polygon
A = Point(0, 0)
B = Point(1, 0)
C = Point(1, 1)
D = Point(0, 1)
square = Polygon(A, B, C, D)
print("Area =", square.area)
print("Perimeter =", square.perimeter)
print("Centroid =", square.centroid)
print("Angles =", square.angles)
#Q.1]
#1)
import matplotlib.pyplot as plt
# Original
x = [4, -4, -4, 4, 4]
y = [4, 4, -4, -4, 4]
# Shearing (y - 3x)
y_shear = [y[i] - 3*x[i] for i in range(len(x))]
x_shear = x
# Reflection (x-axis)
y_ref = [-i for i in y_shear]
# Translation (x+5, y+8)
x_trans = [i + 5 for i in x_shear]
y_trans = [i + 8 for i in y_ref]
# Plot
plt.plot(x, y, label="Original")
plt.plot(x_shear, y_shear, label="Sheared")
plt.plot(x_shear, y_ref, label="Reflected")
plt.plot(x_trans, y_trans, label="Translated")
plt.legend()
plt.title("Transformations")
plt.show()