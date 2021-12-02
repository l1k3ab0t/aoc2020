import re
from operator import add
from functools import reduce, cache


fields, myticket, others = re.split("\n\n", open("input").read())


def split_fields(field):
    fname, ranges = field.split(": ")
    ranges = [int(x) for x in re.split("[-|( or )]", ranges) if x.isdigit()] 
    ranges = list(range(ranges[0],ranges[1]+1)) +  list(range(ranges[2],ranges[3]+1))

    return (fname, ranges)



fields = list(map(split_fields, fields.split("\n")))
myticket = [int(x) for x in myticket.split("\n")[1].split(",")]
others= [[int(xi) for xi in x.split(",")] for x in others.split("\n")[1:-1]]


ticket_nums = list(reduce(add, others))
f_nums = set(reduce(add, map(lambda x: x[1], fields)))

field_map = dict(fields)
r_field_map = {tuple(v): k for k, v in field_map.items() }


valid_tickets = []
for ticket in others:
    if all((num in f_nums)  for num in ticket):
        valid_tickets.append(ticket)



for num in f_nums:
     ticket_nums = list(filter(num.__ne__, ticket_nums))


cols = list(zip(*valid_tickets))

m = dict()


keys = list(r_field_map.keys())

j = 0


print(len(cols), len(keys))

@cache
def find_positions(i, r1, r2):

    for j in r1:
        s1 = set(cols[j])
        for k in r2:
            if s1 <= set(keys[k]):
                r1 = list(r1.copy())
                print(r1, j)

                r1.remove(j)

                r2 = list(r2).copy()
                r2.remove(k)
               
                if len(r2) == 0:
                    return True, {r_field_map[keys[k]]:i}

                found, sol = find_positions(i+1, frozenset(r1), frozenset(r2))
                
                if found:
                    sol[r_field_map[keys[k]]] = i
                    return found, sol
   
    return False, None

_, m = find_positions(0, frozenset(range(20)), frozenset(range(20)))

p2 = 1
for key in field_map.keys():
    if "departure" in key:
        print(key, m[key], myticket[m[key]])
        p2 *= myticket[m[key]]



#print(ticket_nums)
#print(f_nums)

print(m)
print(sum(ticket_nums))
print(p2)

