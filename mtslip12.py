#Q.1]
#1)
import matplotlib.pyplot as plt
subjects = ["Mathematics", "English", "Biology", "Physics", "Chemistry"]
marks = [84, 48, 60, 35, 72]
plt.pie(marks, labels=subjects, autopct='%1.1f%%')
plt.title("Marks Distribution")
plt.show()
#2)
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-np.pi, np.pi, 100)
y = np.cos(2*x)
plt.plot(x, y, color='red', linestyle='--')
plt.xlabel("x")
plt.ylabel("y")
plt.title("y = cos(2x)")
plt.show()
#3)
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
x = np.linspace(-10, 10, 50)
y = np.linspace(-10, 10, 50)
X, Y = np.meshgrid(x, y)
Z = np.sin(X**2 + Y**2)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_wireframe(X, Y, Z, color='brown')
plt.title("Wireframe Plot")
plt.show()
#4)
from sympy import Point
P = Point(0, 0)
Q = Point(1, 1)
R = Point(-7, 5)
# Distances
print("Distance QP =", Q.distance(P))
print("Distance RP =", R.distance(P))
# Midpoint of QR
print("Midpoint QR =", Q.midpoint(R))
#Q.2]
#1)
import matplotlib.pyplot as plt
# Original
x = [1, 3, 4, 1]
y = [3, 3, 5, 3]
# Reflection y = x
x1 = y
y1 = x
# Reflection y = -x
x2 = [-yi for yi in y]
y2 = [-xi for xi in x]
# Plot
plt.plot(x, y, label="Original")
plt.plot(x1, y1, label="Reflection y=x")
plt.plot(x2, y2, label="Reflection y=-x")
plt.legend()
plt.title("Triangle Reflections")
plt.show()