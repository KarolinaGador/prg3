import re
def f(numbers):
    pattern = '^[+-]?[1-7a-dA-D]+$'
    git = 0
    for i in numbers:
        if re.match(pattern, i):
         git = git +1
        else:
           continue
    return git

print(f(["A05","-3+1","7ab8C","+Bb7","-22c55"]))     