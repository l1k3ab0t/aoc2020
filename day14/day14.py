
mem = {}
mem2 = {}
mask = ""

for line in open("input"):
    if "mask" in line:
        mask = line.strip().split(" = ")[1][::-1]
    else:
        cell, val = line.strip().split(" = ")
        cell = int(cell[4:-1])
        val = int(val)
        masked = 0
        masked_add = list([0])
        for i, c in enumerate(mask):
            if c == "1":
                v = 2**i
                masked += v

                for j in range(len(masked_add)):
                    masked_add[j] += v

            elif c== "X":
                v = 2**i & val
                masked += v
                
                nmasked = masked_add.copy()
                for j in range(len(masked_add)):
                    nmasked.append(masked_add[j]+2**i)
               
                masked_add = nmasked

            else:
                v = 2**i & cell
                if v:
                    print(v)
                    for j in range(len(masked_add)):
                        masked_add[j] += v

        for cell in masked_add:
            mem2[cell] = val

        mem[cell] = masked


print(sum(mem.values()))
print(sum(mem2.values()))
