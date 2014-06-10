#Ball Shooting Simulation(Gravity + Air Resistance + Wind) (VPython Source)

from visual import *
from visual.graph import *

#Set up area on screen to display objects
scene = display(title='Throwing a ball',x=100, y=10, width=1200, height=800,  center=(50,50,0),background=color.white)

#Graphical Output Setup
graph_velocity = gdisplay(title='Velocity',x=1200,y=200,xtitle='time(sec)',ytitle='V(m/s)', foreground=color.black, background=color.white)

#Initialize parameters
dott_radius = 1.5
x0 = -50
g = 9.8
theta = 60*pi/180
speed = 50
dt=1
t=0
tc = 0
vix=50*cos(theta)
viy=50*sin(theta)

#Base Steup
ground = box(pos=(50,-1,0), axis=(250,0,0), lenght=250,height=1,width=20, color=color.green)
ground.color=color.purple

#Processing rate Setup
myrate=200 #for while loop

#Start Program
scene.mouse.getclick()

#Print title
print (('Gravitation only'))

#Ball object setup

ball = sphere(pos=( x0 ,0 ,0), mass= 0.2, v=vector(speed*cos(theta), speed*sin(theta),0),radius=0.5, color=color.blue,  make_trail=True  )
ball.p = ball.mass*ball.v
ballvy_old = 0

#Graphical output initializations

vx_curve    = gcurve(gdisplay=graph_velocity, color=ball.color)
vy_curve    = gcurve(gdisplay=graph_velocity, color=ball.color)

#Initial ball placement
sphere(pos=ball.pos, radius=dott_radius, color=ball.color)

while(ball.y>=0):
    rate(myrate)

    #Force vector definition
    FG = vector (0,-ball.mass*g, 0)
    #update momentum
    ball.p += FG*dt
    #update velocity
    ball.v = (ball.p/ball.mass)
    #update position
    ball.pos += (ball.p/ball.mass)*dt


    #velocity for plot x ,y
    vx = ball.p.x/ball.mass
    vy = ball.p.y/ball.mass



    vx_curve.plot(pos=(t,vx))
    vy_curve.plot(pos=(t,vy))


    if ballvy_old*ball.v.y <0 :
        print("Max height is "+ str(ball.pos.y) +"m")
    ballvy_old = ball.v.y
    t+=dt
    tc+=dt
    if tc>1.0:
        tc =0
        sphere(pos=ball.pos, radius=dott_radius, color =ball.color)
print(" time= %.1f s , distance = %.2f m "%(t,ball.pos.x-x0))
print("")
#########################################################################################################
print (('Gravitation + Air drag:'))

#Initialize parameters
dott_radius = 1.5
x0 = -50
g = 9.8
theta = 60*pi/180
speed = 50
dt=.01
t=0
tc = 0
cc =0.5
rho = 0.005

ball = sphere(pos=( x0 ,0 ,0), mass= 0.2, v=vector(speed*cos(theta), speed*sin(theta),0) ,radius=0.5, color=color.green,  make_trail=True  )
ball.p = ball.mass*ball.v
ballvy_old = ball.v.y

vx_curve    = gcurve(gdisplay=graph_velocity, color=ball.color)
vy_curve    = gcurve(gdisplay=graph_velocity, color=ball.color)

#Place initial ball
sphere(pos=ball.pos, radius=dott_radius, color=ball.color)
while(ball.y>=0):
    rate(myrate)

    # define force
    FG = vector (0,-ball.mass*g, 0)
    fair = -0.5*cc*rho*pi*(ball.radius**2) * (mag(ball.v)**2) * norm(ball.v)
    f =FG+fair
    # update momentum
    ball.p += f*dt
    # update velocity
    ball.v = (ball.p/ball.mass)
    # update position
    ball.pos += (ball.p/ball.mass)*dt


    # velocity for plot x ,y
    vx = ball.p.x/ball.mass
    vy = ball.p.y/ball.mass



    vx_curve.plot(pos=(t,vx))
    vy_curve.plot(pos=(t,vy))

    if ballvy_old*ball.v.y <=0 :
        print("Max height is "+ str(ball.pos.y) +"m")
    ballvy_old = ball.v.y

    t+=dt
    tc+=dt
    if tc>1.0:
        tc =0
        sphere(pos=ball.pos, radius=dott_radius, color =ball.color)
print(" time= %.1f s , distance = %.2f m "%(t,ball.pos.x-x0))
print("")

############################################################################
print (('Gravitation + Air drag + Wind'))

#Initialize parameters
dott_radius = 1.5
x0 = -50
g = 9.8
theta = 60*pi/180
speed = 50
dt=.01
t=0
tc = 0
cc =0.5
rho = 0.005



ball = sphere(pos=( x0 ,0 ,0), mass= 0.2, v=vector(speed*cos(theta), speed*sin(theta),0) ,radius=0.5, color=color.yellow,  make_trail=True  )
ball.p = ball.mass*ball.v
ballvy_old = ball.v.y

vx_curve    = gcurve(gdisplay=graph_velocity, color=ball.color)
vy_curve    = gcurve(gdisplay=graph_velocity, color=ball.color)

#Place initial ball
sphere(pos=ball.pos, radius=dott_radius, color=ball.color)


while(ball.y>=0):
    rate(myrate)

    # define force
    FG = vector (0,-ball.mass*g, 0)
    wind=vector(-20,0,0)
    fair = -0.5*cc*rho*pi*(ball.radius**2) * (mag(ball.v-wind)**2) * norm(ball.v-wind)
    f =FG+fair
    # update momentum
    ball.p += f*dt
    # update velocity
    ball.v = (ball.p/ball.mass)
    # update position
    ball.pos += (ball.p/ball.mass)*dt
    
    # velocity for plot x ,y
    vx = ball.p.x/ball.mass
    vy = ball.p.y/ball.mass

    vx_curve.plot(pos=(t,vx))
    vy_curve.plot(pos=(t,vy))


    if ballvy_old*ball.v.y <=0 :
        print("Max height is "+ str(ball.pos.y) +"m")
    ballvy_old = ball.v.y

    t+=dt
    tc+=dt
    if tc>1.0:
        tc =0
        sphere(pos=ball.pos, radius=dott_radius, color =ball.color)
print(" time= %.1f s , distance = %.2f m "%(t,ball.pos.x-x0))
print("")
