import math
import matplotlib.pyplot as plt
import random
import numpy as np
from sympy import symbols, Eq, solve

SIDES = 6
AREA = 100

SLEN = math.sqrt((AREA * 4 * math.tan(math.pi/SIDES)) / SIDES)
EXTANG = math.pi - (SIDES-2) * math.pi / SIDES

xc, yc = symbols('xc yc')

def dist(x1, y1, x2, y2):
    return math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))

def geteq(x1, y1, x2, y2):
    m = (y2 - y1) / (x2 - x1)
    eq = Eq(yc - y1 - m * (xc - x1), 0)
    return eq


vertices = [(0, 0), (SLEN, 0)]
last = vertices[-1]

ext_ang = EXTANG

for i in range(SIDES - 2):
    x = SLEN * math.cos(ext_ang) 
    y = SLEN * math.sin(ext_ang) 

    temp = (last[0] + x, last[1] + y)

    vertices.append(temp)
    last = temp
    ext_ang += EXTANG


xpts = [pt[0] for pt in vertices]
ypts = [pt[1] for pt in vertices]

maxdist = dist(vertices[0][0], vertices[0][1], vertices[int(SIDES/2)][0], vertices[int(SIDES/2)][1]) - 2
eligible = False
while not eligible: 
    randpt = (random.uniform(min(xpts), max(xpts)), random.uniform(min(ypts), max(ypts)))
    dists = [dist(randpt[0], randpt[1], v[0], v[1]) for v in vertices]
    eligible = True
    for dist in dists:
        if dist > maxdist: eligible = False

rand_pts = [rantpt]






plt.figure(figsize=(5, 5))
plt.plot(xpts, ypts, 'ro')

plt.axis([
    min(xpts) - 3,
    max(xpts) + 3,
    min(ypts) - 3,
    max(ypts) + 3
])

plt.show()