# write code for libraries need by Vpython
from __future__ import division
from visual import *
from visual.graph import*

##
# Set up area on screen to display objects
##
scene = display(title='Sun - Earth System',x=100, y=10, width=1000, height=1000, background=color.white, userspin = True, range =5.e11)

#
# set up earth and sun objects
r0_es= 1.496e11
Sun = sphere(pos=( 0 ,0 ,0), mass= 2e30, radius=7e8*10, color=color.orange, v= vector(0,0,0))
Earth = sphere(pos=(r0_es ,0 ,0), mass= 6e24, radius=6.4e6*500, color=color.blue,  make_trail=True, v = vector(2e4,0,0))


# define the path of the Earth
path=curve(color=Earth.color)  
path.append(pos=Earth.pos)
#
# initialize earth and sun paramters 
#
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
#
# set up graph output for angular momentum plots
#

#
# initialize graphical output for angular momentum plots
#

#
# set up graph output for velocity plots
#
graph_velocity = gdisplay(title='Velocity ( v_x - red, v_y - blue, v_z – green)' ,x=1200,y=200,xtitle='time(sec)',ytitle='V(m/s)',
foreground=color.black, background=color.white)

#
# initialize graphical output for velocity plots
#

#
# initialize time parameter
#
dt =3600 # one day
t = 0
tc = 0

# start program with mouse click
dott_radius = 4

##############################################
# process loop (action)   ####################
##############################################
while t<(2*366*10*24*60*60):
                  # plot for two years
                   # shows 100 points in a second
    rate(2400)
    ##############################################
    # PHYSICS    >>>>>>             ##############
    ##############################################
    # calculate force 
    r_vector = Earth.pos - Sun.pos           # Sun - Earth vector
    centForce = (-(6.67e-11)* Earth.mass*(Sun.mass)/r0_es**2)
    FC = centForce*norm(r_vector)

     # MOMENTUM PRINCIPLE
    Earth.p += FC*dt
    # update ball velocity
    Earth.v = (Earth.p/Earth.mass)
    # update ball position
    Earth.pos += (Earth.v)*dt
    # calculate angular momentum

    ##############################################
    # PHYSICS    <<<<<<<<<    ####################
    ##############################################
    # plot energy
    #kpe= ke+ pe #kinetic + potential energy
    #ke_curve.plot(pos=(t,ke))
    #pe_curve.plot(pos=(t,pe))
    #pe_curve.plot(pos=(t,kpe))
    # plot velocity
    
    # plot angular momentum
 
    # update time
    t+=dt
    tc+=dt            

    
    if tc>1.0:
        tc =0
        sphere(pos=Earth.pos, radius=dott_radius, color =color.red)
# print final position
#print(" time= %.1f s , distance = %.2f m "%(t,ball.pos.x-x0))
print ("  "  )
