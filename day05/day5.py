s=sorted(int(x[:-1].translate({66:49,70:48,82:49,76:48}),2)for x in open("input"))
print(s[-1], sum(range(s[0],s[-1]+1))-sum(s))
