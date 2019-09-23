class vehicle:
    def __init__(self,doors,wheels,name):
            self.doors=doors
            self.wheels=wheels
            self.name=name
    def __repr__(self):
        return "%s: %d doors and %d wheels"%(self.name, self.doors, self.wheels)
    def __eq__(self,aveh):
        return self.doors==aveh.doors and self.wheels==aveh.wheels
    def __iadd__(self,aveh):
            self.doors+=aveh.doors
            self.wheels+=aveh.wheels
            self.name+="+"
            self.name+=aveh.name
            return self
car1=vehicle(4,4,"sedan")
car2=vehicle(2,4,"coupe")
car3=vehicle(2,4,"mini")
cycle=vehicle(0,2,"motorcycle")
truck=vehicle(18,2,"semi")
car1
print(car1)
car1==car2
car2==car3
car1+=cycle
print(car1)