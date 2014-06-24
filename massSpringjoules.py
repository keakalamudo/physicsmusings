from visual import *
from visual.graph import *

##
# Set up area on screen to display objects
##
scene = display(title='Spring',
    x=80, y=10, width=1000, height=300,
    background=color.white, userspin = True)
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
graph_energy = gdisplay(title='Energy',x=1200,y=200,xtitle='time(sec)',ytitle='Energy(Joule)',
                   foreground=color.black, background=color.white)
graph_work = gdisplay(title='Work',x=1200,y=200,xtitle='time(sec)',ytitle='Work(Joule)',
                   foreground=color.black, background=color.white)
                   
