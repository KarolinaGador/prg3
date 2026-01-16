def f(word):
    lista = []
    if len(word)<=1:
        return word.upper()
    
    elif len(word)>1:
       cos =""
       for i in range(len(word)):
        
        for idx, litera in enumerate(word.lower()):
           if idx==i:
              cos = cos + litera.upper()
           else:  
              cos = cos + litera
        if i != len(word)-1:      
         cos = cos + "-"
       return cos
    
print(f("waTer"))    
         