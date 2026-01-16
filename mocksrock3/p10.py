def f(value1):
    def mnoznik(value2):
        return value1 * value2
    
    
    return mnoznik

# Użycie:
times_five = f(5)    
print(times_five(8))   

times_three = f(3)     
print(times_three(7))  