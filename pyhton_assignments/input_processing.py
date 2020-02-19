

## part (a)
study_benefit = float(input("Enter the amount of the study benefits: "))
indx = 1.17
gain = (1.17/100)
val = (gain * study_benefit) + study_benefit

## part(b)

gain2 = val * gain
val2 = gain2 + val

print("If the index raise is", indx,"percent, the study benefit,\nafter a raise, would be", val, "euros")

print("and if there was another index raise, the study\nbenefits would be as much as",val2,"euros")

