class Dog:
    dog_name="Tigger"
    def __init__ (self,name,type):
            self.name=name
            self.type=type
    def bark(self):
        return f"I bought a {self.type} puppy three days ago"

    def call(self):
        return f"When I call my puppy {self.name} it barks"