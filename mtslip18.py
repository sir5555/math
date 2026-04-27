Q.1]
1)
import matplotlib.pyplot as plt
ages = [21,29,35,21,41,36,32,24,43,27,38,34,31,22,39,26,34,26,44,37,37,31,30,22,39]
bins = [20,25,30,35,40,45]
plt.hist(ages, bins=bins, color='maroon')
plt.xlabel("Age Groups")
plt.ylabel("Number of Donors")
plt.title("Histogram of Blood Donors")
plt.show()
2)
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-7, 10, 100)
y = 2*x**2 + 6*x + 10
plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("y")
plt.title("y = 2x^2 + 6x + 10")
plt.show()
3)
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
x = np.linspace(-15, 10, 50)
y = np.linspace(-15, 10, 50)
X, Y = np.meshgrid(x, y)
Z = -(X**2 + Y**2)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, color='green')
plt.title("Surface Plot")
plt.show()
4)
from sympy import symbols, Eq, solve, Line
x, y = symbols('x y')
# Equations
eq1 = Eq(x + y, 2)
eq2 = Eq(3*x + 2*y, 1)
# Intersection
sol = solve((eq1, eq2), (x, y))
print("Intersection =", sol)
# Lines
line1 = Line(Eq(x + y, 2))
line2 = Line(Eq(3*x + 2*y, 1))
# Angle
print("Angle =", line1.angle_between(line2))
Q.2]
1)
import matplotlib.pyplot as plt
# Original
x = [1, 4, 4, 1]
y = [2, 2, 5, 2]
# Scaling 0.5
x_s1 = [i*0.5 for i in x]
y_s1 = [i*0.5 for i in y]
# Scaling 4
x_s2 = [i*4 for i in x]
y_s2 = [i*4 for i in y]
# Plot
plt.plot(x, y, label="Original")
plt.plot(x_s1, y_s1, label="Scale 0.5")
plt.plot(x_s2, y_s2, label="Scale 4")
plt.legend()
plt.title("Triangle Scaling")
plt.show()