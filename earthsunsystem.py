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
Sun = sphere(pos=( 0 ,0 ,0), mass= 2e30, radius=7e8*10, color=color.orange)
r0_es = 1.496e11
Earth = sphere(pos=( r0_es ,0 ,0), mass= 6e24, radius=6.4e6*500, color=color.blue,  make_trail=True velocity =)


# define the path of the Earth
path=curve(color=Earth.color)  
path.append(pos=Earth.pos)
#
# initialize earth and sun paramters 
#
                   # mass of the Earth
                    # mass of the Sun 

                      # initial velocity
                    # gravitational constant
                      # Earth initial momentum

#
# set up graph output for energy plots
#

#
# initialize graphical output for energy plots
#


#
# set up graph output for angular momentum plots
#


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
             

    
    
