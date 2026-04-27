Q.1]
1)
import matplotlib.pyplot as plt
subjects = ["History", "Geography", "English", "Sociology", "Psychology"]
students = [168, 90, 195, 95, 46]
plt.pie(students, labels=subjects, autopct='%1.1f%%', radius=0.7)
plt.title("Students Data")
plt.show()
2)
import matplotlib.pyplot as plt
subjects = ["History", "Geography", "English", "Sociology", "Psychology"]
students = [168, 90, 195, 95, 46]
plt.pie(students, labels=subjects, autopct='%1.1f%%', radius=0.7)
plt.title("Students Data")
plt.show()
3)
from sympy import Point
import matplotlib.pyplot as plt
A = Point(1,1)
B = Point(1,6)
C = Point(6,1)
D = Point(6,6)
x = [A.x, B.x, C.x, D.x, A.x]
y = [A.y, B.y, C.y, D.y, A.y]
plt.plot(x, y, color='black')
plt.title("Quadrilateral ABCD")
plt.show()
4)
from sympy import Point
A = Point(1,1)
B = Point(1,4)
C = Point(4,1)
D = Point(4,4)
points = [A, B, C, D]
# Shearing
sheared = [Point(p.x + 3*p.y, p.y + 7*p.x) for p in points]
print("Sheared Points:", sheared)
Q.2]
1)
import matplotlib.pyplot as plt
import numpy as np
# Original
points = np.array([[4,4], [2,4], [4,2], [4,4]])
# Rotation p/2
theta = np.pi/2
R = np.array([[0, -1], [1, 0]])
rot = np.dot(points, R)
# Scaling 3
scale = 3 * points
# Plot
plt.plot(points[:,0], points[:,1], label="Original")
plt.plot(rot[:,0], rot[:,1], label="Rotated")
plt.plot(scale[:,0], scale[:,1], label="Scaled")
# Axes
plt.axhline(0)
plt.axvline(0)
plt.legend()
plt.title("Triangle Transformations")
plt.show()