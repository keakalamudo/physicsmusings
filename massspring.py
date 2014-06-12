#Mass and Spring Simulation(Gravity + Air Resistance + Wind) (VPython Source)
from visual import *
from visual.graph import *


#Set up area on screen to display objects
scene = display(title='Spring',x=80, y=10, width=1000, height=300,background=color.white, userspin = True)

#Set up base
ground = box(length =10, width = 10, height=0.01, pos=(0,-0.25,0),color=color.green)

#Graph Output
graph_spring_x = gdisplay(title=' Position x ',xtitle='time(sec)',ytitle='m',x=80, y= 320, width=1000, background=color.white)
graph_spring_v = gdisplay(title=' Velocity_x  ',xtitle='time(sec)',ytitle='V(m/s)', x=80, y= 720, width=1000, background=color.white)

#Graphical output intializations
posplot = gcurve(gdisplay=graph_spring_x, color=color.red)
vplot = gcurve(gdisplay=graph_spring_v, color=color.magenta)

# y(Weight Displacemrnt)
y = 2.5

#Set up block object (shows horizontal motion of spring-block system)
block = box(length =0.5, width = 0.5, height=0.5, pos=(y,0,0), color=color.blue, v=vector(0,0,0))

#Initialize parameters
m = 0.04
k = 1.4
l = 2
dl =0.5
g = 9.8
cc =30
rho = 0.005
block.p = m*block.v

#Time parameters
dt=.01
t=0
tc = 0

#Start Program

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
    yx = block.pos.x
    yy = block.pos.y
    yz = block.pos.z
    FS = vector(-k*(yx-l),-ky*(yy-l),-kz*(yz-l))
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
