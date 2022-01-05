class coordinate(object):
    def __init__(self,x,y):# definre the object
        self.x=x
        self.y=y
    def distance(self,other): # fiunction on the object
        x_dist=(self.x-other.x)**2
        y_dist=(self.y-other.y)**2
        return (x_dist+y_dist)**0.5   
    def __str__ (self):
        return "("+str(self.x)+","+str(self.y)+")"

c=coordinate(1,2)#print(c.distance(coordinate(3,4)))
#print(coordinate.distance(c,coordinate(3,4)))
#print(coordinate(3,4))
#print(type(c))
class fraction(object):
    def __init__(self,num,denom):
        assert type(num)== int and type(denom)==int, "numerator and denominator must be integers"


        self.num=num
        self.denom=denom
    def __str__(self):
        return str(self.num)+"/"+str(self.denom)
    def __add__(self,other): 
        new_num=self.num*other.denom+self.denom*other.num
        new_denom=self.denom*other.denom
        return fraction(new_num,new_denom)
print(fraction(1,2))
print(fraction(1,3)+fraction(1,4))     




