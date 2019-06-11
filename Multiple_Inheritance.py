class Car:
    def __init__(self, tyres=4):
        self.tyres = tyres

class Gasoline_Car(Car):
    def __init__(self, engine='gasoline', tank_cap=20):
        Car.__init__(self)
        self.engine = engine
        self.tank_cap = tank_cap
        self.tank = 0

    def refuel(self):
        self.tank = self.tank_cap

class Electric_Car(Car):
    def __init__(self, engine='electric', kwph_cap=60):
        Car.__init__(self)
        self.engine = engine
        self.kwph_cap = kwph_cap
        self.kwph = 0

    def recharge(self):
        self.kwph = self.kwph_cap

class Hybrid(Gasoline_Car, Electric_Car):
    def __init__(self, engine='hybrid', tank_cap=10, kwph_cap=50):
        Gasoline_Car.__init__(self, engine, tank_cap)
        Electric_Car.__init__(self, engine, kwph_cap)

toyota = Hybrid()
print (toyota.tyres)
print (toyota.tank)
print (toyota.kwph)

print ('After Refuelling the car')
toyota.refuel()
toyota.recharge()
print (toyota.tank)
print (toyota.kwph)