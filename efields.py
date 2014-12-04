# charge moving in a magnetic field
#
from visual import *
# set up scene for visualization
scene = display(width = 1024,height = 768, x=100, y=100, background = color.white, range=(1,1,1) )
# designate visibility parameter 1 = True
arrowvis = 1

# set position parameters
xmax = .5
dx = xmax/5.

# set up a set of locations to represent the B field
grid = []
for x in arange(-xmax, xmax+dx, dx):
    grid.append(curve(pos=[(x,0,-xmax),(x,0,xmax)], color=(.6,.6,.6)))
for z in arange(-xmax, xmax+dx, dx):
    grid.append(curve(pos=[(-xmax,0,z),(xmax,0,z)],color=(.6,.6,.6)))

# set up B field representation
B0 = vector(0,1,0)

bfield=[]
bscale = (xmax/3.)/mag(B0)
for x in arange(-xmax, xmax+dx, 2*dx):
    for z in arange(-xmax, xmax+dx, 2*dx):
        bfield.append(arrow(pos=(x,0,z), axis=B0*bscale, color=(0,.8,.8)))

## set up particle: place it inside or outside area of uniform B and designate charge
## there are several cases to try:
## (For example)
## Outside:       pos=(0.75*xmax,dx,2*xmax), charge positive
## Inside:        pos=(-xmax/2.,dx,xmax/2.), charge positive
## Outside:       pos=(-0.75*xmax, dx ,2*xmax), charge negative
## Inside:        pos=(xmax/2.,dx, xmax/2. ), charge negative
 # Outside:       pos=(xmax/2.,dx, 2*xmax - 3*dx), charge negative 
particle = sphere(pos=(xmax/2.,dx, 2*xmax - 3*dx), mass = 1.7e-27, charge= -1.6e-19,
                  v = vector(0,1.e6,-1e7),
                  color=(0,0,1), radius = dx/8, make_trail=True)
# initial momentum
particle.p = particle.mass*particle.v

# set up an arrow to show force on the particle
farrow = arrow(pos=particle.pos, axis=(0,0,0), color=(0.6,0.6,0.6))
# scale and visualize arrow
fscale = 1.e11
farrow.visible = arrowvis
# set up an arrow to show velocity on the particle
varrow = arrow(pos=particle.pos, axis=(0,0,0), color=color.green)
# scale and visualize arrow
vscale = 1e-8
varrow.visible = arrowvis
# time
dt = (xmax/(mag(particle.p)/particle.mass))/1000.
scene.mouse.getclick()
t = 0.
# dynamics loop - motion of particle through B field
# constrain motion to area of interest
while particle.pos.z < xmax + 3.1*dx  and particle.pos.y < xmax:

    rate(500)
    # set up B field in a specific location and nowhere else
    if -xmax < particle.x < xmax and -xmax < particle.z < xmax:
        B = B0
    else:
        B = vector(0,0,0)
    #### PHYSICS HERE ###
    # calculate velocity
    particle.v = particle.p/particle.mass
    # calculate force
    F = particle.charge*cross(particle.v,B)
    # calculate momentum
    particle.p += F*dt
    # calculate position
    particle.pos += dt*particle.v
    #### PHYSICS HERE ### 
    # update position and dimension of arrow
    farrow.pos = particle.pos
    farrow.axis = F*fscale
    varrow.pos = particle.pos
    varrow.axis = particle.v*vscale
    #### update time ###

    t += dt


