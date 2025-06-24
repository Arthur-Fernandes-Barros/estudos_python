options = [
 '🍔 Cheeseburger',
 '🍟 Fries',
 '🥤 Soda',
 '🍦 Ice Cream',
  '🍪 Cookie' 
 ]

def get_item(option):
    if 1 <= option <= len(options):
        return options[option - 1]
    else:
        return "Invalid option"


def welcome():
  print('=====================')
  print('Welcome to MacDonalds')
  print('=====================')
  print('')
  print('1- 🍔 Cheeseburger')
  print('2- 🍟 Fries')
  print('3- 🥤 Soda')
  print('4- 🍦 Ice Cream')
  print('5- 🍪 Cookie')

welcome()
option = int(input('What would you like to order? '))
print(get_item(option))
