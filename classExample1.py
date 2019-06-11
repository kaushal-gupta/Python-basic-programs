class Bankaccount:
      def __init__(self):
          self.balance=0
      def deposit(self,amount):
          self.balance+=amount
      def withdraw(self,amount):
          self.balance-=amount


tp=Bankaccount()
print(tp.balance)
tp.deposit(1000)
print tp.balance
tp.withdraw(500)
print tp.balance
