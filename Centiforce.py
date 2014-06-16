from __future__ import division
from visual import *
from visual.graph import *
##
# Set up area on screen to display objects
##
scene = display(title=' Turning around on a circle ',
     x=100, y=10, width=800, height=800,  range=400,  background=color.white)
scene.userzoom = True
#
# set up graph output
#
graph_velocity = gdisplay(title='Velocity',x=1200,y=200,xtitle='time(sec)',ytitle='V(m/s)',
                   foreground=color.black, background=color.white)
#
# set up bsll object
#
ball = sphere(pos=(25 , -100 ,0), mass= 10, v=vector(0, 1, 0) ,
              radius=4, color=color.blue,  make_trail=True)
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
dt=.01
t=0
tc = 10

#
# initialize graphical output
#
vxcurve = gcurve(gdisplay=graph_velocity, color=color.red)
vycurve = gcurve(gdisplay=graph_velocity, color=color.magenta)

#
# Place initial ball
#

sphere(pos=ball.pos, radius=dott_radius, color=color.red)

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
while (initPosy<=ball.pos.y):
# creat while loop with condition run while y position is greater than
# or equal to starting_position
    # set rate
    rate(myrate)
    ##############################################
    # PHYSICS    >>>>>>             ##############
    ##############################################
    if (ball.pos.y >= 0):
    # use an if statement to create force vector
        #Force = vector()
        # calculate centripital (radial inward force) force on ball at other positions

        centForce = (-ball.mass*(mag(ball.v)**2)/25)
        pythagorean = ((ball.pos.x**2)+(ball.pos.y**2))**(1/2)
        posx = ball.pos.x/pythagorean
        posy = ball.pos.y/pythagorean
        FC = vector(centForce*posx,centForce*posy,0)
    else :
        FC = vector (0,0,0)

    # MOMENTUM PRINCIPLE
    ball.p += FC*dt
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
    vxcurve.plot(pos=(t,vx))
    vycurve.plot(pos=(t,vy))
   # if ballvy_old*ball.v.y <=0 :
 #       print("Max height is "+ str(ball.pos.y) +"m")
   # ballvy_old = ball.v.y
    # update time paramters
    t+=dt
    tc+=dt
    # periodically place ball on scene


    if tc>1.0:
        tc =0
        sphere(pos=ball.pos, radius=dott_radius, color =color.red)
# print final position
#print(" time= %.1f s , distance = %.2f m "%(t,ball.pos.x-x0))
print ("  "  )

######### END OF PROGRAM #######################################
