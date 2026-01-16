import math
class C:
    def __init__(self,x,y):
        self.x= x
        self.y = y
    def m1(self):
        if self.x>0 and self.y>0:
            return 1
        elif self.x<0 and self.y>0:
            return 2
        elif self.x<0 and self.y<0:
            return 3
        elif self.x>0 and self.y<0:
            return 4
        else:
            return 0
    def m2(self,a,b):
        yx = 0
        ab = 0
        if self.x>0 and self.y>0:
            yx= 1
        elif self.x<0 and self.y>0:
            yx =2
        elif self.x<0 and self.y<0:
            yx = 3
        elif self.x>0 and self.y<0:
            yx = 4
        else:
            yx = 0

        if a>0 and b>0:
            ab =1
        elif a<0 and b>0:
            ab =2
        elif a<0 and b<0:
            ab =3
        elif a>0 and b<0:
            ab = 4
        else:
            ab =0
        if ab ==yx:
            return True
        else:
            return False
    def m3(self, a,b):
        distance = math.sqrt((self.x - a)**2+(self.y - b)**2)
        return distance >5 
def main():
  p = C(2,3)
  print(p.m1()) 
  print(p.m2(7,4)) 
  print(p.m2(-3,1)) 
  print(p.m3(8,5))
  print(p.m3(4,7)) 
 
if __name__ == "__main__":
    main()
                            



