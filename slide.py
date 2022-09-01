from math import degrees, hypot, sqrt, atan

a = input("Enter the rise of the slide's ladder: ")
b = input("Enter the run of the slide's ladder: ")

rise = int(a)
run = int(b)

sidea = rise * rise
sideb = run * run
slide = int(sqrt(sidea + sideb))
#slide = int(hypot(rise, run))
angle = int(degrees(atan(rise/run)))

slidesafe = False

if angle > 40:
    slidesafe = False
elif rise > 6:
    slidesafe = False
else:
    slidesafe = True

if slidesafe == True:
    print("Safe! The angle is: " + str(angle) + " degrees and your slide length is: " + str(slide))
else:
    print("Unsafe! The angle is: " + str(angle) + " degrees and your slide length is: " + str(slide))
