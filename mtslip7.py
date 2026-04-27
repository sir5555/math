import numpy as np
import matplotlib.pyplot as plt
from sympy.geometry import Point, Polygon
from math import e
from mpl_toolkits.mplot3d import Axes3D

x=[20,40,30,10,15]
y=['food','education','rent','travelling','other']
plt.pie(x,labels=y,radius=0.5,autopct='%1.1f%%',explode=[1,0.5,1,1,0])
plt.legend()
plt.title(' piechart for expenses')
plt.show()

x=np.linspace(0,10,50)
y=np.exp(x)
plt.plot(x,y,color='maroon',label='graph of e**x',linestyle='dotted')
plt.legend()
plt.show()

def f(x,y):
        return (np.exp(x**2+y**2))
x=np.linspace(-10,10,50)
y=np.linspace(-10,10,50)
x,y=np.meshgrid(x,y)
z=np.exp(x**2+y**2)
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot_surface(x,y,z,color='red')
ax.set_zlabel('z axis')
plt.title('3D surface graph')
plt.show()

p=Polygon(Point(4,3),Point(-4,3),Point(-4,-3),Point(4,-3))
print(' area of polygon : ',p.area)
print(' centroid of polygon: ',p.centroid)
print(' perimeter of polygon : ',p.perimeter)
print(' angles in polygon : ',p.angles)

p_parabola=[-20,20]
q_parabola=[0,0]
plt.plot(p_parabola,q_parabola,label='x axis',color='black')
plt.plot(q_parabola,p_parabola,label='y axis',color='black')
n=10
a=1
xmin=0
xmax=20
tmin=np.sqrt((xmin/a))
tmax=np.sqrt((xmax/a))
delta=(tmax - tmin)/(n-1)
x1=a*tmin**2
y1=2*a*tmin
for i in range(1,n+1):
    print([i,round(x1,4),round(y1,4)])
    plt.plot(x1,y1,marker='*',color='red')
    plt.plot(x1, -y1,marker='*',color='red')
    x2= x1+y1*delta +a*(delta)** 2
    y2= x1+2*a*delta
    x1=x2
    y1=y2
plt.title(' parabola ')
plt.show()