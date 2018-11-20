#!/usr/bin/python
# coding:UTF-8
# make_angle.py
import csv
import math
import numpy as np

def change_coodinate(x,y,z,initTheta):
    "change coodinate"  # x[mm],y[mm],z[mm],initTheta[deg]
    initTheta = math.radians(initTheta)
    cx = (x * math.cos(initTheta)) + (y * math.sin(initTheta))
    cy = -(x * math.sin(initTheta)) + (y * math.cos(initTheta))
    cz = z
    return map(lambda n: round(n, 6),[cx,cy,cz])

def make_angle(x, y, z):
    "Calculation theta's deg"    # x[mm],y[mm],z[mm]
    length1 = 30    #[mm]
    length2 = 55    #[mm]
    length3 = 80    #[mm]

    pow_x = pow(x,2)
    pow_y = pow(y,2)
    pow_z = pow(z,2)

    alpha     = math.sqrt(pow_x+pow_y) - length1
    pow_alpha = pow(alpha,2)

    check_value = (
        pow(pow_alpha + pow_z + pow(length2,2)
        + pow(length3,2),2)
        - (2*( pow( pow_alpha + pow_z,2) + pow(length2,4) + pow(length3,4)))
    )

    if check_value > 0:
        k = math.sqrt(check_value)
    else:
        print 'errorrrrrrr'
        return None
    theta1 = math.atan2(y,x)
    theta2 = (
        math.atan2(z,alpha)
        + math.atan2(k, pow_alpha + pow_z + (length2*2) - (length3*2))
    )
    theta3 = -math.atan2(k, pow_alpha + pow_z - pow(length2,2) - pow(length3,2))
    if math.fabs(theta1) > math.radians(80): print 'error1'
    if math.fabs(theta2) > math.radians(90): print 'error2'
    if math.fabs(theta3) > math.radians(135): print 'error3'
    theta = map(lambda n: math.degrees(n), [theta1, -theta2, -theta3])
    return theta    #[deg]
def DataOut(group, Speed, Data, next=None):
    dataline = [group, Speed]
    dataline.extend(np.round(Data))
    if next == ('&' or '&\r'):
        dataline.extend('&')
    csvWrite.writerow(dataline)

if __name__ == "__main__":
    
