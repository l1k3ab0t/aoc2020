a = [[set(y) for y in g.split()] for g in open("input").read().split("\n\n")] 
print(sum(map(lambda x:len(set.union(*x)),a)),sum(map(lambda x:len(set.intersection(*x)),a)))
