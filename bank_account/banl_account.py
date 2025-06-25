class BankAccount:
  def __init__(self, firstName,lastName,accountId,accountType,pin,balance):
    self.firstName = firstName
    self.lastName = lastName
    self.accountId = accountId
    self.pin = pin
    self.balance = balance
  
  def deposit(self,money):
    self.balance = self.balance + money
    return(self.balance)
  
  def withdraw(self, money):
    if money <= self.balance:
      self.balance = self.balance - money
      return(self.balance)
    else:
      print('Invalid Number')
  
  def display_balance(self):
    print(self.firstName + '' + self.lastName + f' Balance is: ${self.balance}')

arthur = BankAccount('Arthur', 'Fernandes', '112', 'Savings Account', 1234, 1000.0) 

arthur.deposit(500.00)
arthur.display_balance()
arthur.withdraw(200.00)
arthur.display_balance()