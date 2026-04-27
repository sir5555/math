#slip 2

#Q1.1
x=[34,50,24,10,82]
y=['cricket','football','badminton','hockey','other']
pie(x,labels=y,radius=0.5,autopct='%1.1f%%')
legend()
title(' piechart for sports students')
show()

#q1.2
x=linspace(-10,10,50)
y=x**2+5
subplot(1,1,1)
plot(x,y,color='g',label='graph of x**2+5',linestyle='--')
legend()
show()

#q1.3
def f(x,y):
    return(x**2-y**2)
x=np.linspace(-20,20,50)
y=np.linspace(-20,20,50)
x,y=np.meshgrid(x,y)
z=f(x,y)
ax=axes(projection='3d')
ax.plot_wireframe(x,y,z,color='brown')
ax.set_xlabel('x axis')
ylabel('y axis')
ax.set_zlabel('z axis')
title('3d wireframe graph')
show()

#q1.4
p=Point(-4,5)
x,y=symbols('x,y')

print('scaling',p.scale(2,0))
l=Line(y-x)
print('reflection',p.reflect(l))
print('translation',p.translate(0,7))

#q1.5
a=Point(3,0)
b=Point(0,4)
c=Point(-3,0)
t=Triangle(a,b,c)

print(' area of triangle is :  ',t.area)
print(' perimeter of triangle is : ',t.perimeter)
print(' angles of triangle are :   ',t.angles)
show()

#q2.1
a=Point(1,1)
b=Point(-5,1)
c=Point(-5,-4)
d=Point(1,-4)
p=Polygon([a,b,c,d])
x1=[a.x,b.x,c.x,d.x,a.x]
y1=[a.y,b.y,c.y,d.y,a.y]
plot(x1,y1,label='original polygon',color='red')

a1=a.rotate(pi/2)
b1=b.rotate(pi/2)
c1=c.rotate(pi/2)
d1=d.rotate(pi/2)
x2=[a1.x,b1.x,c1.x,d1.x,a1.x]
y2=[a1.y,b1.y,c1.y,d1.y,a1.y]
plot(x2,y2,label='rotate about 90',color='blue')
xlabel('x axis')
ylabel('y axis')
legend()
show()

#2.2

from matplotlib.pyplot import*
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