lines = [(lambda x: (x[0], int(x[1])))(line.strip().split(" ")) for line in open("input")]


def run(prog, part1=True):

        visited = [False for i in lines]
        acc = 0
        index = 0

        while True:

            op, arg = prog[index]
            visited[index] = True

            if op == "acc":
                acc += arg
                index+=1
            elif op == "jmp":
                index += arg
            else:
                index+=1

            if index >= len(lines):
                return acc
            
            if visited[index]:
                break
    
        if part1: 
            return acc


def p2():

    for i in range(len(lines)):
        
        if lines[i][0] == "nop":
            lines[i] = ("jmp", lines[i][1])
        elif lines[i][0] == "jmp":
            lines[i] = ("nop", lines[i][1])
        else:
            continue

        result = run(lines, False)
        if result is not None:
            return result

        if lines[i][0] == "nop":
            lines[i] = ("jmp", lines[i][1])
        elif lines[i][0] == "jmp":
            lines[i] = ("nop", lines[i][1])


print("Part 1", run(lines))
print("Part 2", p2())
