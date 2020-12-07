a=[[*map(set,g.split())] for g in open("input").read().split("\n\n")]
print(sum(len(set.union(*x))for x in a),sum(len(set.intersection(*x))for x in a))
#print([sum([len(f(*x))for x in a])for f in[set.union,set.intersection]])
