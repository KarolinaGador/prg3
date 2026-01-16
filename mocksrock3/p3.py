def f(d):
 counter = 0
 suma = 0
 for val in d.values():
  suma = suma + val
  counter = counter + 1

 avg = suma/counter
 ilosc = 0
 for key, val in d.items():
  if d[key]>avg:
   ilosc = ilosc + 1
 return ilosc 

print(f({"LO231":150,"BA787":20,"NZ15":30})) 