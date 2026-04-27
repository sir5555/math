#Q.1]
#1)
import matplotlib.pyplot as plt
marks = [71,29,35,21,66,32,24,27,38,44,51,42,49,86,94,46,57,47,41,50,46]
bins = [20, 40, 60, 80, 100]
plt.hist(marks, bins=bins, color='brown')
plt.xlabel("Marks Range")
plt.ylabel("Number of Students")
plt.title("Histogram of Marks")
plt.show()
#2)
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, np.pi/2, 100)
y = x**2 + np.cos(2*x + 5)
plt.plot(x, y, color='red')
# Arrow lines
plt.arrow(0, 0, 1, 0, head_width=0.1, color='black')
plt.arrow(0, 0, 0, 1, head_width=0.1, color='black')
plt.xlabel("x")
plt.ylabel("y")
plt.title("y = x^2 + cos(2x + 5)")
plt.show()
#3)
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
x = np.linspace(0, 2*np.pi, 50)
y = np.linspace(0, 2*np.pi, 50)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, color='brown')
plt.title("Surface Plot")
plt.show()
#4)
from sympy import symbols, Eq, solve, Line
x, y = symbols('x y')
# Equations
eq1 = Eq(3*x + 5*y, 4)
eq2 = Eq(x - 5*y, 8)
# Solve intersection
sol = solve((eq1, eq2), (x, y))
print("Intersection =", sol)
# Lines
line1 = Line(Eq(3*x + 5*y, 4))
line2 = Line(Eq(x - 5*y, 8))
# Angle
print("Angle =", line1.angle_between(line2))
#Q.2]
#1)
import matplotlib.pyplot as plt
import numpy as np
# Original
x = [10, -7, 8, 10]
y = [5, 4, -3, 5]
# Reflection (y-axis)
x_ref = [-i for i in x]
y_ref = y
# Rotation (90°)
x_rot = [-y_ref[i] for i in range(len(x))]
y_rot = [x_ref[i] for i in range(len(x))]
# Scaling (×7)
x_scale = [7*i for i in x_rot]
y_scale = [7*i for i in y_rot]
# Plot
plt.plot(x, y, label="Original")
plt.plot(x_ref, y_ref, label="Reflected")
plt.plot(x_rot, y_rot, label="Rotated")
plt.plot(x_scale, y_scale, label="Scaled")
plt.legend()
plt.title("Triangle Transformations")
plt.show()