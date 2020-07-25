class car():
    def __init__(self, name):
        self.name = name
        self.sum = 0
    def kilometers(self, amount):
        self.sum += amount
a = car("Truck")
a.kilometers(53)#騎了23公里
a.kilometers(34)#騎了34公里
b = car("Trailer")
b.kilometers(49)#騎了59公里
b.kilometers(45)#騎了45公里
c = car("Hatchback")
c.kilometers(5)#騎了5公里
print(a.name)
print(b.name)
print(c.name)
print(a.sum)
print(b.sum)
print(c.sum)