import re
def f(dates):
    pattern ='[1-2]{1}[0-9]{3}[-]{1}[0-9]{2}[-]{1}[0-9]{2}'
    a = re.findall(pattern, dates)
    return a
print(f("2021-1-3,05/12/2024,1998-12-11,9 maj 2007,2001-12-07,15-09-2011"))