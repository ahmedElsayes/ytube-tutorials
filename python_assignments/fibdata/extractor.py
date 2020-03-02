
# the function takes the value from the tool "A" and gives a TRUE signal "signal" when break in interface occure
def extractor(A):

    import numpy as np
    import time
    from difference import *
    trigger = True
    signal = False

    # A is the value that recorded form the tool and change in a speed driven by the sampling frequency
    force_values = []
    count = 1
    force_indx = 0
    min_derivative = []
    threshold = -20
    # trigger = 0
    subdivision = 300
    while trigger:
        time.sleep(0.005)   # this delay is introduced within the while loop to update the Value of "A" every 5 millisecond
        # where "A" here represent every value recorded from the robotic instrument
        force_values.append(A)
        if len(force_values) == (count*subdivision):
            # time = [*range(0, count, count/len(force_values))]
            tim = np.linspace(0, count, num=len(force_values))
            # time.remove(time[-1])

            # Taking the first derivative to the newly acquired 500 dataset
            diff_force = subtractor(force_values)
            diff_time = subtractor(tim)
            diff1 = np.divide(diff_force, diff_time)
            minimum_value = np.amin(diff1) # return the minimum value of "diff1" that correspond to maximum drop in force measurement
            # max_indx = np.argmin(diff1)     # return the index of the previous value
            min_derivative.append(minimum_value)
            count = count+1
            force_indx = force_indx+1
        else:
            continue
        while len(min_derivative) >= 2:
            derivative_monitor = min_derivative[force_indx-1] - min_derivative[force_indx-2]
            min_derivative = []
            if derivative_monitor > threshold:
                break
            else:
              print('the break in interface is occured!')
              signal = True
              trigger = False

    return signal
        
