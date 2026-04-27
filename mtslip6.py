#slip 6

import numpy as np
import matplotlib.pyplot as plt
from sympy.geometry import Point, RegularPolygon, Polygon
from math import e, pi # Import e and pi for use as constants
from mpl_toolkits.mplot3d import Axes3D # For 3D axes

#q1.1

# Plot 1
x1=np.linspace(-10,10,100)
y1=x1**2
plt.figure() # Create a new figure for each plot block
plt.subplot(1,1,1)
plt.plot(x1,y1,color='g',label='graph of x1**2')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.legend()
plt.title('Graph of x^2')
plt.show()

# Plot 2
x2=np.linspace(1,10,100)
y2=e**2*x2+4 # Using math.e for the constant e
plt.figure() # Create a new figure for each plot block
# plt.subplot(1,2,1) -- This subplot config would place it next to the previous one, which is already shown.
# To avoid issues, using separate figures with plt.show(). If combined, need a single figure with multiple subplots.
plt.plot(x2,y2,color='blue',label='graph of e**2*x2+4')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.legend()
plt.title('Graph of e^2*x + 4')
plt.show()


#q1.2
x=np.linspace(-20,20,50)
y=x**2+2*x+5
plt.plot(x,y,color='r',label='graph of x**2+2*x+5',linestyle=':') # Fixed linestyle from 'dot' to ':'
plt.legend()
plt.show()

#q1.3
def f(x,y):
    return (np.sin(x**2+y**2))
x=np.linspace(0,2*np.pi,50)
y=np.linspace(-20,20,50)
x,y=np.meshgrid(x,y)
z=np.sin(x**2+y**2)
fig = plt.figure()
ax = fig.add_subplot(projection='3d') # Correct way to get 3D axes
ax.plot_wireframe(x,y,z,color='brown')
ax.set_xlabel('x axis')
ax.set_ylabel('y axis') # Corrected to ax.set_ylabel
ax.set_zlabel('z axis')
plt.title('3d wireframe graph') # Corrected to plt.title
plt.show()

#q1.4
p1=RegularPolygon(Point(0,0),4,5) # center, radius, n (number of sides)
v1=p1.vertices
print(v1)
x1=[v1[0][0] , v1[1][0] , v1[2][0] , v1[3][0] , v1[4][0] , v1[0][0] ]
y1=[v1[0][1] , v1[1][1] , v1[2][1] , v1[3][1] , v1[4][1] , v1[0][1] ]
plt.plot(x1,y1)
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title(' polygon graph')
plt.show()
print(p1)
print()

#q1.5
a=Point(2,2)
b=Point(6,2)
c=Point(6,6)
d=Point(2,6)
p=Polygon(a,b,c,d) # Sympy Polygon expects individual points, not a list
print(' area of polygon : ',p.area)
print(' perimeter of polygon : ',p.perimeter)
print(' angles of polygon : ',p.angles)

#q2.2
p_circ=[-10,10] # Renamed to avoid conflict with sympy Point
q_circ=[0,0] # Renamed to avoid conflict with sympy Point
plt.plot(p_circ,q_circ,label='x axis',color='black')
plt.plot(q_circ,p_circ,label='y axis',color='black')

# Replace eval(input()) with default values for non-interactive execution
n_circ=100 # enter no of points n
r_circ=5   # enter radius of circle r
h_circ,k_circ=0,0 # enter centre of circle h,k

deltheta=(2*np.pi)/n_circ # Using np.pi
x1=r_circ
y1=0
for i in range(0,n_circ+1):
        print([1,round(x1,4),round(y1,4)])
        plt.plot(x1,y1,marker='*',color='red')
        x2= x1 * np.cos(deltheta) - y1 * np.sin(deltheta) # Using np.cos, np.sin
        y2= x1 * np.sin(deltheta) + y1 * np.cos(deltheta) # Using np.sin, np.cos
        x1=x2
        y1=y2
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('generation of 100 points on circle')
plt.show()