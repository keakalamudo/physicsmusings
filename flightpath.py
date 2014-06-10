from visual import *
from visual.graph import *

##
# Set up area on screen to display objects
##
scene = display(title='Spring',
    x=80, y=10, width=1000, height=300,
    background=color.white)
#
# set up base to display objects on the scene
#
ground = box(length =10, width = 10, height=0.01, pos=(0,-0.25,0),
             color=color.green)
#
# set up graph output
#
graph_spring_x = gdisplay(title=' Position x ',xtitle='time(sec)',ytitle='m',
    x=80, y= 320, width=1000, background=color.white)
graph_spring_v = gdisplay(title=' Velocity_x  ',xtitle='time(sec)',ytitle='V(m/s)',
    x=80, y= 720, width=1000, background=color.white)
#
# initialize graphical output
#
posplot = gcurve(gdisplay=graph_spring_x, color=color.red)
vplot = gcurve(gdisplay=graph_spring_v, color=color.magenta)

# initialize y Set to 0.5
y = 2.5
#
# set up block object (shows horizontal motion of spring-block system)
#
block = box(length =0.5, width = 0.5, height=0.5, pos=(y,0,0), color=color.blue, v=vector(0,0,0))
#
# initialize parameters
#
m = 0.04
k = 1.4
l = 2
dl =0.5
g = 9.8
cc =30
rho = 0.005
block.p = m*block.v
#
# initialize time parameters
#
dt=.01
t=0
tc = 0

#
# start program with a mouse click
#
scene.mouse.getclick()
# set processing rate
myrate = 1000
# print title
print (" Spring force + quadratic air drag ")
w = sqrt(k/m)
period = (2*pi)/w
bx_old = block.pos.x
t1=0
##############################################
# process loop (action)   ####################
##############################################
while (t < 8):
    rate(myrate)
    ##############################################
    # PHYSICS    >>>>>>             ##############
    ##############################################
    # calculate spring force
    y = block.pos.x
    FS = vector(-k*(y-l),0,0)
    #print(FS)
    # if damped oscillator - calculate air resistance
    fair = -0.5*cc*rho*(block.width**2) * (mag(block.v)**2) * norm(block.v)
    # calculate total force on block
    FT=FS+fair
    # MOMENTUM PRINCIPLE
    block.p += FT*dt
    # update block velocity
    block.v = (block.p/m)
    # update block position
    block.pos +=(block.p/m)*dt
    y = block.pos.x
    ##############################################
    # PHYSICS    <<<<<<<<<    ####################
    ##############################################
    # update time paramters
    t+=dt
    tc+=dt
    # plot position and velocity
    pos = block.p.x/m
    velo = block.v.x/m

    posplot.plot(pos=(t,pos))
    vplot.plot(pos=(t,velo))


    # Find Period and Calculate period; print them out
    # Try and find your own method, I will help you out if you
    # are struggling.
    #print(block.pos)
    if ((bx_old < 2) and (block.pos.x > 2)) :
        print(" t = %.4f " %(t))

        if t1 > 0 :
                T = (t - t1)
                print (" T_comp = %.3f     T_exact = %.3f   " %(T,period ))
    # update time paramters
        t1 = t
    # update position paramter to find period
    bx_old = block.pos.x

######### END OF PROGRAM #######################################
