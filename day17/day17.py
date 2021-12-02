from copy import deepcopy

init_state = [[(c=="#") for c in l.strip()] for l in open("input")] 

space = []
for _ in range(13):
    dim = []
    for _ in range(13):
        plain = []
        for _ in range(12+len(init_state)):
            plain.append([False]*(12+len(init_state[1])))
        dim.append(plain)
    space.append(dim)


def pretty_space(s):
    for z,plain_2d in enumerate(s):
        for y,plain_1d in enumerate(plain_2d):
            l = "".join(map(lambda x: "#" if x else ".",plain_1d))
            print(l)
        print("\n")


for y in range(len(init_state)):
    for x in range(len(init_state[0])):
        space[6][6][y+6][x+6] = init_state[y][x]


pretty_space(space[6])

def count_active(space, x,y,z,w):
    c = 0
    for ow in range(-1,2):
        aw = w + ow
        if aw<0 or aw>=len(space):
            continue

        for oz in range(-1,2):
            az = z + oz
            if az<0 or az >= len(space[0]):
                continue

            for oy in range(-1,2):
                ay = y + oy
                if ay<0 or ay >= len(space[0][0]):
                    continue
                
                for ox in range(-1,2):
                    ax = x + ox
                    if ax<0 or ax >= len(space[0][0][0]):
                        continue
                    if ax != x or ay != y or az != z or aw != w:
                        c += space[aw][az][ay][ax]
    return c 



for cycle in range(6):
    old_space = deepcopy(space)
    for w in range(len(space)):
        for z in range(len(space[0])):
            for y in range(len(space[0][0])):
                for x in range(len(space[0][0][0])):
                    c = count_active(old_space, x,y,z,w)
                    if old_space[w][z][y][x]:
                        if c !=3 and c!=2:
                            space[w][z][y][x] = False
                    else:
                        if c == 3:
                            space[w][z][y][x] = True
        

print(sum(sum(sum(map(sum,plain)) for plain in dim) for dim in space))
