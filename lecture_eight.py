# class student:
# #     name = "yamini"

# # s1 = student()
# # print(s1.name)
# # s2 = student()
# # print(s2.name)
# class Car:
#     color ="blue"
#     brand ="Mercedees"

# car1 = Car()
# print(car1.brand)

class Account :
    def __init__(self,bal,acc,account_pass):
        self.balance = bal
        self.account_no = acc
        self.__account_password = account_pass
        # reset password
    def reset_password(self):
        print(self.__account_password) 
# debit method
    def debit(self,amount):
        self.balance  -= amount
        print("Rs.",amount,"debited from your account")
        print("Total amount .", self.get_balance())

    def credit(self,amount):
        self.balance += amount
        print("Rs.", amount,"Credited to your account")
        print("Total amount .", self.get_balance())


    def get_balance(self):
        return self.balance
    
AccountDetails = Account(10000,31521233444,"yaminee")
print(AccountDetails.reset_password())
# AccountDetails.debit(1000)
# AccountDetails.credit(500)
# AccountDetails.credit(65000)
# print(AccountDetails.balance)
# print(AccountDetails.account_no)