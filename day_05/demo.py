#import numpy as np

x1, y1, x2, y2 = 8,0,0,8
#x1, y1, x2, y2 = 9,7,7,9
#x1, y1, x2, y2 = 1,1,3,3

if x1 > x2:
    xs = range(x2,x1+1)
else:
    xs = reversed(range(x1,x2+1))

if y1 > y2:
    ys = range(y2,y1+1)
else:
    ys = reversed(range(y1,y2+1))

for x,y in zip(xs, ys):
    print(y,x)
