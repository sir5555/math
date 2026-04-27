#Q.1]
#1)
import matplotlib.pyplot as plt
subjects = ["Mathematics", "English", "Biology", "Physics", "Chemistry"]
marks = [85, 15, 50, 67, 77]
plt.pie(marks, labels=subjects, autopct='%1.1f%%')
plt.title("Marks Distribution")
plt.show()
#2)
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-np.pi, np.pi, 100)
y = np.cos(x**2)
plt.plot(x, y, color='red', linestyle='--')
plt.xlabel("x")
plt.ylabel("y")
plt.title("y = cos(x^2)")
plt.show()
#3)
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
x = np.linspace(-10, 10, 50)
y = np.linspace(-10, 10, 50)
X, Y = np.meshgrid(x, y)
Z = X**2 - Y**2
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_wireframe(X, Y, Z, color='brown')
plt.title("Wireframe Plot")
plt.show()
#4)
from sympy import Point, Polygon, pi
P = Point(0, 0)
Q = Point(1, 1)
R = Point(-1, 1)
S = Point(-1, -1)
T = Point(1, -1)
poly = Polygon(P, Q, R, S, T)
#Centroid
print("Centroid =", poly.centroid)
# Rotation by pi radians
rotated = [p.rotate(pi) for p in poly.vertices]
print("Rotated Points =", rotated)
#Q.2]
#1)
import matplotlib.pyplot as plt
# Original
x = [0, -3, -3, 0, 0]
y = [3, 3, 0, 0, 3]
# Reflection y = x
x_ref = y
y_ref = x
# Scaling (×4)
x_scale = [4*i for i in x]
y_scale = [4*i for i in y]
# Plot
plt.plot(x, y, label="Original")
plt.plot(x_ref, y_ref, label="Reflection y=x")
plt.plot(x_scale, y_scale, label="Scaled")
plt.legend()
plt.title("Polygon Transformations")
plt.show()