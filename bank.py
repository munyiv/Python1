from datetime import datetime
class BankAccount:
   
    def __init__ (self,name,phoneNumber):
            self.name=name
            self.balance=0
            self.phoneNumber=phoneNumber
            self.loan=0
            self.statement=[]
    def amount(self):
        return f"Your remaining balance is {self.balance} Thank you for chosing our bank"

    def name(self):
        return f"{self.name} bank is my bank of choice "


    def show_balance(self):
        return f"Hello {self.name}, your balance is {self.balance}"

    def deposit(self,ammount):
       if ammount<0:
           return f"Hello {self.name} Your balance is kshs {self.balance}"
       else:
            self.balance += ammount
            now=datetime.now()
            transaction={
                "ammount":{ammount},
                "time":now,
                "Narration":" You succesfully deposited"
            }
            self.statement.append(transaction)
            return self.show_balance()

    def show_statement(self):
        for transaction in self.statement:
           ammount=transaction["ammount"]
           Narration=transaction["Narration"]
           time=transaction["time"]
           date=time.strftime("%d /%m /%y")
           print(f"{date} {Narration} {ammount}")
        
         
        
     
    def withdraw(self,ammount):
       if ammount > self.balance:
           return f"Your balance is {self.balance} you can not withdraw {ammount}"
       else:
           self.balance -= ammount
           now=datetime.now()
           transaction={
                "ammount":{ammount},
                "time":now,
                "Narration":" You have withdrawn"
            }
           self.statement.append(transaction)

           return self.show_balance()



    def borrow(self,ammount):
        return f"Hello {self.name} I am glad to inform you that you can now acess kshs {ammount-self.loan} of loan from us"

    def pay(self,ammount):
        return f"Hello you are due to pay our loan of kshs{ammount}" 

    
# starndard libray you can say import math (contains a lot of math) 
# from datetime import datetime deals with time
#to get current time use datetime.now() to format time we use create a var now=datetime.now