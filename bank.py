class BankAccount:
    car_name="Barclays"
    def __init__ (self,name,year_of_start,balance):
            self.name=name
            self.year_of_start=year_of_start
            self.balance=balance
    def amount(self):
        return f"Your remaining balance is {self.balance} Thank you for chosing our bank"

    def name(self):
        return f"{self.name} bank is my bank of choice "

    def start(self):
        return f"Our bank has been in the industry for  {self.year_of_start-2021} years "