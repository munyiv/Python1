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
        
    def show_balance(self):
        return f"Hello {self.name}, your balance is {self.balance}"

    def deposit(self,ammount):
        try:
            0+ammount
        except TypeError:
            return f"The ammount must be in figures"
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

    def transfer(self,account,ammount):
            try:
                0+ammount
            except TypeError:
                return f"Please input your ammount in figures"
            fee= ammount*0.05
            total=ammount+ fee
            self.balance-=total
            account.deposit(ammount)
            if total>self.balance:
                    return f"Hello {self.name} your balance is {self.balance} and you need at least {total} for this transfer"
            else :
                    return f"Hello {self.name} you have transfered your money to a different account"

    def show_statement(self):
        for transaction in self.statement:
           ammount=transaction["ammount"]
           Narration=transaction["Narration"]
           time=transaction["time"]
           date=time.strftime("%d /%m /%y")
           print(f"{date} {Narration} {ammount}")
        
         
        
     
    def withdraw(self,ammount):
        try:
            0+ammount
        except TypeError:
            return f"The ammount must be in figures"
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
        try:
            0+ammount
        except TypeError:
            return f"Please input the ammount in figures"
        if ammount < 0:
            return f"Your amount is{self.balance} you can not borrow a loan"
        elif  self.loan > 0:
            return f"Hello {self.name} you have an outstanding loan.Please repay your outstanding loan "
        elif ammount < 0.1* self.balance:
            return f"Sorry {self.name} you are not qualified"
        else:
            loan=ammount * 1.05
            self.loan=loan
            self.balance += ammount
            now=datetime.now()
            transaction={
                "ammount":{ammount},
                "time":now,
                "Narration":" You have succesfully borrowed"
            }
            self.statement.append(transaction)

            return f"You have sucesfully borrowed"

      
            

    def repay(self,ammount):
        try:
            0+ammount
        except TypeError:
            return f"Please input the ammount in figures"
        if ammount <0:
           return f"Hello {self.name} you should repay your entire loan"
        elif ammount<= self.loan:
            self.loan-=ammount
            return f"You have repaid the loan"
        else:
            diff=ammount-self.loan
            self.loan=0
            self.deposit(diff)
            now=datetime.now()
            transaction={
                "ammount":{ammount},
                "time":now,
                "Narration":" You have succesfully repaid your loan"
            }
            self.statement.append(transaction)
 
            return f"You have succesfuly repaid your loan" 

class MobileMoneyAccount(BankAccount):
    def __init__(self, name, phoneNumber,service_provider):
        BankAccount.__init__(self,name, phoneNumber)
        self.service_provider=service_provider

    def buy_airtime(self,ammount):
        try:
            0+ammount
        except TypeError:
            return f"Please input the ammount in figures"
        if ammount<0:
            return f"Hello {self.name} your balance is {ammount}"
        elif self.balance < ammount:
            return f"Dear customer your account balance is low recharge your balance"
        else :
            self.balance -=ammount
            return f"Dear customer you have bought airtime worth {ammount}"
    
    

        
      
      
     

      


