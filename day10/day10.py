from functools import cache

adapters = sorted([int(l) for l in open("input")])

count1s = 0
count3s = 1

previous = 0
for adapter in adapters:
    div = adapter - previous
    if div == 1:
        count1s += 1
    elif div == 3:
        count3s += 1

    previous = adapter

print("Part 1", count1s*count3s)


last = adapters[-1]

#When DP is to much work
@cache
def p2(next_adapters):
   adapter = next_adapters[0]
   if adapter == last:
       return 1

   s = 0
   for i in range(1, min(len(next_adapters), 4)):
       if next_adapters[i] - adapter <= 3:
           s += p2(next_adapters[i:])

   return s 

print("Part 2", p2(tuple([0] + adapters)))
