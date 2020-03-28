import _thread
import numpy as np
import time
# import cv2 as cv
# this part is to simulate the variation in pressure and temperature
temp_ = np.arange(24,300,1)   # assuming that ambient temperature = 24, and heating capacity of heater is upto 300
T_time_ = 0.1    # adjust the heater speed
pres_ = np.arange(1,0.01,-0.01) # the pressure in the chamber decrease from 1 bar to the maximum of 0.01 / (start,stop,step)
P_time_ = 0.1   # adust the vacuum pump speed
temp_limit= 150
# pres_limit_up = 0.11
pres_limit_down = 0.1
GV_GT03 = 0 # the valve of the nitrogen tank normally closed (0) turn to open (1) when activated
GV_GT02 = 0 # the valve of Al2(CH3)6 (precursor 1) tank normally closed (0) turn to open (1) when activated
GV_GT01 = 0 # the valve of the H2O (precursor 2)tank normally closed (0) turn to open (1) when activated
GV01 = 0 # the vent valve for extuding the secondary products

GT02_time = 1  # time of activation for valve of Al2(CH3)6 (precursor 1)
GT01_time = 1  # time of activation for valve of H2O (precursor 1)
def heater_activation(temp, T_time, TEMP_lim):
    global GV01, GV_GT01, GV_GT02, GV_GT03
    for T in temp:
        time.sleep(T_time)
        print('Chamber temperature', T, '\n all valves condition(vent,precursor2,precursor1,nitrogen): ', GV01, GV_GT01, GV_GT02, GV_GT03)
        if T == TEMP_lim:
            break
    return T
def pump_activation(pres, p_time, limitDn):
    global GV01, GV_GT01, GV_GT02, GV_GT03
    for P in pres:
        PP = round(P, 2)
        time.sleep(p_time)
        print('Chamber pressure', PP, '\n all valves condition(vent,precursor2,precursor1,nitrogen): ', GV01, GV_GT01, GV_GT02, GV_GT03)
        if limitDn >= PP:
            break
    return PP
inpt = int(input('initiate process by entering 1: '))
if inpt == 1:
    print('process is activated')
    ultimate_pressure = pump_activation(pres_, P_time_, pres_limit_down)
    GV_GT03 = 1
    print('nitrogen valve: opened', GV_GT03)
    ultimate_temperature = heater_activation(temp_, T_time_, temp_limit)
    print('these are the final values for the temperature and presure', ultimate_temperature, ultimate_pressure)
    for i in range(6):
        GV_GT02 = 1     # valve opened
        print('precursor 1 valve: opened', GV_GT02)
        time.sleep(GT02_time)
        GV_GT02 = 0     # Valve closed
        print('precursor 1 valve: closed', GV_GT02)
        GV_GT01 = 1     # Valve opened
        print('precursor 2 valve: opened', GV_GT01)
        time.sleep(GT01_time)
        GV_GT01 = 0     # Valve closed
        print('precursor 2 valve: closed', GV_GT02)
    GV01 = 1
    print('Vent Valve: opened', GV01)
    GV_GT03 = 0     # close nitrogen valve
    print('all valves condition(vent, precursor2, precursor1, nitrogen): ', GV01, GV_GT01, GV_GT02, GV_GT03)
    #  .........For loop is just to simulate the effect of opening vent valve 
    pres_down = np.arange(ultimate_pressure, 1, 0.01)
    for press in pres_down:
        press_ = round(press, 2)
        time.sleep(P_time_)
        print('Chamber pressure', press_)
    #  .........For loop is just to simulate the effect of opening vent valve
    # deactivate all
    GV_GT02 = 0
    GV_GT01 = 0
    GV01 = 0
    print('all valves condition(vent, precursor2, precursor1, nitrogen): ', GV01, GV_GT01, GV_GT02, GV_GT03)
