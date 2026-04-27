#slip 8
import numpy as np
import matplotlib.pyplot as plt
from sympy.geometry import Point, Line, Polygon, RegularPolygon
from mpl_toolkits.mplot3d import Axes3D
#q1.1
x_cities=['satara','dhule','Nashik ','Nagpur','Pune']
y_temps=[20,32,25,40,30]
plt.figure()
plt.bar(x_cities,y_temps,width=0.5,color='pink')
plt.xlabel('city')
plt.ylabel('temperature')
plt.title('bargraph of climate')
plt.show()

#q1.2
x1_wave=np.linspace(-np.pi,np.pi,50)
y1_wave=(np.cos(x1_wave)+np.sin(x1_wave))
plt.figure()
plt.plot(x1_wave,y1_wave,color='maroon',label='graph of (cos(x1)+sin(x1))')
plt.legend()
plt.show()

#q1.3
def f_3d(x,y):
        return (np.sin(np.sqrt(x**2+y**2)))
x_grid=np.linspace(0,2*np.pi,50)
y_grid=np.linspace(0,2*np.pi,50)
x_grid,y_grid=np.meshgrid(x_grid,y_grid)
z_grid=f_3d(x_grid,y_grid)
fig_3d = plt.figure()
ax_3d=fig_3d.add_subplot(projection='3d')
ax_3d.plot_wireframe(x_grid,y_grid,z_grid,color='brown')
ax_3d.set_xlabel('x axis')
ax_3d.set_ylabel('y axis')
ax_3d.set_zlabel('z axis')
plt.title('3d wireframe graph')
plt.show()

#q1.4
l_pt=Point(2,6)
m_pt=Point(-2,9)
n_pt=Point(-3,-5)
print(Point.is_collinear(l_pt,m_pt,n_pt))
print('distance betn l and m is: ',l_pt.distance(m_pt))
print('distance betn l and n is: ',l_pt.distance(n_pt))
print('distance betn n and m is: ',n_pt.distance(m_pt))
t_line=Line(l_pt,m_pt)
print('slope of eqn',t_line.slope)

#q1.5
p_regpoly=RegularPolygon(Point(0,0),6,6)
v_verts=p_regpoly.vertices
print(v_verts)
x_verts=[ v_verts[0][0] ,  v_verts[1][0] , v_verts[2][0] , v_verts[3][0] , v_verts[4][0] , v_verts[5][0], v_verts[0][0] ]
y_verts=[ v_verts[0][1] ,  v_verts[1][1] , v_verts[2][1] , v_verts[3][1] , v_verts[4][1] , v_verts[5][1], v_verts[0][1] ]
plt.figure()
plt.plot(x_verts,y_verts)
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('polygon graph')

print('area of polygon',p_regpoly.area)
print('perimeter of polygon',p_regpoly.perimeter)
print('translate in x dir',p_regpoly.translate(8,0))
plt.show()

#q2.1
a_pt=Point(-2,5)
b_pt=Point(-2,9)
c_pt=Point(3,5)
d_pt=Point(4,2)
p_poly=Polygon(a_pt,b_pt,c_pt,d_pt)
print(p_poly)
x_poly_coords=[a_pt.x,b_pt.x,c_pt.x,d_pt.x,a_pt.x]
y_poly_coords=[a_pt.y,b_pt.y,c_pt.y,d_pt.y,a_pt.y]
plt.figure()
plt.plot(x_poly_coords,y_poly_coords,'pink')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('polygon')
plt.show()

p1_translated=p_poly.translate(2,-5)
print(p1_translated)

#q2.2
p_circ_axis=[-10,10]
q_circ_axis=[0,0]
plt.figure()
plt.plot(p_circ_axis,q_circ_axis,label='x axis',color='black')
plt.plot(q_circ_axis,p_circ_axis,label='y axis',color='black')
n_pts_circ=10 # Hardcoded value instead of eval(input(' enter no of points n : '))
r_circ_rad=5 # Hardcoded value instead of eval(input(' enter radius of circle r : '))
h_circ_center,k_circ_center=0,0 # Hardcoded values instead of eval(input(' enter centre of circle h,k : '))
deltheta=(2*np.pi)/n_pts_circ
x1_curr_circ=r_circ_rad
y1_curr_circ=0
for i in range(0,n_pts_circ+1):
    print([i,round(x1_curr_circ,4),round(y1_curr_circ,4)])
    plt.plot(x1_curr_circ,y1_curr_circ,marker='*',color='red')
    x2_next_circ= x1_curr_circ * np.cos(deltheta) - y1_curr_circ * np.sin(deltheta)
    y2_next_circ= x1_curr_circ * np.sin(deltheta) + y1_curr_circ * np.cos(deltheta)
    x1_curr_circ=x2_next_circ
    y1_curr_circ=y2_next_circ
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('generation of points on circle')
plt.show()