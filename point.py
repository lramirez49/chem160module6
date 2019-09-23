class point:
    def __init__(self, dim, data):
        self.dim=dim
        self.data=[]
        for i in range(dim):
            self.data.append(float(data[i]))
    def __repr__(self):
        output=""
        for i in self.data:
            output+=str(i)+" "
        return output
    def scale(self, x):
        for i in range(self.dim):
            self.data[i]*=x
    def dot(self, apoint):
        sum=0
        for i in range(self.dim):
            sum+=self.data[i]*apoint.data[i]
        return sum
from point import *
p1=point(3, [1.2, 8.2, 3.4])
p1
p1.scale(3.3)
print(p1)
p2=point(3, [3.1, 4.5, 2.2])
print("p1 dot p2=", p1.dot(p2))