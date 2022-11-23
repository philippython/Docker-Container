"""How do I minimize this code and also make the program to start afresh Incase if user wants to make a new order?"""

#START KITE IMPORT
import json
from time import sleep
#END KITE IMPORT

Fried_Rice = 1
Jollof_Rice =2
Fruit_Juice = 3
Vegetable_Soup = 4
Turkey = 5
price_1 = '$3'
price_2 = '$2'
price_3 = '$1.5'
price_4 = '$2.5'
price_5 = '$1.5'
ask_name = str(input("Enter Name: "))
print("Welcome " + ask_name + str("\n\nBelow Are Items Available\n1: Fried Rice\n2: Jollof Rice\n3: Fruit Juice"))
print("4: Vegetable Soup\n5: Turkey\n")
selection = int(input("" + ask_name +"\n\nEnter From 1-5: "))
if selection == 1:
  print('' + ask_name + " You selected, Fried Rice, And the price is " + price_1)
  order_quest = input(str("Would You Like To Order?\nYes Or No: "))
  if order_quest == 'yes':
    print("Order Sent For Delivery!!")
  elif order_quest == 'no':
    print(f"Alrght " + ask_name + ' Until next Time')
  else:
    print("You haven\'t or have made invalid response!!")
elif selection == 2:
  print('' + ask_name + " You selected, Jollof Rice, And the price is " + price_2)
  order_quest = input(str("Would You Like To Order?\nYes Or No: "))
  if order_quest == 'yes':
    print("Order Sent For Delivery!!")
  elif order_quest == 'no':
    print("Alrght " + ask_name + ' Until next Time')
  else:
    print("You haven\'t or have made invalid response!!")
elif selection == 3:
  print('' + ask_name + " You selected, Fruit Juice, And the price is " + price_3)
  order_quest = input(str("Would You Like To Order?\nYes Or No: "))
  if order_quest == 'yes':
    print("Order Sent For Delivery!!")
  elif order_quest == 'no':
    print("Alrght " + ask_name + ' Until next Time')
  else:
    print("You haven\'t or have made invalid response!!")
elif selection == 4:
  print('' + ask_name + " You selected, Vegetable Soup, And the price is " + price_4)
  order_quest = input(str("Would You Like To Order?\nYes Or No: "))
  if order_quest == 'yes':
    print("Order Sent For Delivery!!")
  elif order_quest == 'no':
    print("Alrght " + ask_name + ' Until next Time')
  else:
    print("You haven\'t or have made invalid response!!")
elif selection == 5:
  print('' + ask_name + " You selected, Turkey, And the price is " + price_5)
  order_quest = input(str("Would You Like To Order?\nYes Or No: "))
  if order_quest == 'yes':
    print("Order Sent For Delivery!!")
    sleep(2.5)
  elif order_quest == 'no':
    print("Alrght " + ask_name + ' Until next Time')
    sleep(2.5)
  else:
    print("You haven\'t or have made invalid response!!")
    sleep(2.5)
else:
  print("Next time, only select from available items")
  sleep(2.5)