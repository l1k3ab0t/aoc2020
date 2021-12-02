# start = [0,3,6]
start = [1,0,18,10,19,6]


spoken = {}

for i,num in enumerate(start[:-1]):
    spoken[num] = i+1


last = start[-1]

for i in range(len(start)+1,30000001):
    if last in spoken:
        llast = last
        last = i -1 -spoken[last]
        spoken[llast] = i - 1
    else:
        spoken[last] = i - 1
        last = 0
    
    if i == 2020:
        print("Part 1", last)


print("Part 2", last)
