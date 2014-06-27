# -*- coding: utf-8 -*-
from __future__ import division
from visual import *
from visual.graph import *
##
# Set up area on screen to display objects
##
scene = display(title=' Turning around on a circle ',
     x=100, y=10, width=1000, height=1000,  range=5e11,  background=color.white)
scene.userzoom = True
#
# set up graph output
#
graph_velocity = gdisplay(title='Velocity ( v_x - red, v_y - blue, v_z – green)',x=1200,y=200,xtitle='time(sec)',ytitle='V(m/s)',
                   foreground=color.black, background=color.white)

#Distance between sun and Earth

r0_es = 1.496e11

#
# set up Earth and sun objects
#
Sun = sphere(pos=( 0 ,0 ,0), mass= 2e30,
              radius=7e8*10, color=color.orange)

Earth = sphere(pos=( r0_es ,0 ,0), mass= 6e24,
              radius=6.4e6*500, v=vector(0,3e4,0), color=color.blue,  make_trail=True)

ball = sphere(pos=(25 , 0 ,0), mass= 10, v=vector(0, 1, 0) ,
              radius=4, color=color.blue,  make_trail=True)

# set up more parameters

Earth.p=Earth.mass*Earth.v
g=9.8


# define the path of the Earth
path=curve(color=Earth.color)
path.append(pos=Earth.pos)


# set processing rate to 800
myrate=800
# start program
scene.mouse.getclick()
# print title
print ((' Turning around  '))
print ("  "  )

dott_radius = 4
g = 9.8
theta = 60*pi/180
speed = 50



#
# initialize ball momentum
#
ball.p = ball.mass*ball.v
#
# initialize time paramters
#
dt=24*60*60
t=0
tc = 0

#
# initialize graphical output
#
vxcurve = gcurve(gdisplay=graph_velocity, color=color.red)
vycurve = gcurve(gdisplay=graph_velocity, color=color.red)

#
# Place initial ball
#



#
# set start location ifor ball
#
initPosy = ball.pos.y
# print initial point
#rcenter = initPosy.x/2
print ("Initial Position = %.2f m "%(ball.pos.y))

##############################################
# process loop (action)   ####################
##############################################
while (t<365*24*60*60):
# creat while loop with condition run while y position is greater than
# or equal to starting_position
    # set rate
    rate(myrate)
    ##############################################
    # PHYSICS    >>>>>>             ##############
    ##############################################

    # use an if statement to create force vector
        #Force = vector()
        # calculate centripital (radial inward force) force on ball at other positions
    r=Earth.pos-Sun.pos
    centForce = (-(6.67e-11)* Earth.mass*(Sun.mass)/r0_es**2)


    FC = centForce*norm(r)
    print ("velocity"+str(Earth.v))
    print ("Position"+str(Earth.pos))
    print ("Momentum" + str(Earth.p))
    print ("FC" + str(FC))
    # MOMENTUM PRINCIPLE
    Earth.p += FC*dt
    # update ball velocity
    Earth.v = (Earth.p/Earth.mass)
    # update ball position
    Earth.pos += (Earth.v)*dt

    ##############################################
    # PHYSICS    <<<<<<<<<    ####################
    ##############################################
    # transfer ball x, y velocity to graphing paramters
    vx = Earth.p.x/ball.mass
    vy = Earth.p.y/ball.mass

    # plot velocity
    vxcurve.plot(pos=(t,vx))
    vycurve.plot(pos=(t,vy))
   # if ballvy_old*ball.v.y <=0 :
   #print("Max height is "+ str(ball.pos.y) +"m")
   # ballvy_old = ball.v.y
    # update time paramters
    t+=dt
    tc+=dt
    # periodically place ball on scene


    if tc>1.0:
        tc =0
        sphere(pos=Earth.pos, radius=dott_radius, color =color.red)
# print final position
#print(" time= %.1f s , distance = %.2f m "%(t,ball.pos.x-x0))
print ("  "  )

######### END OF PROGRAM ######################################
