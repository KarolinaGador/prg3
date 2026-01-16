class C:
    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age
    def __str__(self):
        if self.age>=18:

         return f'{self.fname[0].upper()}{self.lname[0].upper()}{self.age}'  
        else:
         return f'{self.fname[0].lower()}{self.lname[0].lower()}{self.age}'
def main():
 a = C("Anna","Brown",17) 
 print(a)             
if __name__ == "__main__":
    main()     