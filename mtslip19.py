Q.1]
1)
import matplotlib.pyplot as plt
labels = ["Wild Animals", "Grazing Animals", "Birds", "Water Animals", "Reptiles"]
values = [150, 400, 225, 175, 100]
explode = (0.1, 0.1, 0.1, 0.1, 0.1)
plt.pie(values, labels=labels, explode=explode, autopct='%1.1f%%')
plt.title("Animal Distribution")
plt.show()
2)
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, np.pi/2 - 0.1, 50) # avoid infinity
y = np.tan(x)
plt.plot(x, y, color='green')
plt.xlabel("x")
plt.ylabel("y")
plt.title("y = tan(x)")
plt.show()
3)
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
x = np.linspace(1, 10, 50)
y = np.linspace(1, 10, 50)
X, Y = np.meshgrid(x, y)
Z = -X**3 - Y**3
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z)
plt.title("Surface Plot")
plt.show()
4)
from sympy import Point, Line, Eq, symbols
A = Point(7, 2)
B = Point(3, -4)
line1 = Line(A, B)
x, y = symbols('x y')
line2 = Line(Eq(2*x - y, 1))
print("Angle =", line1.angle_between(line2))
Q.2]
1)
import matplotlib.pyplot as plt
import numpy as np
# Original
A = np.array([1, -2])
B = np.array([3, 5])
# Rotation (p)
R = np.array([[-1, 0], [0, -1]])
A1 = R @ A
B1 = R @ B
# Scaling in x (×7)
A2 = np.array([7*A1[0], A1[1]])
B2 = np.array([7*B1[0], B1[1]])
# Uniform scaling (×4)
A3 = 4 * A2
B3 = 4 * B2
# Plot
plt.plot([A[0], B[0]], [A[1], B[1]], label="Original")
plt.plot([A3[0], B3[0]], [A3[1], B3[1]], label="Transformed")
plt.legend()
plt.title("Line Transformations")
plt.show()