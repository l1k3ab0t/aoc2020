f = open('input', 'r')
arr = [int(l.rstrip("\n")) for l in f]

for i,x in enumerate(arr):
    for j in range(i+1, len(arr)):
        if x+arr[j]==2020:
            print("Part 1: ",x *arr[j])
        else:
            for k in range(j+1, len(arr)):
                if x+arr[j]+arr[k] == 2020:
                    print("Part 2: ", x*arr[j]*arr[k])
