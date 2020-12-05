s=sorted(map(lambda x:int(x[:7],2)*8+int(x[7:-1],2),(x.translate({66:49,70:48,82:49,76:48}) for x in open("input").readlines())))
print(s[-1], sum(range(s[0],s[-1]+1))-sum(s)) 
