s=list(map(lambda x:int(x[:7],2)*8+int(x[7:-1],2),("".join(str(int(ord(xi)>77)) if ord(xi)>70 else str(int(ord(xi)<67)) for xi in x) for x in open("input").readlines())))
s.sort()
print(s[-1], sum(range(s[0],s[-1]+1))-sum(s)) 
