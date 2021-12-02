
seats = ["."+l.strip()+"." for l in open("input")]

rows = len(seats)+2
cols = len(seats[0])

seats = ["."*rows] + seats + ["."*rows]


old_seats = []


def pretty(arr):
    for l in arr:
        print(l)


def occupated(arr, i,j):
    c = 0
    #down
    for l in range(i+1,rows):
        if arr[l][j] == "#":
            c+=1
            break
        if arr[l][j] == "L":
            break

    #up
    for l in range(1, i):
        if arr[i-l][j] == "#":
            c+=1
            break
        if arr[i-l][j] == "L":
            break


    #left
    for l in range(1,j):
        if arr[i][j-l] == "#":
            c+=1
            break
        if arr[i][j-l] == "L":
            break

    #right
    for l in range(j+1,cols):
        if arr[i][l] == "#":
            c+=1
            break
        if arr[i][l] == "L":
            break

    #up left
    for l in range(1, min(i,j)):
        if arr[i-l][j-l] == "#":
            c+=1
            break
        if arr[i-l][j-l] == "L":
            break

    #up right
    for l in range(1, min(i,cols-j)):
        if arr[i-l][j+l] == "#":
            c+=1
            break
        if arr[i-l][j+l] == "L":
            break

    #dowm left
    for l in range(1, min(rows-i,j)):
        if arr[i+l][j-l] == "#":
            c+=1
            break
        if arr[i+l][j-l] == "L":
            break

    #down right
    for l in range(1, min(rows-i,cols-j)):
        if arr[i+l][j+l] == "#":
            c+=1
            break
        if arr[i+l][j+l] == "L":
            break

    return c


change = True

while change:
    change = False


    #pretty(seats)
    old_seats = seats.copy()
    for i in range(1, rows):
        for j in range(1,cols):
            occ = occupated(old_seats,i,j)
            if old_seats[i][j] == "L" and occ==0:

                change = True

                row = list(seats[i])
                seats[i] = "".join((row[:j]+ ["#"] +row[j+1:]))
            elif old_seats[i][j] == "#" and occ>=5:

                change = True
                row = list(seats[i])
                seats[i] = "".join((row[:j]+ ["L"]+row[j+1:]))



print(sum(map(lambda x: x.count("#"),seats)))

