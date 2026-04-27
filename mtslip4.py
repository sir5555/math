from sympy import Matrix
from sympy.geometry import Point, Polygon

x1=linspace(-5,5,100)
y1=x1**3
subplot(2,1,1)
plot(x1,y1,color='g',label='graph of x1**3')
xlabel('x axis')
ylabel('y axis')

x2=linspace(1,10,100)
y2=e**x2
subplot(2,1,2)
plot(x2,y2,color='blue',label='graph of e**x2')
xlabel('x axis')
ylabel('y axis')

legend()
show()

x=linspace(1,20,50)
y=2*x+5
subplot(1,1,1)
plot(x,y,color='skyblue',label='graph of 2*x+5',linestyle='--')
legend()
show()

def f(x,y):
    return (cos(x**2+y**2))
x=np.linspace(0,20,50)
y=np.linspace(0,20,50)
x,y=np.meshgrid(x,y)
z=np.cos(y**2 + y**2)
ax=axes(projection='3d')
ax.plot_wireframe(x,y,z,color='brown')
ax.set_xlabel('x axis')
ylabel('y axis')
ax.set_zlabel('z axis')
title('3d wireframe graph')
show()

s=Polygon(Point(0,0),Point(1,0),Point(1,1),Point(0,1))
print(' perimeter of polygon is : ',s.perimeter)
print(' centroid of polygon is : ',s.centroid)
print(' area of polygon is : ',s.area)

p=Point(2,-1,3)
print(p)
plot(p.x,p.y,p.z,marker='*',color='red')
ax=axes(projection='3d')
m=Matrix([[cos(pi/2),-sin(pi/2),0,0],[sin(pi/2),cos(pi/2),0,0],[0,0,1,0],[0,0,0,1]])
p1=p.transform(m)
xlabel('x axis')
ylabel('y axis')
ax.set_zlabel('z axis')
title('3d point plotting')
show()

p=[-10,10]
q=[0,0]
plot(p,q,label='x axis',color='black')
plot(q,p,label='y axis',color='black')
n=100 # Default value for number of points
r=5   # Default value for radius
h,k=0,0 # Default values for center (h,k)
# Original lines were:
# n=eval(input(' enter no of points n :  '))
# r=eval(input(' enter radius of circle r  :  '))
# h,k=eval(input(' enter centre of circle h,k :  '))
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