#slip 5

import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols
from sympy.geometry import Point, Line, Triangle
from mpl_toolkits.mplot3d import Axes3D # For 3D axes

#q1.1
x=['2016','2017','2018','2019','2020']
y=[45,50,60,55,70]
colors = ['red', 'blue', 'green', 'orange', 'purple']
plt.bar(x,y,width=0.6,color=colors)
plt.xlabel('years')
plt.ylabel('sale of newspaper')
plt.title('bargraph of newspaper')
plt.show()

#1.2
x=np.linspace(-20,20,50)
y=x**2+2*x+5
plt.plot(x,y,color='r',label='graph of x**2+2*x+5',linestyle=':') # Fixed linestyle
plt.legend()
plt.show()

#1.3
def f(x,y):
        return np.sqrt(x**2-y**2)
x=np.linspace(-10,10,50)
y=np.linspace(-10,10,50)
x,y=np.meshgrid(x,y)

# Explicitly handle the domain for sqrt to avoid RuntimeWarning
z_vals = x**2 - y**2
z = np.where(z_vals >= 0, np.sqrt(z_vals), np.nan)

fig = plt.figure()
ax = fig.add_subplot(projection='3d') # Correct way to get 3D axes
ax.plot_surface(x,y,z,color='pink')
ax.set_zlabel('z axis')
plt.title('3D surface graph')
plt.show()

#1.4
a=Point(2,-4)
b=Point(2,8)
l1=Line(a,b)

p=Point(5,4)
q=Point(-8,3)
l2=Line(p,q)

print('point of intersection betwen ab and pq : ',l1.intersection(l2))
print('distance betwn point a and line pq is : ',l2.distance(a))
print(' equation of line ab : ',l1.equation())
print(' equation of line pq : ',l2.equation())

#1.5
o=Point(0,0)
a=Point(7,-2)
b=Point(3,6)
t=Triangle(o,a,b)
x_sym,y_sym=symbols('x,y') # Renamed x,y to x_sym,y_sym to avoid conflict with numpy arrays
print('scaling in x and y :',o.scale(3,-7),a.scale(3,-7),b.scale(3,-7))
l=Line(y_sym-x_sym)
print('reflection : ',t.reflect(l))

#2.2
p_parabola=[-20,20] # Renamed to avoid conflict with sympy Point
q_parabola=[0,0] # Renamed to avoid conflict with sympy Point
plt.plot(p_parabola,q_parabola,label='x axis',color='black')
plt.plot(q_parabola,p_parabola,label='y axis',color='black') # Removed duplicate label
n_parabola=10 # Default value for n
a_parabola=1 # Default value for a
xmin_parabola=0 # Default value for xmin
xmax_parabola=20 # Default value for xmax
# Original lines were:
# n=eval(input(' enter no of points n :  '))
# a=eval(input(' enter value of a :  '))
# xmin=eval(input(' enter value of xmin :  '))
# xmax=eval(input(' enter value of xmax :  '))
tmin=np.sqrt((xmin_parabola/a_parabola))
tmax=np.sqrt((xmax_parabola/a_parabola))
delta=(tmax - tmin)/(n_parabola-1)
x1=a_parabola * tmin ** 2
y1=2 * a_parabola * tmin
for i in range(1,n_parabola+1):
    print([i,round(x1,4),round(y1,4)])
    plt.plot(x1,y1,marker='*',color='red')
    plt.plot(x1,-y1,marker='*',color='red')
    x2= x1 + y1 * delta + a_parabola *(delta) ** 2
    y2= x1 + 2 * a_parabola * delta # This formula seems to be independent of y1 and likely incorrect for the next point's y-coordinate if it's meant to be a smooth curve.
    x1=x2
    y1=y2
plt.title(' parabola ')
plt.show()