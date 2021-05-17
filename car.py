class Car:
    car_name="Tesla"
    def __init__ (self,name,model):
            self.name=name
            self.model=model
    def buy(self):
        return f"I bought a {self.name} for a million dollars"

    def ride(self):
        return f"The car I rode yesterday was of this model {self.model} "