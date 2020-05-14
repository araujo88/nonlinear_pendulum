# Non-linear pendulum solver via explicit finite-difference scheme
# Author: Leonardo Antonio de Araujo
# E-mail: leonardo.aa88@gmail.com
# Date: 08/05/2020
import math
import matplotlib.pyplot as plt
import numpy as np

# Parameters
G=9.806 # gravity acceleration
L=0.25 # pendulum length
T=4 # final time
V0=1 # initial velocity
theta0=math.pi # initial position
dt=0.01 # time step

# Total number of iterations
it = int(T/dt)

# Initialize vectors
theta=np.zeros(it)
x=np.zeros(it)
y=np.zeros(it)
t=np.zeros(it)

# Initial conditions
theta[0]=theta0
theta[1]=V0*dt+theta[0]
x[0]=-L*math.sin(theta[0])
x[1]=-L*math.sin(theta[1])
y[0]=-L*math.cos(theta[0])
y[1]=-L*math.cos(theta[1])
t[0]=0
t[1]=dt

# Main time loop
for i in range(1,it-1):

	# Solves for theta
	theta[i+1]=((-dt**2)*G/L)*math.sin(theta[i])+2*theta[i]-theta[i-1]  
	t[i+1]=t[i]+dt
	x[i+1]=-L*math.sin(theta[i+1])
	y[i+1]=-L*math.cos(theta[i+1])

	# Figure plot
	fig, ax = plt.subplots()
	plt.axis([-L, L, -L, L])
	plt.plot([0,x[i]],[0,y[i]])
	circle1 = plt.Circle((0, 0), 0.005, color='r')
	circle2 = plt.Circle((x[i], y[i]), 0.01, color='k')
	ax.add_artist(circle1)
	ax.add_artist(circle2)
	plt.gca().set_aspect('equal', adjustable='box')
	plt.savefig('figure-' + str(i) + '.png')

