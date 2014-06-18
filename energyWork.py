from visual import *
from visual.graph import *

scene = display(title='Throwing a ball',x=100, y=10, width=1200, height=800,  center=(50,50,0),background=color.white)
ground = box(pos=(50,-1,0), axis=(250,0,0), lenght=250,height=1,width=20, color=color.red)
graph_velocity = gdisplay(title='Velocity',x=1200,y=200,xtitle='time(sec)',ytitle='V(m/s)',foreground=color.black, background=color.white)

graph_energy = gdisplay(title='Energy',x=1200,y=200,xtitle='time(sec)',ytitle='Energy(Joule)', foreground=color.black, background=color.white)
graph_work = gdisplay(title='Work',x=1200,y=200,xtitle='time(sec)',ytitle='Work(Joule)', foreground=color.black, background=color.white)

#Parameter initialization
dott_radius = 1.5
x0 = -50
g = 9.8
theta = 60*pi/180
speed = 50
dt=.01
t=0
tc = 0
vix=50*cos(theta)
viy=50*sin(theta)
cc =0.5
rho = 0.005


# set processing rate
myrate=200
# start program mouse click event handler
scene.mouse.getclick()
print (('Gravitation only'))

#Ball object setup
ball = sphere(pos=( x0 ,0 ,0), mass= 0.2, v=vector(speed*cos(theta), speed*sin(theta),0) , radius=0.5, color=color.blue,  make_trail=True  )

#Graphical output initialization
vx_curve = gcurve(gdisplay=graph_velocity, color=ball.color)
vy_curve = gcurve(gdisplay=graph_velocity, color=ball.color)

#Graphical output for energy and work initialization
work_curve    = gcurve(gdisplay=graph_work, color=color.green)
energy_curve    = gcurve(gdisplay=graph_energy, color=color.red)

#Ball momentum
ball.p = ball.mass*ball.v

#Time paramter initialiazation
dt=.01
t=0
tc = 0


#
# Place initial sphere
#

sphere(pos=ball.pos, radius=dott_radius, color=ball.color)
#
# initialze ball velocity from previous while loop
#
ballvy_old = ball.v.y

# initialize KE and work
KE = 0
work = 0
##############################################
# process loop (action)####################
##############################################
# ^^^^^this means create a while loop
while(ball.y>=0):
    # set your rate
    rate(myrate)
    ##############################################
    # PHYSICS    >>>>>>             ##############
    ##############################################
    # calculate force on ball
    FG = vector (0,-ball.mass*g, 0)

    # MOMENTUM PRINCIPLE
    ball.p += FG*dt

    # update ball velocity
    ball.v = (ball.p/ball.mass)

    # update ball position
    ball.pos += (ball.p/ball.mass)*dt


    ##############################################
    # PHYSICS    <<<<<<<<<    ####################
    ##############################################

    # transfer ball x, y velocity to graphing paramters
    vx = ball.p.x/ball.mass
    vy = ball.p.y/ball.mass


    # plot velocity
    vx_curve.plot(pos=(t,vx))
    vy_curve.plot(pos=(t,vy))

    ####################################################
    ######################### energy and work   ########
    # calculate KE and work
    KE = .5*ball.mass*mag(ball.v)**2
    dx=ball.v*dt
    work += dot(FG,dx)
    # plot KE and work
    energy_curve.plot(pos=(t,KE))
    work_curve.plot(pos=(t,work))

    ######################### energy and work   ########
    ####################################################
    # find maximum height of ball and print it out
    if ballvy_old*ball.v.y <=0 :
        print("Max height is "+ str(ball.pos.y) +"m")
    ballvy_old = ball.v.y
    # update time paramters
    t+=dt
    tc+=dt

    # place a ball periodically on path
    if tc>1.0:
        tc =0
        sphere(pos=ball.pos, radius=dott_radius, color =ball.color)
# print final distance traversed
print(" time= %.1f s , distance = %.2f m "%(t,ball.pos.x-x0))
#############################################################################
# Add air resistance  #########################
###############################################
#
# start this part of the program with mouse click event
#

# print title gravity and air resistance
print (('Gravitation + Air drag'))

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
ballvy_old = ball.v.y

ball = sphere(pos=( x0 ,0 ,0), mass= 0.2, v=vector(speed*cos(theta), speed*sin(theta),0) ,
              radius=0.5, color=color.red,  make_trail=True)

sphere(pos=ball.pos, radius=dott_radius, color=ball.color)
ball.p = ball.mass*ball.v

#
# initialize graphical output
#
vx2_curve    = gcurve(gdisplay=graph_velocity, color=color.black)
vy2_curve    = gcurve(gdisplay=graph_velocity, color=color.black)

#
# initialize graphical output for energy and work
#
work2_curve    = gcurve(gdisplay=graph_work, color=color.black)
energy2_curve    = gcurve(gdisplay=graph_energy, color=color.black)


