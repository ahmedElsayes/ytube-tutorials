# ahmed.elsayes@student.tut.fi
from  __future__ import print_function # use python 3 syntax but make it compatible with python 2
from  __future__ import division       #                           ''

import time     # import the time library for the sleep function
import brickpi3 # import the BrickPi3 drivers

qw = brickpi3.BrickPi3() # Create an instance of the BrickPi3 class. BP will be the BrickPi3 object.
####
qw.offset_motor_encoder(qw.PORT_A, qw.get_motor_encoder(qw.PORT_A)) # reset encoder A
qw.offset_motor_encoder(qw.PORT_B, qw.get_motor_encoder(qw.PORT_B))
qw.offset_motor_encoder(qw.PORT_C, qw.get_motor_encoder(qw.PORT_C)) # reset encoder A
qw.offset_motor_encoder(qw.PORT_D, qw.get_motor_encoder(qw.PORT_D))

qw.set_sensor_type(qw.PORT_2, qw.SENSOR_TYPE.NXT_LIGHT_ON) # setting port 2 to lightsesor
qw.set_motor_power(qw.PORT_A,qw.MOTOR_FLOAT)#setting float power 
qw.set_motor_power(qw.PORT_B,qw.MOTOR_FLOAT)
qw.set_motor_power(qw.PORT_C,qw.MOTOR_FLOAT)
qw.set_motor_power(qw.PORT_D,qw.MOTOR_FLOAT)
####################################################
qw.set_motor_limits(qw.PORT_A,20,100)#setting float power limits
qw.set_motor_limits(qw.PORT_B,25,100)
qw.set_motor_limits(qw.PORT_C,35,100)
qw.set_motor_limits(qw.PORT_D,45,100)
##################################################
##################################################
a=[0,115]# the gripper reference, close position
b=[0,250,-350]# the base reference (first, second object, third)##
b_modified=[250,0,-350]## the base reference in case of wrong object detected(first, second object, third)##
c=[0,124, 105, 95]#the link reference, the picking position,(other values determine later for objiects 2&3 position) 
d=[0,90,-90]#the linear translation reference, moving backward, moving forward
targetb=[525,420,370] #for modifing the base motor position in iterative way to set the target in write position
targetd=[20,133,180] #for modifing the linear movement motor position in iterative way to set the target in write position
vari=0
varx=1
vary=0 # variable used for transfer for another loop in case of wrong detection of the targeted object
vark=0
varh=0

#### ########function loop of gripping#############
def gripping():
    qw.set_motor_position(qw.PORT_A,a[1]) #picking up the object
    time.sleep(5)
    qw.set_motor_position(qw.PORT_C,c[0])# energize link toward reference position
    time.sleep(5)
    ################################################
    qw.set_motor_position(qw.PORT_D,targetd[varh])###going linearly backward for the target position
    time.sleep(5)
    qw.set_motor_position(qw.PORT_B,targetb[vark]) #going by base for target position
    time.sleep(11)
    #############################
    qw.set_motor_position(qw.PORT_C,c[varx])# energize link toward target position
    time.sleep(5)
    #########   value of x should be setted later
   
    ####################################
    qw.set_motor_position(qw.PORT_A,a[0]) # realising the object
    time.sleep(5)
    ############this space for energizing motor D backward##
    qw.set_motor_position(qw.PORT_D,d[1])###1 pos
    time.sleep(5)
    ########################################################
    qw.set_motor_position(qw.PORT_C,c[0])    # moving link up
    time.sleep(5)
#### the end of gripping function#############

try:        
    for vari in range(0,3):
        while (vari==0 or vari==2) and vary==0:#During first or the third iteration
            qw.set_motor_position(qw.PORT_B,b[vari])#### i will be incremented for 4 positions##
            time.sleep(5)
            qw.set_motor_position(qw.PORT_C,c[1])# energize link toward position 1
            time.sleep(5)
            qw.set_motor_position(qw.PORT_D,d[2])## moving the robot forward
            color=qw.get_sensor(qw.PORT_2)  #to get the value recorded in sensor
            time.sleep(5)
            if color>2300:# is the object black??
                v=gripping()  ##functioning gripping loop
                vari=vari+1
                time.sleep(.1)
                varx=varx+1
                time.sleep(.1)
                vark=vark+1
                time.sleep(.1)
                varh=varh+1
                time.sleep(.1)
            else:
                qw.set_motor_position(qw.PORT_D,d[1])## moving the robot backward
                time.sleep(5)
                qw.set_motor_position(qw.PORT_C,c[0])
                time.sleep(5)
                vary=vary+1
                time.sleep(.1)
  #######################Second picking up######################################
        while vari==1 and vary==0:#During the second iteration
            qw.set_motor_position(qw.PORT_B,b[vari])#### i will be incremented for 4 positions##
            time.sleep(5)
            qw.set_motor_position(qw.PORT_C,c[1])# energize link toward position 1
            time.sleep(5)
            qw.set_motor_position(qw.PORT_D,d[2])## moving linear in forward##2 pos
            color=qw.get_sensor(qw.PORT_2)  #to get the value recorded in sensor
            time.sleep(5)
            if color<2300:# is the object white??
                v=gripping()  ##functioning gripping loop
                vari=vari+1
                time.sleep(.1)
                varx=varx+1
                time.sleep(.1)
                vark=vark+1
                time.sleep(.1)
                varh=varh+1
                time.sleep(.1)
            else:
                qw.set_motor_position(qw.PORT_D,d[1])## moving the robot backward
                time.sleep(5)
                qw.set_motor_position(qw.PORT_C,c[0])
                time.sleep(5)
                vari=vari+1
                time.sleep(.1)
                vary=vary+1
                time.sleep(.1)
#####################################################################
###this loop only when the it miss the right object in the first or the second iteration##
        while vari in range(0,3) and vary==1:
            qw.set_motor_position(qw.PORT_B,b_modified[vari])#### i will be incremented for 4 positions##
            time.sleep(5)
            qw.set_motor_position(qw.PORT_C,c[1])# energize link toward position 1
            qw.set_motor_position(qw.PORT_D,d[2])## moving linear in forward##2
            time.sleep(5)
            v=gripping()  ##functioning gripping loop
            vari=vari+1
            time.sleep(.1)
            varx=varx+1
            time.sleep(.1)
            vark=vark+1
            time.sleep(.1)
            varh=varh+1
            time.sleep(.1)
    else:
        qw.set_motor_position(qw.PORT_B,b[0])
        time.sleep(5)
        qw.reset_all()
        time.sleep(2)
except KeyboardInterrupt: # except the program gets interrupted by Ctrl+C on the keyboard.
    qw.reset_all()        # Unconfigure the sensors, disable the motors, and restore the LED to the control of the BrickPi3 firmware.
