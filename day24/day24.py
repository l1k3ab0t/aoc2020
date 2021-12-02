from collections import defaultdict
from operator import itemgetter

def get_coord(line):
    i = 0
    r,g,b = 0,0,0
    while i<len(line):
        if line[i:i+2] == "sw":
            g+=1
            b-=1
            i+=2
        elif line[i:i+2] == "se":
            r+=1
            b-=1
            i+=2
        elif line[i:i+2] == "nw":
            r-=1
            b+=1
            i+=2
        elif line[i:i+2] == "ne":
            g-=1
            b+=1
            i+=2
        elif line[i:i+1] == "w":
            r-=1
            g+=1
            i+=1
        elif line[i:i+1] == "e":
            r+=1
            g-=1

            i+=1

    return (r,g,b)

inst = [get_coord(l.strip()) for l in open("input")]

cnted = [(i,inst.count(i))  for i in set(inst)]
filterd = list(filter(lambda x: x[1]%2==1, cnted))
print("Part 1", len(filterd))


tiles = defaultdict(bool)
tiles.update(map(lambda x: (x[0], True), filterd))


def get_adjacent(coord):
    r = coord[0]
    g = coord[1]
    b = coord[2]

    adj = []
    for x in (-1,1):
        adj.append((r+x,g-x,b))
        adj.append((r+x,g,b-x))
        adj.append((r,g+x,b-x))
    return adj



for _ in range(100):
    next_tiles = defaultdict(bool)
    keys = list(tiles.keys())
    for tile in keys:
        if tiles[tile]:
            adj = get_adjacent(tile)
            bcnt = list(map(lambda x: tiles[x] , adj)).count(True)
            if bcnt in (1,2):
                next_tiles[tile] = True

            for adj_tile in adj:
                if not (tiles[adj_tile] or adj_tile in next_tiles):
                    adj_n = get_adjacent(adj_tile)

                    bcnt = list(map(lambda x: tiles[x] , adj_n)).count(True)
                    if bcnt == 2:
                        next_tiles[adj_tile] = True
                    else:
                        next_tiles[adj_tile] = False


    tiles = next_tiles.copy()
    
print(list(tiles.values()).count(True))