# initialize variable and objects etc etc
while(ball.y>=0):
    # set your rate
    rate(myrate)
    ##############################################
    # PHYSICS    >>>>>>             ##############
    ##############################################
    # calculate force on ball
    FG = vector (0,-ball.mass*g, 0)
    fair = -0.5*cc*rho*pi*(ball.radius**2) * (mag(ball.v)**2) * norm(ball.v)
    f =FG+fair
    # MOMENTUM PRINCIPLE
    ball.p += f*dt

    # update ball velocity
    ball.v = (ball.p/ball.mass)

    # update ball position
    ball.pos += (ball.p/ball.mass)*dt


    ##############################################
    # PHYSICS    <<<<<<<<<    ####################
    ##############################################

    # transfer ball x, y velocity to graphing paramters
    vx2 = ball.p.x/ball.mass
    vy2 = ball.p.y/ball.mass


    # plot velocity
    vx2_curve.plot(pos=(t,vx2))
    vy2_curve.plot(pos=(t,vy2))

    ####################################################
    ######################### energy and work   ########
    # calculate KE and work
    KE = .5*ball.mass*mag(ball.v)**2
    dx=ball.v*dt
    work += dot(f,dx)
    # plot KE and work
    energy2_curve.plot(pos=(t,KE))
    work2_curve.plot(pos=(t,work))

    ######################### energy and work   ########
    ####################################################
    # find maximum height of ball and print it out
    if ballvy_old*ball.v.y <=0 :
        print("Max height is "+ str(ball.pos.y) +"m")
    ballvy_old = ball.v.y
    # update time paramters
    t+=dt
    tc+=dt

    # place a ball periodically on path
    if tc>1.0:
        tc =0
        sphere(pos=ball.pos, radius=dott_radius, color =color.yellow)
# print final distance traversed
print(" time= %.1f s , distance = %.2f m "%(t,ball.pos.x-x0))



###############################################
# Add air resistance + wind  ##################
###############################################
#
# start this part of the program
#

# print title gravity and air resistance
print (('Gravitation + Air drag'))
# initialize variable and objects etc etc
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
ballvy_old = ball.v.y

ball = sphere(pos=( x0 ,0 ,0), mass= 0.2, v=vector(speed*cos(theta), speed*sin(theta),0) ,
              radius=0.5, color=color.orange,  make_trail=True)

sphere(pos=ball.pos, radius=dott_radius, color=ball.color)
ball.p = ball.mass*ball.v

#
# initialize graphical output
#
vx3_curve    = gcurve(gdisplay=graph_velocity, color=color.red)
vy3_curve    = gcurve(gdisplay=graph_velocity, color=color.red)

#
# initialize graphical output for energy and work
#
work3_curve    = gcurve(gdisplay=graph_work, color=color.red)
energy3_curve    = gcurve(gdisplay=graph_energy, color=color.red)

while(ball.y>=0):
    # set your rate
    rate(myrate)
    ##############################################
    # PHYSICS    >>>>>>             ##############
    ##############################################
    # calculate force on ball
    FG = vector (0,-ball.mass*g, 0)
    wind=vector(-20,0,0)
    fair = -0.5*cc*rho*pi*(ball.radius**2) * (mag(ball.v-wind)**2) * norm(ball.v-wind)
    f =FG+fair
    # MOMENTUM PRINCIPLE
    ball.p += f*dt

    # update ball velocity
    ball.v = (ball.p/ball.mass)

    # update ball position
    ball.pos += (ball.p/ball.mass)*dt


    ##############################################
    # PHYSICS    <<<<<<<<<    ####################
    ##############################################

    # transfer ball x, y velocity to graphing paramters
    vx3 = ball.p.x/ball.mass
    vy3 = ball.p.y/ball.mass


    # plot velocity
    vx3_curve.plot(pos=(t,vx3))
    vy3_curve.plot(pos=(t,vy3))

    ####################################################
    ######################### energy and work   ########
    # calculate KE and work
    KE = .5*ball.mass*mag(ball.v)**2
    dx=ball.v*dt
    work += dot(f,dx)
    # plot KE and work
    energy3_curve.plot(pos=(t,KE))
    work3_curve.plot(pos=(t,work))

    ######################### energy and work   ########
    ####################################################
    # find maximum height of ball and print it out
    if ballvy_old*ball.v.y <=0 :
        print("Max height is "+ str(ball.pos.y) +"m")
    ballvy_old = ball.v.y
    # update time paramters
    t+=dt
    tc+=dt

    # place a ball periodically on path
    if tc>1.0:
        tc =0
        sphere(pos=ball.pos, radius=dott_radius, color =color.black)
# print final distance traversed
print(" time= %.1f s , distance = %.2f m "%(t,ball.pos.x-x0))

######### END OF PROGRAM #######################################
