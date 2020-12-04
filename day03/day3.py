import operator
from functools import reduce


lines = open("input").readlines()

w = len(lines[0]) - 1 


def f(x, y):
    trees, p = 0,0
    for i in range(0,len(lines), y):
        trees += lines[i][p] == "#"
        p = (p+x) % w
    
    return trees


print("Part 1", f(3,1))
print("Part 2" , reduce(operator.mul, map(lambda x: f(*x) ,[(1,1),(3,1),(5,1),(7,1),(1,2)])))


