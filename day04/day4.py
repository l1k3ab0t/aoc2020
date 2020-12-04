import re

inp = open("input")

istring = inp.read()

i = 0
for pp in re.split("\n\n", istring):
    
    pp = pp.replace("\n", " ")
    print(pp)

    m = re.search("byr:(\d){4,}", pp)
    if not m or not 1920 <=int(m.group()[4:])<=2002:
        continue

    m = re.search("iyr:(\d){4,}", pp)
    if not m or not 2010 <=int(m.group()[4:])<=2020:
        continue
    
    m = re.search("eyr:(\d){4,}", pp)
    if not m or not 2020 <=int(m.group()[4:])<=2030:
        continue

    m = re.search("hgt:(\d)+(cm|in)", pp)
    if not m:
        continue
    w = m.group()
    print(w, int(w[4:len(w)-2]))
    if "cm" in w and not 150<=int(w[4:len(w)-2])<=193:
        continue
    elif "in" in w and not 59<=int(w[4:len(w)-2])<=76:
        continue
    print(w)
    

    m = re.search("ecl:(amb|blu|brn|gry|grn|hzl|oth)", pp)
    if not m:
        continue
    print(m.group())



    m = re.search("hcl:#(\d|[abcdef]){6}", pp)
    if not m:
        continue
    print(m.group())

    m = re.search("pid:(\d){9}(?!\d)", pp)
    if not m:
        continue
    print(m.group())




    i+=1

print(i, len(inp.read()))
