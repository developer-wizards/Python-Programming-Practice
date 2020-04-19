'''
find the area under a curve sin(x)/x in the interval [-10, 10]
'''

import math

def f(x):
    if(x != 0):
        return abs(math.sin(x)/x)
    else:
        return 1

delta_x = 1; Area = 0

for i in range(-10, 11, delta_x):
    print(i)
    Area = Area + (f(i)*delta_x)

print('Area is '+str(Area))
