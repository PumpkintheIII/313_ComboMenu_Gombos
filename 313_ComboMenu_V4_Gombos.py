total_cost_list = []
final_order_list = []
sandwich_list = ["Chicken", "Beef", "Tofu"]
sandwich_price_list = [5.25, 6.25, 5.75]
drink_list = ["Small Drink", "Medium Drink", "Large Drink"]
drink_price_list = [1, 1.75, 2.25]
frie_list = ["Small Fries", "Medium Fries", "Large Fries", "Mega-Sized Fries"]
frie_price_list = [1, 1.5, 2, 2]
type_list = []
"""
total_cost_list: a list of the price of each item in the order
final_order_list: a list of each item in the order
sandwich_list: list of sandwich options
sandwich_price_list: list of sandwich prices
drink_list: list of drink sizes
drink_price_list: list of drink prices
frie_list: list of frie sizes
frie_price_list: list of frie prices
type_list: used for finding the combo discount
"""
print("Welcome!")


def welcome():
  #welcome message
  welcome = 0
  #intializes the welcome variable
  print(
    "\nWhat would you like to order?\n  1: Sandwich\n  2: Drink\n  3: French Fries\n  4: Ketchup Packets\n  5: Check Out"
  )
  welcome = int(
    input(
      "Please enter the number corresponding with the item you would like. (1, 2, 3, 4, or 5)"
    ))
  #asks what you would like to add to your order
  #if-elif statement below calls the corresponding function depending on what they want to add to their order
  if (welcome == 1):
    sandwich()
  elif (welcome == 2):
    drink()
  elif (welcome == 3):
    fries()
  elif (welcome == 4):
    ketchup()
  elif (welcome == 5):
    check_out()


def sandwich():
  print(
    "\nChoose between the following sandwiches:\n  1: Chicken ($5.25)\n  2: Beef ($6.25)\n  3: Tofu ($5.75)"
  )
  #displays sandwich options
  index = int(
    input(
      "Please select the number of the sandwich you would like to purchase! (1, 2, or 3)"
    ))
  #user inputs which sandwich they would like and sets the index variable to it's corresponding number
  print("You picked " + sandwich_list[index - 1] + " for $" +
        str(sandwich_price_list[index - 1]) + ".")
  #tells the user which sandwich they picked and it's price
  final_order_list.append(sandwich_list[index - 1])
  #adds the sandwich to the final order list
  total_cost_list.append(sandwich_price_list[index - 1])
  #adds the sandwich price to the final order list
  type_list.append(1)
  #adds a value to the type list signifying that the user added a sandwich to the order
  total_cost()
  #tells the user their order cost so far
  welcome()


  #allows the user to add more items to their order
def drink():
  print("\nWould you like to add a drink?\n  1: Yes\n  2: No")
  #asks the user if they want a drink
  wantDrink = int(input("Please select 1 or 2."))
  #prompts the user to select 1 or 2 if they want a drink or not
  if (wantDrink < 2):
    #checks if they responded yes or no
    print(
      "Which size would you like?\n  1: Small ($1)\n  2: Medium ($1.75)\n  3: Large ($2.25)"
    )
    #if they responded yes, lists the drink size options
    index = int(
      input(
        "Please select the number of the drink size you would like to purchase! (1, 2, or 3)"
      ))
    #has the user input the size they want, sets the index variable to its corresponding value
    print("You picked " + drink_list[index - 1] + " for $" +
          str(drink_price_list[index - 1]) + ".")
    #tells the user the drink size and price they picked
    final_order_list.append(drink_list[index - 1])
    #adds the drink to the finla order list
    total_cost_list.append(drink_price_list[index - 1])
    #adds the drink to the final cost list
  type_list.append(2)
  #adds a value to the type list signifying that the user added a drink to the order
  total_cost()
  #tells the user their order cost so far
  welcome()


  #allows the user to add more items to thier order
def fries():
  print("\nWould you like to add french fries?\n  1: Yes\n  2: No")
  #asks the user if they want fries
  wantFries = int(input("Please select 1 or 2."))
  #prompts the user to select 1 or 2 if they want fries or not
  if (wantFries < 2):
    #checks if they responded yes or no
    print(
      "Which size would you like?\n  1: Small ($1)\n  2: Medium ($1.50)\n  3: Large ($2)"
    )
    #if they responded yes, lists the frie size options
    index = int(
      input(
        "Please select the number of the frie size you would like to purchase! (1, 2, or 3)"
      ))
    #has the user input the size they want, sets the index variable to its corresponding value
    if (index == 1):
      # if the user selected a small, askes if they want to mega-size their fries
      print("Would you like to mega-size your fries?\n  1: Yes\n  2: No")
      mega = int(input("Please select 1 or 2."))
      if (mega == 1):
        #if they do, sets the local index variable accordingly
        index = 4
    print("You picked " + frie_list[index - 1] + " for $" +
          str(frie_price_list[index - 1]) + ".")
    #tells the user the frie size and price they picked
    final_order_list.append(frie_list[index - 1])
    #adds the frie to the finla order list
    total_cost_list.append(frie_price_list[index - 1])
    #adds the frie to the final cost list
  type_list.append(3)
  #adds a value to the type list signifying that the user added fries to the order
  total_cost()
  #tells the user their order cost so far
  welcome()


  #allows the user to add more items to their order
def ketchup():
  print("\n  Ketchup ($0.25 each)")
  ketchup = int(
    input("How many ketchup packets would you like? Enter the number here."))
  print("You added " + str(ketchup) + " ketchup packets for $" +
        str(ketchup * 0.25) + ".")
  total_cost_list.append(ketchup * 0.25)
  final_order_list.append(str(ketchup) + " ketchup packets")
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
  print("")
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
  print("Your total cost is $" + str(total_cost))
  #prints total cost


#runs each of the functions
def check_out():
  print("")
  #blank string to add space between parts of the program
  index = 0
  #initializes the local index variable
  InitialCost = 0
  #initializes the logal InitialCost varialbe, used to tell the user the cost before the combo discount
  length = len(type_list)
  #initializes the length variable
  s = 0
  d = 0
  f = 0
  #intitialzies the s, d, and f varialbes. s = sandwich, d = drink, f = fries
  discount = 0
  #initialzies the discount variable, used to tell the user what the discound is
  while (index < length):
    #loops the following code for each item in the type list
    if (type_list[index] == 1):
      s = s + 1
      #for every sandwich in the type list, adds 1 to the sandwich variable
    elif (type_list[index] == 2):
      d = d + 1
      #for every drink in the type list, adds 1 to the drink variable
    elif (type_list[index] == 3):
      f = f + 1
      #for every fries in the type list, adds 1 to the fries variable
    InitialCost = InitialCost + total_cost_list[index]
    #adds the cost of each item together and puts them in the InitialCost variable
    index = index + 1
    #updates the index variable
  index = 0
  #sets the index variable to 1
  cost = InitialCost
  #sets the cost variable to the InitialCost variable
  while (index < length):
    if (s > 0 and d > 0 and f > 0):
      #checks if there is 1 of each item in the order
      cost = cost - 1
      #if ther is, subtracts 1 from the price
      s = s - 1
      d = d - 1
      f = f - 1
      #updates the item varialbes
      discount = discount + 1
      #updates the discount variable
    print("  " + final_order_list[index] + " $" + str(total_cost_list[index]))
    #prints each item in the order, along with their cost
    index = index + 1
  print("Your order cost is: $" + str(InitialCost) +
        "\nYour combo discount is: $" + str(discount * 1) +
        "\nYour final price is: $" + str(cost))
  #prints the order cost, combo discount, and final price


welcome()