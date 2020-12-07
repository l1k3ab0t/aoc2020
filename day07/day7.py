from collections import defaultdict


subbags = defaultdict(set)
supbags = defaultdict(set)
for line in open("input"):
    parts = line.strip().split(" bags contain ")
    key = parts[0]
    vals = parts[1].replace(".","").replace(" bags","").replace(" bag","").split(", ")
    
    if "no other" in line:
        supbags[key].add((0,""))
        continue
    
    for val in vals:
        subbags[val[2:]].add(key)
        supbags[key].add((int(val[0]), val[2:]))


def p1(key): 
    return subbags[key].union(*map(p1, subbags[key]))


def p2(key):
    return sum([cnt*p2(bag)+cnt for cnt, bag in supbags[key]])


print(len(p1("shiny gold")))
print(p2("shiny gold"))
