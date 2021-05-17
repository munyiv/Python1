class Student:
    school="AkiraChix"
    def __init__ (self,name,age):
            self.name=name
            self.age=age
    def speak(self):
        return f"Hello class my name is{self.name}"

    def year_of_birth(self):
        return f"Hey i was born in { 2021-self.age}"
        
