def get_coords(x, y):
    l = [(x, y), (x + 1, y), (x + 2, y), (x + 1, y + 1), (x, y + 2), (x + 1, y + 2), (x + 2, y + 2)]
    return l
    

arr = [[int(x) for x in input().split()] for i in range(6)]

hs_list = []

for hy in range(4):
    for hx in range(4):
        hs = 0
        for coord in get_coords(hx, hy):
            x, y = coord
            hs += arr[y][x]

        hs_list.append(hs)

print(max(hs_list))
