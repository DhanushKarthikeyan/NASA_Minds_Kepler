
from math import acos, degrees

#x_val = [100.31857813547957, 100.3185781354796, 148.4863727821475, 148.4863727821475, 301.5258215962442]
#y_val = [99.81708432412658, 198.59154929577466, 149.20431680995063, 249.80793854033288, 99.2073654045485]

'''x_val = [1,2,1,3]
y_val = [1,2,3,1]'''

def dist(x,y,x2,y2):
    return (((x2-x)**2) + ((y2-y)**2))**(1/2)


def convert_mecanum_polar(x_val, y_val):
    RAoutput = [] # populate your calculations here
    for i in range(len(x_val)-1):
        x = round(x_val[i])
        y = round(y_val[i])
        x_2 = round(x_val[i+1])
        y_2 = round(y_val[i+1])
        r = dist(x,y,x_2,y_2)
        if x_2 == x:
            if y_2 > y:
                a = 90
            else:
                a = 270
        elif x_2 > x:
            if y_2 > y:
                a = degrees(acos(abs(x_2 - x)/r))
            else:
                a = 360 - degrees(acos(abs(x_2 - x)/r))
        else:
            if y_2 > y:
                a = 180 - degrees(acos(abs(x - x_2)/r))
            else:
                a = 270 - degrees(acos(abs(x - x_2)/r))
        RAoutput.append((round(r, 2), round(a)))
    return RAoutput

