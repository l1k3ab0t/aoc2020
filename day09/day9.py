numbers = [int(l.strip()) for l in open("input")]

def p1():
    for i in range(25,len(numbers)):
        preamble = numbers[i-25:i]
        intc = list(map(lambda x: numbers[i]-x in preamble, preamble))
        if not any(intc):
            return numbers[i]


def p2(target):
    for i in range(0,len(numbers)):
        for j in range(i+2,len(numbers)):
            r = numbers[i:j]
            s = sum(r)
            
            if s == target:
                return min(r) + max(r)
            elif s>target:
                break


target = p1()
print("Part 1", target)
print("Part 2", p2(target))
