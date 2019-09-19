#%%
class Account():

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return "Account owner: %s \nAccount balance: %i" % (self.owner, self.balance)

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            print("You don't have the funds!")
            return
        self.balance -= amount
        return self.balance
#%%
ac = Account('jose',100)
print(ac)

#%%
ac.withdraw(150)

#%%
ac.deposit(50)

#%%
ac.withdraw(150)

#%%
ac.withdraw(1)

#%%
ac.deposit(1000)

#%%
print(ac)

#%%
ac.owner

#%%
ac.balance