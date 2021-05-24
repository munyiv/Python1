class Student:
    school="AkiraChix"

    def __init__ (self,firstName,lastName ,age):
            self.firstName=firstName
            self.lastName=lastName
            self.age=age

    def speak(self):
        return f"Hello class my name is{self.name}"


    def greet(self):
        return f"Hello {self.firstName},welcome to {self.school} you are {self.age} years old"

    def year_of_birth(self):
        return f"Hey i was born in { 2021-self.age}"

    def initials(self):
        return f"Hello {self.firstName} your initials are {self.firstName[0]},{self.lastName[0]}"



        
