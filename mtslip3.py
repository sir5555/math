#slip 3

#q1.1
x=['mathematics','english','biology','physics','chemistry']
y=[45,35,85,50,60]
barh(x,y,height=0.5,color='brown')
xlabel('subject')
ylabel('marks')
title(' horizontal bargraph of result')
show()

#q1.2
x=linspace(-5,5,50)
y=x**3*-3*x+2
subplot(1,1,1)
plot(x,y,color='maroon',label='graph of x**3*-3*x+2',linestyle=':')
legend()
show()

#q1.3
def f(x,y):
        return sqrt(x**2+y**2)
x=np.linspace(-20,20,50)
y=np.linspace(-20,20,50)
x,y=np.meshgrid(x,y)
z=np.sqrt(y**2 + y**2)
ax=axes(projection='3d')
ax.plot_surface(x,y,z,color='red')
ax.set_zlabel('z axis')
title('3D surface graph')
show()

#q1.4
l=Point(-5,0)
m=Point(4,0)
n=Point(9,0)
print(Point.is_collinear(l,m,n))
t=Line(l,n)
print('slope of eqn',t.slope)

#q1.5
p1=RegularPolygon(Point(0,0),2,5)
v1=p1.vertices
print(v1)
x1=[v1[0][0] , v1[1][0] , v1[2][0] , v1[3][0] , v1[4][0] , v1[0][0] ]
y1=[v1[0][1] , v1[1][1] , v1[2][1] , v1[3][1] , v1[4][1] , v1[0][1] ]
plot(x1,y1)
xlabel('x axis')
ylabel('y axis')
title(' polygon graph')
show()
print(p1)
print()

#q2.1
a=Point(0,0)
b=Point(1,0)
c=Point(1,1)
d=Point(0,1)
p=Polygon([a,b,c,d])
print('og obj : ',p)
plot([a.x,b.x,c.x,d.x,a.x],[a.y,b.y,c.y,d.y,a.y],label=' og obj',color='red')
m1=Matrix([[1,0,0],[0,-1,0],[0,0,1]])
m2=Matrix([[cos(pi/4),sin(pi/4),0],[-sin(pi/4),cos(pi/4),0],[0,0,1]])
m3=Matrix([[-3,0,0],[0,-3,0],[0,0,1]])
m=m1*m2*m3
print(m)
a1=a.transform(m)
b1=b.transform(m)
c1=c.transform(m)
d1=d.transform(m)
p1=Polygon([a1,b1,c1,d1])
plot([a1.x,b1.x,c1.x,d1.x,a1.x],[a1.y,b1.y,c1.y,d1.y,a1.y],label=' transf obj',color='blue')
show()

#q2.2
p=[-20,20]
q=[0,0]
plot(p,q,label='x axis',color='black')
plot(q,p,label='y axis',color='black')
a=eval(input(' enter value of a :  '))
xmin=eval(input(' enter value of xmin :  '))
xmax=eval(input(' enter value of xmax :  '))
n=eval(input(' enter no of points n :  '))
tmin=sqrt((xmin/a))
tmax=sqrt((xmax/a))
delta=(tmax - tmin)/(n-1)
x1=a * tmin ** 2
y1=2 * a * tmin
for i in range(1,n+1):
    print(i,round(x1,4),round(y1,4))
    plot(x1,y1,marker='*',color='red')
    plot(x1, -y1,marker='*',color='red')
    x2= x1 + y1 * delta + a *(delta) ** 2
    y2= y1 + 2 * a * delta
    x1=x2
    y1=y2
title(' parabola ')
show()