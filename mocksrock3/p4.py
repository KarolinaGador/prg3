def f(fnc,res):
    
    aa = list(filter(fnc,res))
    a = max(aa)
    b= min(aa)
    return a-b



print(f(lambda x: x>30 and x<90,[95,90,20,50,70] ))        