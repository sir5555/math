Q.1]
1)
import matplotlib.pyplot as plt
subjects = ["Computer", "Mathematics", "Electronics", "Statistics", "English"]
marks = [60, 80, 65, 55, 70]
explode = (0.1, 0.1, 0.1, 0.1, 0.1)
plt.pie(marks, labels=subjects, autopct='%1.1f%%', explode=explode)
plt.title("Subject Marks")
plt.show()
2)
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-5*np.pi, 5*np.pi, 100)
y = np.sin(3*x + 1)
plt.plot(x, y, color='red', linestyle=':')
plt.xlabel("x")
plt.ylabel("y")
plt.title("f(x) = sin(3x + 1)")
plt.show()
3)
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
x = np.linspace(-10, 20, 50)
y = np.linspace(-10, 20, 50)
X, Y = np.meshgrid(x, y)
Z = -(X**2 + Y**2)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z)
plt.title("Surface Plot")
plt.show()
4)
from sympy import symbols, Eq, solve
x, y = symbols('x y')
# Equations
eq1 = Eq(x + y, 2)
eq2 = Eq(3*x + 2*y, 1)
# Intersection
sol = solve((eq1, eq2), (x, y))
print("Intersection =", sol)
# Slopes
# x + y = 2 ? y = -x + 2 ? slope = -1
# 3x + 2y = 1 ? y = (-3/2)x + 1/2 ? slope = -3/2
print("Slope of L1 =", -1)
print("Slope of L2 =", -3/2)
Q.2]
1)
import matplotlib.pyplot as plt
import numpy as np
# Original
P = np.array([5, -2])
Q = np.array([3, 2])
# Rotation (p)
R = np.array([[-1, 0], [0, -1]])
P1 = R @ P
Q1 = R @ Q
# Scaling (x * 4)
P2 = np.array([4*P1[0], P1[1]])
Q2 = np.array([4*Q1[0], Q1[1]])
# Reflection (y = x)
P3 = np.array([P2[1], P2[0]])
Q3 = np.array([Q2[1], Q2[0]])
# Plot
plt.plot([P[0], Q[0]], [P[1], Q[1]], label="Original")
plt.plot([P3[0], Q3[0]], [P3[1], Q3[1]], label="Transformed")
plt.legend()
plt.title("Line Transformations")
plt.show()