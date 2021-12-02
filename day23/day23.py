
cups = [int(c) for c in "158937462"]
#cups = [int(c) for c in "389125467"]
cups = cups + list(range(10,1000001))

arr = [0] * (len(cups)+1)
n = len(arr)

for i in range(0, n-2):
    arr[cups[i]] = cups[i+1]

arr[1000000] = cups[0]

print(n, arr.count(0))

i = cups[0]
for r in range(10000000):


    assert i != 0

    if r%1000000 == 0:
        print(r)

    
    
    #print(cups, cc)

    pick = []
    j = i
    for _ in range(0,3):
        pick.append(arr[j])
        j = arr[j]

    arr[i] = arr[pick[2]]
    
    #print(pick)

    dest = (i-1)%1000001
    
    if dest == 0:
        dest = 1000000
    while dest in pick:
        dest=(dest-1)%1000001
        if dest == 0:
            dest = 1000000

    #print(dest)
    temp = arr[dest]

    arr[dest] = pick[0]
    arr[pick[2]] = temp
    

    i = arr[i]

#sol = ""
#i = cups.index(1)
#for off in range(1, 9):
#    sol+=str(cups[(i+off)%n])
#
#print(sol,cups)


print(arr[1] * arr[arr[1]])
