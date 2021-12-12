import math
import matplotlib.pyplot as plt
from matplotlib import animation
import random as rnd

fig, ax = plt.subplots()

sx=3*math.pi
sy=2*math.pi
N=10000
alpha=10
beta=7.5
p=2
sm=1
k=1
omega=1
phi=0
t=36*math.pi
frps=60
sec=30
dt=t/(frps*sec)

x0=[]
y0=[]
x=[]
y=[]

for i in range(N):
	x0.append(sx*(1-2*rnd.random()))
	y0.append(sy*rnd.random())
	x.append(0)
	y.append(0)

def run(frame):
	plt.clf()
	ax=plt.gca()
	ax.set_aspect(1)
	plt.xlim([-sx,sx])
	plt.ylim([0,2*sy])
	ax.set_facecolor('xkcd:black')
	for i in range(N):
		x[i]=x0[i]+((y0[i]/alpha)**p)*sm*math.cos(k*x0[i]-omega*frame*dt+phi)
		y[i]=y0[i]+((y0[i]/beta)**p)*sm*math.sin(k*x0[i]-omega*frame*dt+phi)
	plt.scatter(x,y,s=1,c='r')

ani=animation.FuncAnimation(fig,run,frames=frps*sec)
writervideo=animation.FFMpegWriter(fps=frps)
ani.save('wwrp.mp4',writer=writervideo)
plt.show()


