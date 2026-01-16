def f(uid):
    for nazwy in uid:
        if uid.count(nazwy)>1:
            return False
        
    return True
print(f(["abc123","ann","abc123","a10"]))