from visual import *

# Static display of E field around a + or - charge or a di-pole
# Area set up on screen display to display objects
disp = display(x=0,y=0,height=800,width=1024,background=color.white,
            title='Electric field')
epsilon = 9e9
scale = 2e-20
#scale = 0.1e-19

# location in natural units
R = 0.5e-9
# list of ordered objects
E_field =[]
# set up field display arrows oriented around the charge
# arrange creates an array of numbers
for r1 in arange(R , 1.6*R, R/2):
    for theta in arange(0, 1.1*pi, pi/4):
        for phi in arange( 0, 2.1*pi, pi/4):
            # create an arrow
            b = arrow(pos=(r1*sin(theta)*cos(phi), r1*sin(theta)*sin(phi), r1*cos(theta)),
                      color=color.green,fixedwidth = True, shaftwidth = 0.000000000005, axis=(0,0,0) )
            # put an arrow representing the E field in the ordered list
            E_field.append(b)

s = 0.2e-9
#Positive charge
q1 = sphere(pos=(s/2,0,0), charge= 1.6e-19, radius=s/10, color=color.blue)
#Negative charge 
q2 = sphere(pos=(-s/2,0,0), charge= -1.6e-19, radius=s/10, color=color.red)
# The for loop iterates over the items of the ordered list E_field
for E in E_field:
##### PUT PHYSICS HERE #####################   
    # calculate E field for positive particle
        r_vector = E.pos - q1.pos
        r = mag(r_vector)
        rhat = r_vector/r
        E_net1 =  ((q1.charge*epsilon)/(r**2))*rhat
    # calculate E field for negative charged particle
        r_vector = E.pos - q2.pos
        r = mag(r_vector)
        rhat = r_vector/r
        E_net2 = ((q2.charge*epsilon)/(r**2))*rhat
###   calculate  for dipole 
        E_net = E_net1 + E_net2
##### PUT PHYSICS HERE #####################
        #Scale factor
        #E.axis = scale * E_net1
        #E.axis = scale * E_net2
        E.axis = scale * E_net
