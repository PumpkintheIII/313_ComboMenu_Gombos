total_cost_list = []
final_order_list = []
sandwich_list = ["Chicken", "Beef", "Tofu"]
sandwich_price_list = [5.25, 6.25, 5.75]
drink_list = ["Small", "Medium", "Large"]
drink_price_list = [1, 1.75, 2.25]
def welcome():
  print("Welcome!")
  print("Choose between the following sandwiches:")
  print("  1: Chicken ($5.25)")
  print("  2: Beef ($6.25)")
  print("  3: Tofu ($5.75)")
def sandwich():
  index = int(input("Please select the number of the sandwich you would like to purchase! (1, 2, or 3)"))
  print("You picked " + sandwich_list[index-1] + " for $" + str(sandwich_price_list[index-1]) + ".")
  final_order_list.append(sandwich_list[index-1])
  total_cost_list.append(sandwich_price_list[index-1])
def drink():
  print("Would you like to add a drink?")
  print("  1: Yes")
  print("  2: No")
  wantDrink = int(input("Please select 1 or 2."))
  if (wantDrink < 2):
    print("Which size would you like?")
    print("  1: Small ($1)")
    print("  2: Medium ($1.75)")
    print("  3: Large ($2.25)")
    index = int(input("Please select the number of the drink size you would like to purchase! (1, 2, or 3)"))
    print("You picked " + drink_list[index-1] + " for $" + str(drink_price_list[index-1]) + ".")
    final_order_list.append(drink_list[index-1])
    total_cost_list.append(drink_price_list[index-1])
def total_cost():
  total_cost = 0
  index = 0
  length = len(total_cost_list)
  x = 0
  print("Your order so far:")
  while (x < length):
    total_cost = total_cost + total_cost_list[index]
    print(final_order_list[index], total_cost_list[index])
    x = x + 1
    index = index + 1
  print("Your total cost is " + str(total_cost))
welcome()
sandwich()
drink()
total_cost()