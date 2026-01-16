def f(fnc, prods):
 pro =  list(map(fnc,prods))
 return ",".join(pro)
print(f(lambda x: (x[0]+x[-1]).upper(),["water","cheese","tomato"]))