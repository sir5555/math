#slip1

from numpy import*
from sympy import*
from math import *
from matplotlib.pyplot import*

#q1.1
x=['mathematics','english','biology','physics','chemistry']
y=[68,45,79,56,70]
bar(x,y,width=0.5,color='brown')
xlabel('subject')
ylabel('marks')
title('bargraph of result')
show()

#1.2
x=linspace(-10,10,50)
y=x**3+10*x-5
plot(x,y,color='r',label='graph of x**3+10*x-5',linestyle='--')
legend()
show()

#1.3
def f(x,y):
        return(x**2+y**2)
x=np.linspace(-10,10,50)
y=np.linspace(-10,10,50)
x,y=np.meshgrid(x,y)
z=f(x,y)
ax=axes(projection='3d')
ax.plot_surface(x,y,z,color='pink')
ax.set_zlabel('z axis')
title('3D surface graph')
show()

#1.4


p=Point(7,2)
q=Point(1,8)
print('distance between point p and q ',p.distance(q))
l=Line(p,q)
print('slope of eqn',l.slope)

#1.5
a=Point(2,2)
b=Point(4,2)
c=Point(3,6)
t=Triangle(a,b,c)
print('centroid of triangle',t.centroid)

m1=Matrix([[2,0,0],[0,1,0],[0,0,1]])
print(m1)
a1=a.transform(m1)
b1=b.transform(m1)
c1=c.transform(m1)
print(a1)
print(b1)
print(c1)

#Q2

#2.1
p=Point(4,3)
q=Point(6,3)
r=Point(6,5)
s=Point(4,5)
T=Polygon([p,q,r,s])
x1=[p.x,q.x,r.x,s.x,p.x]
y1=[p.y,q.y,r.y,s.y,p.y]
plot(x1,y1,label='original polygon',color='red')

reflect_axis = Line(Point(0,0), Point(1,0)) # Correctly define X-axis as a Line object
print(reflect_axis)
p1=p.reflect(reflect_axis)
q1=q.reflect(reflect_axis)
r1=r.reflect(reflect_axis)
s1=s.reflect(reflect_axis)
x2=[p1.x,q1.x,r1.x,s1.x,p1.x]
y2=[p1.y,q1.y,r1.y,s1.y,p1.y]
plot(x2,y2,label='reflect x axis',color='green')

show()

#2.2
p=[-10,10]
q=[0,0]
plot(p,q,label='x axis',color='black')
plot(q,p,label='y axis',color='black')
n=eval(input(' enter no of points n :  '))
r=eval(input(' enter radius of circle r  :  '))
h,k=eval(input(' enter centre of circle h,k :  '))
deltheta=(2*pi)/n
x1=r
y1=0
for i in range(0,n+1):
    print([1,round(x1,4),round(y1,4)])
    plot(x1,y1,marker='*',color='red')
    x2= x1 * cos(deltheta) - y1 * sin(deltheta)
    y2= x1 * sin(deltheta) + y1 * cos(deltheta)
    x1=x2
    y1=y2
xlabel('x axis')
ylabel('y axis')
title('generation of 100 points on circle')
show()