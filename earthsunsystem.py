# write code for libraries need by Vpython
from __future__ import division
from visual import *
from visual.graph import*

##
# Set up area on screen to display objects
##
scene = display(title='Sun - Earth System',x=100, y=10, width=1000, height=1000, background=color.white, range =5.e11)
#
# set up earth and sun objects
#
r0_es= 1.496e11
Sun = sphere(pos=( 0 ,0 ,0), mass= 0, radius=7e8*10, color=color.orange, v= vector(0,0,0))
Earth = sphere(pos=(r0_es ,0 ,0), mass= 0, radius=6.4e6*500, color=color.blue,  make_trail=True, v = vector(0,0,0))

                                  
# define the path of the Earth
path=curve(color=Earth.color)  
path.append(pos=Earth.pos)
#
# initialize earth and sun paramters 
#

Sun.mass = 2e30
Earth.mass = 6e24
Earth.v = vector(0,2.9e4,0) 
G = 6.67384e-11
Earth.p = Earth.mass*Earth.v
#
# set up graph output for energy plots
#
graph_energy = gdisplay(title='Energy',x=1200,y=200,xtitle='time(sec)',ytitle='Energy(Joule)',
                   foreground=color.black, background=color.white)

#
# initialize graphical output for energy plots
#
ke_curve  =gcurve(gdisplay=graph_energy, color=color.blue)
pe_curve  =gcurve(gdisplay=graph_energy, color=color.green)
kpe_curve =gcurve(gdisplay=graph_energy, color=color.red)
kpew_curve =gcurve(gdisplay=graph_energy, color=color.yellow)
work_curve =gcurve(gdisplay=graph_energy, color=color.black)


#
# set up graph output for angular momentum plots
#
graph_angMomemtum = gdisplay(title='Angular Momentum',x=1200,y=200,xtitle='time(sec)',ytitle='L',
                   foreground=color.black, background=color.white)

#
# initialize graphical output for angular momentum plots
#
amX  =gcurve(gdisplay=graph_angMomemtum, color=color.blue)
amY  =gcurve(gdisplay=graph_angMomemtum, color=color.green)
amZ =gcurve(gdisplay=graph_angMomemtum, color=color.red)
#
# set up graph output for velocity plots
#
graph_Velocity = gdisplay(title=' Velocity ',xtitle='time(sec)',ytitle='V(m/s)',
    x=80, y= 720, width=1000, background=color.white)
#
# initialize graphical output for velocity plots
#
vplotx = gcurve(gdisplay=graph_Velocity, color=color.magenta)
vploty = gcurve(gdisplay=graph_Velocity, color=color.green)

#
# initialize time parameter
#
dt =12*60*60 # one day
t = 0

earthvy_old = Earth.v.y
y_acc = (earthvy_old-Earth.v.y)/dt

# start program with mouse click
scene.mouse.getclick()
myrate = 1000
work = 0 
##############################################
# process loop (action)   ####################
##############################################
while t<(4*366*24*60*60):
    rate(myrate)
    ##############################################
    # PHYSICS    >>>>>>             ##############
    ##############################################
    # calculate force 
    r_vector = Earth.pos - Sun.pos  # Sun - Earth vector
    r = mag(r_vector)               # sqrt(r_vector.x**2 + r_vector.y**2 + r_vector.z**2 ) # distance
    rhat = r_vector/r               # unit vector
    F= (-G*Earth.mass*Sun.mass*rhat)/r**2 # Newton's gravitational force
    Earth.p += F*dt                # MOMENTUM PRINCIPLE
                                                # update momentum
    Earth.pos +=(Earth.p/Earth.mass)*dt # update position
    path.append(pos=Earth.pos)                  # draw a line
    Earth.v = (Earth.p/Earth.mass)            # update velocity
    # calculate energy
    KE = .5*Earth.mass*mag(Earth.v)**2# kinetic energy
    PE = (-G*Earth.mass*Sun.mass)/r # potential energy
    # calculate angular momentum
    angMomentum = cross(Earth.pos,Earth.p)
    
    #period = (2*pi)/w

    # calculate velocity
    vx = Earth.p.x/Earth.mass
    vy = Earth.p.y/Earth.mass

    # calculate work
    dx=Earth.v*dt
    work += dot(F,dx)
    ##############################################
    # PHYSICS    <<<<<<<<<    ####################
    ##############################################
    # plot energy
    ke_curve.plot(pos=(t,KE))
    pe_curve.plot(pos=(t,PE))
    kpe_curve.plot(pos=(t,KE+PE))
    kpew_curve.plot(pos=(t,KE+PE-work))
    work_curve.plot(pos=(t,work))
    # plot velocity
    vplotx.plot(pos=(t,vx))
    vploty.plot(pos=(t,vy))
    
    # plot angular momentum
    amX.plot(pos=(t,angMomentum.x))
    amY.plot(pos=(t,angMomentum.y))
    amZ.plot(pos=(t,angMomentum.z))
    # update time
    t+=dt

    earthvy_old = Earth.v.y

             

    
    
