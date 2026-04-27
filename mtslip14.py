#Q.1]
#1)
import matplotlib.pyplot as plt
subjects = ["Mathematics", "English", "Biology", "Physics", "Chemistry"]
marks = [68, 45, 79, 56, 70]
plt.bar(subjects, marks, color='brown')
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.title("Marks Distribution")
plt.show()
#2)
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0.1, 10, 100) # avoid log(0)
y = np.log(x)
plt.plot(x, y, 'r--')
plt.xlabel("x")
plt.ylabel("y")
plt.title("y = log(x)")
plt.show()
#3)
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
x = np.linspace(-10, 10, 50)
y = np.linspace(-10, 10, 50)
X, Y = np.meshgrid(x, y)
Z = X**3 + Y**3
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, color='green')
plt.title("Surface Plot")
plt.show()
#4)
from sympy import Point, Line
P = Point(7, 2)
Q = Point(1, 8)
# Distance
print("Distance =", P.distance(Q))
# Line
line = Line(P, Q)
# Slope
print("Slope =", line.slope)
# Equation
print("Equation =", line)
#Q.2]
#1)
import matplotlib.pyplot as plt
import numpy as np
# Original
x = [1, 2, 4, 3, 1]
y = [3, 4, 2, 1, 3]
# Rotation p/2
theta1 = np.pi/2
x_rot1 = [x[i]*np.cos(theta1) - y[i]*np.sin(theta1) for i in range(len(x))]
y_rot1 = [x[i]*np.sin(theta1) + y[i]*np.cos(theta1) for i in range(len(x))]
# Rotation p
theta2 = np.pi
x_rot2 = [x[i]*np.cos(theta2) - y[i]*np.sin(theta2) for i in range(len(x))]
y_rot2 = [x[i]*np.sin(theta2) + y[i]*np.cos(theta2) for i in range(len(x))]
# Plot
plt.plot(x, y, label="Original")
plt.plot(x_rot1, y_rot1, label="Rotation p/2")
plt.plot(x_rot2, y_rot2, label="Rotation p")
# Axes
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.legend()
plt.title("Polygon Rotations")
plt.show()