total_cost_list = []
final_order_list = []
sandwich_list = ["Chicken", "Beef", "Tofu"]
sandwich_price_list = [5.25, 6.25, 5.75]
drink_list = ["Small Drink", "Medium Drink", "Large Drink"]
drink_price_list = [1, 1.75, 2.25]
frie_list = ["Small Fries", "Medium Fries", "Large Fries", "Mega-Sized Fries"]
frie_price_list = [1, 1.5, 2, 2]
"""
total_cost_list: a list of the price of each item in the order
final_order_list: a list of each item in the order
sandwich_list: list of sandwich options
sandwich_price_list: list of sandwich prices
drink_list: list of drink sizes
drink_price_list: list of drink sizes
"""
print("Welcome!")
def welcome():
  #welcome message
  welcome = 0
  print("What would you like to order?")
  print("  1: Sandwich")
  print("  2: Drink")
  print("  3: French Fries")
  print("  4: View your final order")
  welcome = int(input("Please enter the number corresponding with the item you would like. (1, 2, 3, or 4)"))
  if (welcome == 1):
    sandwich()
  elif (welcome == 2):
    drink()
  elif (welcome == 3):
    fries()
  elif (welcome == 4):
    total_cost()
def sandwich():
  print("Choose between the following sandwiches:")
  print("  1: Chicken ($5.25)")
  print("  2: Beef ($6.25)")
  print("  3: Tofu ($5.75)")
  index = int(input("Please select the number of the sandwich you would like to purchase! (1, 2, or 3)"))
  #user inputs which sandwich they would like and sets the index variable to it's corresponding number
  print("You picked " + sandwich_list[index-1] + " for $" + str(sandwich_price_list[index-1]) + ".")
  #tells the user which sandwich they picked and it's price
  final_order_list.append(sandwich_list[index-1])
  #adds the sandwich to the final order list
  total_cost_list.append(sandwich_price_list[index-1])
  #adds the sandwich price to the final order list
  total_cost()
  welcome()
def drink():
  print("Would you like to add a drink?")
  print("  1: Yes")
  print("  2: No")
  #asks the user if they want a drink
  wantDrink = int(input("Please select 1 or 2."))
  #prompts the user to select 1 or 2 if they want a drink or not
  if (wantDrink < 2):
    #checks if they responded yes or no
    print("Which size would you like?")
    print("  1: Small ($1)")
    print("  2: Medium ($1.75)")
    print("  3: Large ($2.25)")
    #if they responded yes, lists the drink size options
    index = int(input("Please select the number of the drink size you would like to purchase! (1, 2, or 3)"))
    #has the user input the size they want, sets the index variable to its corresponding value
    print("You picked " + drink_list[index-1] + " for $" + str(drink_price_list[index-1]) + ".")
    #tells the user the drink size and price they picked
    final_order_list.append(drink_list[index-1])
    #adds the drink to the finla order list
    total_cost_list.append(drink_price_list[index-1])
    #adds the drink to the final cost list
  total_cost()
  welcome()
def fries():
  print("Would you like to add french fries?")
  print("  1: Yes")
  print("  2: No")
  #asks the user if they want a drink
  wantFries = int(input("Please select 1 or 2."))
  #prompts the user to select 1 or 2 if they want a drink or not
  if (wantFries < 2):
    #checks if they responded yes or no
    print("Which size would you like?")
    print("  1: Small ($1)")
    print("  2: Medium ($1.50)")
    print("  3: Large ($2)")
    #if they responded yes, lists the drink size options
    index = int(input("Please select the number of the frie size you would like to purchase! (1, 2, or 3)"))
    #has the user input the size they want, sets the index variable to its corresponding value
    if (index == 1):
      print("Would you like to mega-size your fries?")
      print("  1: Yes")
      print("  2: No")
      mega = int(input("Please select 1 or 2."))
      if (mega == 1):
        index = 4
    print("You picked " + frie_list[index-1] + " for $" + str(frie_price_list[index-1]) + ".")
    #tells the user the drink size and price they picked
    final_order_list.append(frie_list[index-1])
    #adds the drink to the finla order list
    total_cost_list.append(frie_price_list[index-1])
    #adds the drink to the final cost list
  total_cost()
  welcome()
def total_cost():
  total_cost = 0
  #sets the total_cost local variable to 0
  index = 0
  #sets the index local variable to 0
  length = len(total_cost_list)
  #sets the length local variable to the length of the total_cost_list
  x = 0
  #sets the x local variable to 0
  print("Your order so far:")
  #prints a title 
  while (x < length):
    #runs the following code, for all the items in the total_cost_list
    total_cost = total_cost + total_cost_list[index]
    #sets total_cost local variable to total_cost + the next item in the total_cost_list
    print(str(final_order_list[index]) + " $" + str(total_cost_list[index]))
    #prints the item name and price
    x = x + 1
    #updates x variable
    index = index + 1
    #updates index variable
  print("Your total cost is " + str(total_cost))
  #prints total cost
#runs each of the functions
welcome()