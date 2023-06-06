import math
import matplotlib.pyplot as plt
import random
import numpy as np
from sympy import symbols, Eq, solve

SIDES = 3 # SET NUMBER OF SIDES
AREA = 1000
ITERATIONS = 1000000 # NUMBER OF ITERATIONS
SLEN = math.sqrt((AREA * 4 * math.tan(math.pi/SIDES)) / SIDES)
EXTANG = math.pi - (SIDES-2) * math.pi / SIDES
WINDOWSIZE = 10

xc, yc = symbols('xc yc')

def distcalc(x1, y1, x2, y2):
    return math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))


vertices = [(0, 0), (SLEN, 0)]
last = vertices[-1]

ext_ang = EXTANG

## Calculates vertex coordinates, circle trig
for i in range(SIDES - 2):
    x = SLEN * math.cos(ext_ang) 
    y = SLEN * math.sin(ext_ang) 

    temp = (last[0] + x, last[1] + y)

    vertices.append(temp)
    last = temp
    ext_ang += EXTANG


xpts = [pt[0] for pt in vertices]
ypts = [pt[1] for pt in vertices]

## checks wheter a random point is inside the polygon, preferably towards the centre, by comparing its distance with 
## all vertices with the maximum distance between two vertices
maxdist = distcalc(vertices[0][0], vertices[0][1], vertices[int(SIDES/2)][0], vertices[int(SIDES/2)][1]) - 2
eligible = False

while not eligible: 
    randpt = (
        random.uniform(min(xpts), max(xpts)), 
        random.uniform(min(ypts), max(ypts))
    )

    dists = []
    for v in vertices:
        dists.append(distcalc(randpt[0], randpt[1], v[0], v[1]))

    eligible = True
    for dist in dists:
        if dist > maxdist: eligible = False

## Sierpinksi stuff, chooses a random vertex, plots midpoint between vertex and randomly chosen point from previous
## iterates x times, each time calculating the midpoint between a new random vertex and the previous midpoint

rand_pts = [randpt]

for i in range(ITERATIONS):
    randvert = vertices[random.randint(0, SIDES - 1)]
    mid_x = (rand_pts[-1][0] + randvert[0]) / 2
    mid_y = (rand_pts[-1][1] + randvert[1]) / 2
    rand_pts.append((mid_x, mid_y))

randxpts = [pt[0] for pt in rand_pts]
randypts = [pt[1] for pt in rand_pts]

print("calculated")

plt.figure(figsize=(WINDOWSIZE, WINDOWSIZE))
plt.plot(xpts + [0], ypts + [0], 'o:r')
# plt.plot([randpt[0]], [randpt[1]], 'bo')  ORIGINAL POINT
plt.plot(randxpts, randypts, 'ro', ms = 1)

plt.axis([
    min(xpts) - 3,
    max(xpts) + 3,
    min(ypts) - 3,
    max(ypts) + 3
])

plt.show()