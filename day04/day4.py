import re
from itertools import repeat


passports =re.split("\n\n", open(input).read())

p1_patterns=["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
p2_patterns=["byr:((19[2-9]\d)|200[0-3])", 
            "iyr:20(1\d|20)",
            "eyr:20(2\d|30)", 
            "hgt:(1([5-8]\d|9[0-3])cm|(59|6\d|7[0-6])in)", 
            "ecl:(amb|blu|brn|gry|grn|hzl|oth)", 
            "hcl:#(\d|[abcdef]){6}", 
            "pid:(\d){9}(?!\d)"]

solution1 = [not any(elem is None for elem in map(lambda x: re.search(*x), zip(p1_patterns, repeat(passport)))) for passport in passports].count(True)
print("Part 1", solution1)

solution2 = [not any(elem is None for elem in map(lambda x: re.search(*x), zip(p2_patterns, repeat(passport)))) for passport in passports].count(True)
print("Part 2", solution2)
