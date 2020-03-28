import numpy as np
import time
import cv2 as cv
# Create a black image
img = np.zeros((650, 1200, 3), np.uint8)
start = 250
end = 400
rect_itirate = np.arange(start,end,2)
font = cv.FONT_HERSHEY_SIMPLEX
cv.rectangle(img, (start, start), (end, end), (0, 255, 0), 2)   # the reaction chamber outline (pressure)
cv.rectangle(img, (450, 250), (500, 300), (0, 255, 0), 2)   # the reaction chamber outline  (heater)
cv.rectangle(img, (250, 450), (270, 470), (0, 255, 0), 2)   # the nitrogen valve representation
cv.rectangle(img, (300, 450), (320, 470), (0, 255, 0), 2)   # the precursor1 valve representation
cv.rectangle(img, (350, 450), (370, 470), (0, 255, 0), 2)   # the precursor2 valve representation
cv.rectangle(img, (400, 450), (420, 470), (0, 255, 0), 2)   # the vent valve representation
# text, location, fontformat, fontsize, color, thickness, linetype
valves_txt = 'Valves: Nitrogen Precursor1 Precursor2 Vent'
frame1 = cv.putText(img, valves_txt, (206, 490), font, 0.3, (255, 0, 0), 1, cv.LINE_AA)     # valves text on the image
frame2 = cv.putText(img, 'Reaction Chamber', (252, 240), font,0.6, (255, 0, 0), 1, cv.LINE_AA)
frame3 = cv.putText(img, 'Heater', (450, 240), font, 0.6, (255, 0, 0), 1, cv.LINE_AA)
cv.imshow('test', frame1)
cv.imshow('test', frame2)
cv.imshow('test', frame3)

# this part is to simulate the variation in pressure and temperature
# assuming that ambient temperature = 24, and heating capacity of heater is upto 300
temp_ = np.arange(24, 300, 1)
T_time_ = 100    # adjust the heater speed
# the pressure in the chamber decrease from 1 bar to the maximum of 0.01 / (start,stop,step)
pres_ = np.arange(1, 0.01, -0.01)
P_time_ = 200   # adust the vacuum pump speed
temp_limit = 150
pres_limit_down = 0.1
GV_GT03 = 0 # the valve of the nitrogen tank normally closed (0) turn to open (1) when activated
GV_GT02 = 0 # the valve of Al2(CH3)6 (precursor 1) tank normally closed (0) turn to open (1) when activated
GV_GT01 = 0 # the valve of the H2O (precursor 2)tank normally closed (0) turn to open (1) when activated
GV01 = 0  # the vent valve for extuding the secondary products

GT02_time = 3000  # time of activation for valve of Al2(CH3)6 (precursor 1)
GT01_time = 1000  # time of activation for valve of H2O (precursor 1)


def heater_activation(temp, T_time, TEMP_lim):
    global GV01, GV_GT01, GV_GT02, GV_GT03
    for T in temp:
        cv.rectangle(img, (450, 250), (500, 300), (0, 0, 255), -1)
        cv.imshow('test', img)
        cv.waitKey(T_time)

        # time.sleep(T_time)
        print('Chamber temperature', T, '\n all valves condition(vent,precursor2,precursor1,nitrogen): ',
              GV01, GV_GT01, GV_GT02, GV_GT03)
        if T == TEMP_lim:
            break
    return T


def pump_activation(pres, p_time, limitDn):
    global GV01, GV_GT01, GV_GT02, GV_GT03, start, end, rect_itirate
    for P, i in zip(pres, rect_itirate):
        ##*****the part for simulation
        cv.rectangle(img, (start, start), (i, end), (0, 0, 255), -1)
        cv.imshow('test', img)
        cv.waitKey(p_time)
        #****************************
        PP = round(P, 2)
        print('Chamber pressure', PP, '\n all valves condition(vent,precursor2,precursor1,nitrogen): ',
              GV01, GV_GT01, GV_GT02, GV_GT03)
        if limitDn >= PP:
            break
    return PP


inpt = int(input('initiate process by entering 1: '))
if inpt == 1:
    print('process is activated')
    ultimate_pressure = pump_activation(pres_, P_time_, pres_limit_down)
    GV_GT03 = 1
    print('nitrogen valve: opened', GV_GT03)
    cv.rectangle(img, (250, 450), (270, 470), (0, 0, 255), -1)
    cv.imshow('test', img)

    ultimate_temperature = heater_activation(temp_, T_time_, temp_limit)
    print('these are the final values for the temperature and presure',
          ultimate_temperature, ultimate_pressure)
    for i in range(6):
        GV_GT02 = 1     # valve opened
        print('precursor 1 valve: opened', GV_GT02)
        cv.rectangle(img, (300, 450), (320, 470), (0, 0, 255), -1)
        cv.imshow('test', img)
        cv.waitKey(GT02_time)

        GV_GT02 = 0     # Valve closed
        print('precursor 1 valve: closed', GV_GT02)
        cv.rectangle(img, (300, 450), (320, 470), (0, 0, 0), -1)
        cv.imshow('test', img)

        GV_GT01 = 1     # Valve opened
        print('precursor 2 valve: opened', GV_GT01)
        cv.rectangle(img, (350, 450), (370, 470), (0, 0, 255), -1)
        cv.imshow('test', img)
        cv.waitKey(GT01_time)
        GV_GT01 = 0     # Valve closed
        print('precursor 2 valve: closed', GV_GT02)
        cv.rectangle(img, (350, 450), (370, 470), (0, 0, 0), -1)
        cv.imshow('test', img)
    GV_GT01 = 0
    cv.rectangle(img, (350, 450), (370, 470), (0, 0, 0), -1)
    GV01 = 1    # vent valve opened
    print('Vent Valve: opened', GV01)
    cv.rectangle(img, (400, 450), (420, 470), (0, 0, 255), -1)
    GV_GT03 = 0     # close nitrogen valve
    cv.rectangle(img, (250, 450), (270, 470), (0, 0, 0), -1)
    cv.imshow('test', img)

    print('all valves condition(vent, precursor2, precursor1, nitrogen): ',
          GV01, GV_GT01, GV_GT02, GV_GT03)
    #  .........For loop is just to simulate the effect of opening vent valve
    pres_down = np.arange(ultimate_pressure, 1, 0.01)
    for press, ii in zip(pres_down, rect_itirate):
        ##*****the part for simulation
        cv.rectangle(img, (start, start), (ii, end), (0, 0, 0), -1)
        cv.imshow('test', img)
        cv.waitKey(P_time_)
        #****************************
        press_ = round(press, 2)
        print('Chamber pressure', press_)
    #  .........For loop is just to simulate the effect of opening vent valve
    # deactivate all
    cv.rectangle(img, (450, 250), (500, 300), (0, 0, 0), -1)   # heater deactivation
    GV01 = 0
    cv.rectangle(img, (400, 450), (420, 470), (0, 0, 0), -1)
    cv.imshow('test', img)
    print('all valves condition(vent, precursor2, precursor1, nitrogen): ',
          GV01, GV_GT01, GV_GT02, GV_GT03)
    cv.waitKey(0)
    cv.destroyAllWindows
