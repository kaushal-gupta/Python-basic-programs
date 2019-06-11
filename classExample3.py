class Account:
     noa=0
     def __init__(self):
         self.balance=1000
         Account.noa+=1
     @staticmethod
     def account_info():
         print Account.noa

Account.account_info()
a=Account()

Account.account_info()
