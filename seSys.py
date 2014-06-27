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
#

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
Earth.v = vector(2e4,0,0) 
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
graph_angMomemtum = gdisplay(title='Angular Momentum',x=1200,y=200,xtitle='time(sec)',ytitle='Energy(Joule)',
                   foreground=color.black, background=color.white)

#
# initialize graphical output for angular momentum plots
#

#
# set up graph output for velocity plots
#


#
# initialize graphical output for velocity plots
#

#
# initialize time parameter
#
 # one day

# start program with mouse click

##############################################
# process loop (action)   ####################
##############################################

                  # plot for two years
                   # shows 100 points in a second
 
    ##############################################
    # PHYSICS    >>>>>>             ##############
    ##############################################
    # calculate force 
                                                # Sun - Earth vector
                                                # sqrt(r_vector.x**2 + r_vector.y**2 + r_vector.z**2 ) # distance
                                                # t vector
                                                # Newton's gravitational force
                                                # MOMENTUM PRINCIPLE
                                                # update momentum
     # update position
                      # draw a line
                # update velocity
    # calculate energy 
                                              # kinetic energy
                                              # potential energy
    # calculate angular momentum

    ##############################################
    # PHYSICS    <<<<<<<<<    ####################
    ##############################################
    # plot energy

    # plot velocity
    
    # plot angular momentum
 
    # update time
             

    
    
