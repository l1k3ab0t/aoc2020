
lines = [l.strip() for l in open("input2")]

start = int(lines[0])

buses =list(map(int,filter(lambda x: x.isdigit(),lines[1].split(","))))

print(buses)
for i in range(min(buses)):
    for bus in buses:
        if (i+start) % bus == 0:
            print(i*bus)



arr1 = []
arr2 = []


for offset,sub_string in enumerate(lines[1].split(",")):
    if sub_string != "x":
        n = int(sub_string)
        arr1.append(n)
        arr2.append(offset)


print(arr1,arr2)

def findMinX(num, rem, k): 
    x = num[0] ; # Initialize result 
  
    # As per the Chinise remainder 
    # theorem, this loop will 
    # always break. 
    while(True): 
          
        # Check if remainder of  
        # x % num[j] is rem[j]  
        # or not (for all j from  
        # 0 to k-1) 
        j = 0; 
        while(j < k): 
            if ((x % num[j]) + rem[j] != num[j]): 
                break; 
            j += 1; 
  
        # If all remainders  
        # matched, we found x 
        if (j == k): 
            return x; 
  
        # Else try next numner 
        x += num[0]; 




print(findMinX(arr1,arr2,len(arr1)))
