import math
a = [1, 0]
b = [1/math.sqrt(2), 0]
t = [0.25, 0]
p = [1, 0]


iterations = 3
for i in range(0, iterations):
    a[1] = 0.5*(a[0]+b[0])
    b[1] = math.sqrt(a[0]*b[0])
    t[1] = t[0] - p[0]*math.pow(a[0] - a[1], 2)
    p[1] = 2*p[0]
    a[0], b[0], t[0], p[0] = a[1], b[1], t[1], p[1]
pi = math.pow(a[0]+b[0], 2)/(4*t[0])
print("pi = ", pi)
