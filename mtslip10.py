#Q.1]
#1)
import matplotlib.pyplot as plt
years = ["2020", "2021", "2022", "2023", "2024"]
matches = [50, 40, 30, 67, 45]
plt.barh(years, matches, color='blue')
plt.xlabel("Number of Matches")
plt.ylabel("Year")
plt.title("Matches per Year")
plt.show()
#2)
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-10, 20, 100)
y = x**2 - 5
plt.plot(x, y, color='red', marker='>')
plt.xlabel("x")
plt.ylabel("y")
plt.title("y = x^2 - 5")
plt.show()
#3)
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
x = np.linspace(0, 2*np.pi, 50)
y = np.linspace(0, 2*np.pi, 50)
X, Y = np.meshgrid(x, y)
Z = np.cos(np.sqrt(abs(X**2 - Y**2)))
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_wireframe(X, Y, Z, color='green')
plt.title("Wireframe Plot")
plt.show()
#4)
from sympy import Point, RegularPolygon
center = Point(0, 0)
polygon = RegularPolygon(center, 5, 4)
print("Area =", polygon.area)
print("Perimeter =", polygon.perimeter)
print("Vertices =", polygon.vertices)
print("Angles =", polygon.angles)
#Q.2]
#1)
import matplotlib.pyplot as plt
import numpy as np
# Original
x = [0, 8, 7, 0]
y = [0, -9, 4, 0]
# Scaling (x*5, y*-6)
x_scale = [i*5 for i in x]
y_scale = [i*(-6) for i in y]
# Reflection (x-axis)
y_ref = [-i for i in y]
# Rotation (60°)
theta = np.radians(60)
x_rot = [x[i]*np.cos(theta) - y[i]*np.sin(theta) for i in range(len(x))]
y_rot = [x[i]*np.sin(theta) + y[i]*np.cos(theta) for i in range(len(x))]
# Plot
plt.plot(x, y, label="Original")
plt.plot(x_scale, y_scale, label="Scaled")
plt.plot(x, y_ref, label="Reflected")
plt.plot(x_rot, y_rot, label="Rotated")
plt.legend()
plt.title("Triangle Transformations")
plt.show()