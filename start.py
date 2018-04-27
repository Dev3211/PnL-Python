#!/usr/bin/python
# -*- coding: utf-8 -*-
import mathclass

ob = mathclass.MyClass()

print('\n')
which = raw_input(' Which calulator do you want to choose? The advanced or the basic one: ')
print('\n')

if which == "advanced":
 num1 = raw_input(' Cost price: ')
 num2 = raw_input(' Selling price: ')
 profit = raw_input(' Profit: ') # either one of them
 loss = raw_input(' Loss: ')
 print('\n')
 if num1 == "0":
  print("Selling price = {}".format(int(num2)))
  print("Profit = {}".format(int(profit)))
  print("Cost price = {}".format(int(num2) - int(profit)))
  print("Therefore the cost price is {}".format(int(num2) - int(profit)))
  print('\n')
  print('Or if there is loss:')
  print("Selling price = {}".format(int(num2)))
  print("Loss = {}".format(int(loss)))
  print("Cost price = {}".format(int(num2) + int(loss)))
  print("Therefore the cost price is {}".format(int(num2) + int(loss)))
 elif num2 == "0":
  print("Cost price = {}".format(int(num1)))
  print("Profit = {}".format(int(profit)))
  print("Selling price = {}".format(int(num1) + int(profit)))
  print("Therefore the Selling price is {}".format(int(num1) + int(profit)))
  print('Or if there is loss:')
  print("Cost price = {}".format(int(num1)))
  print("Loss = {}".format(int(loss)))
  print("Selling price = {}".format(int(num1) - int(loss)))
  print("Therefore the selling price is {}".format(int(num1) - int(loss)))

elif which == "basic":
 num1 = int(raw_input(' Cost price: '))
 num2 = int(raw_input(' Selling price: '))
 print('\n')
 if not num1 or not num2:
  raise Exception('Either one of the number seems to be blank')
 elif num1 == num2:
  print("Therefore, as your selling price and the cost price is the same; you have earned no profit nor loss.")
  print('\n')
  print("Profit = {}".format(float(ob.sub(num1, num2))))
  print("Loss = {}".format(float(ob.sub(num2, num1))))
 elif num1 > num2:
  print("Therefore, as your cost price is higher than the selling price; there is a loss.")
  print('\n')
  print("Loss = {}".format(float(ob.sub(num1, num2))))
  percent = float(ob.sub(num1, num2))
  print("Loss percent = {}".format(round(percent / num1 * 100, 2)) + "%")
 elif num2 > num1:
  print("Therefore, as your selling price is higher than the cost price; there is a profit.")
  print('\n')
  print("Profit = {}".format(float(ob.sub(num2, num1))))
  percent = float(ob.sub(num2, num1))
  print("Loss percent = {}".format(round(percent / num1 * 100, 2)) + "%")
else:
 print('Please either type advanced or basic')
