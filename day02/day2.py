import re

lines = open("input").readlines()

i, j = 0, 0

for line in lines:
    words = re.split("[\W:-]", line)
    
    lower, upper = map(int, words[:2])
    c, _, pw  = words[2:5]


    cnt = pw.count(c)
    i += cnt >= lower <= upper

    j += (c is pw[lower-1]) != (c is pw[upper-1])

print("Part 1", i)
print("Part 2", j)
