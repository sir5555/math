#Q.1]
#1)
import matplotlib.pyplot as plt
games = ["Cricket", "Football", "Hockey", "Chess", "Tennis"]
students = [125, 59, 28, 19, 36]
plt.barh(games, students)
plt.xlabel("Number of Students")
plt.ylabel("Games")
plt.title("Students in Games")
plt.show()
#2)
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-3*np.pi, 3*np.pi, 100)
y = np.sin(x) + np.cos(x)
plt.plot(x, y, linestyle='-.')
plt.xlabel("x")
plt.ylabel("y")
plt.title("f(x) = sin(x) + cos(x)")
plt.show()
#3)
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)
X, Y = np.meshgrid(x, y)
Z = X**4 - Y**2
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, color='black')
plt.title("Surface Plot")
plt.show()
#4)
from sympy import Point, Segment
P = Point(7, 3)
Q = Point(7, -5)
R = Point(7, 1)
# Collinearity
print("Collinear:", Point.is_collinear(P, Q, R))
# Segment PQ
seg = Segment(P, Q)
# Midpoint
print("Midpoint of PQ =", seg.midpoint)
#Q.2]
#1)
import matplotlib.pyplot as plt
import numpy as np
# Original
x, y = 5, -8
# Reflection (Y-axis)
x_ref, y_ref = -x, y
# Scaling (x*4)
x_scale, y_scale = 4*x, y
# Rotation (p/2)
theta = np.pi/2
x_rot = x*np.cos(theta) - y*np.sin(theta)
y_rot = x*np.sin(theta) + y*np.cos(theta)
# Plot
plt.scatter(x, y, label="Original")
plt.scatter(x_ref, y_ref, label="Reflection")
plt.scatter(x_scale, y_scale, label="Scaling")
plt.scatter(x_rot, y_rot, label="Rotation")
plt.legend()
plt.title("Point Transformations")
plt.show()