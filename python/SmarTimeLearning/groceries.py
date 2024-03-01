grocery_list = ["bread", "eggs", "soda", "chips", "yogurt", "milk", "pizza", "chicken burger"]
item_price = {"bread": 7, "eggs": 10, "soda": 6, "chips": 5, "yogurt": 8, "milk": 10, "pizza": 13, "chicken burger": 10}
today_date = "February 25,  2024"
customer_name = input("Enter Customer Name : ")
print("Customer " + customer_name + "'s" + " Shopping list:")
print(grocery_list[0], item_price["bread"])
print(grocery_list[1], item_price["eggs"])
print(grocery_list[2], item_price["soda"])
print(grocery_list[3], item_price["chips"])
print(grocery_list[4], item_price["yogurt"])
print(grocery_list[5], item_price["milk"])
print(grocery_list[6], item_price["pizza"])
print(grocery_list[7], item_price["chicken burger"])
total = 0
for i in range(len(grocery_list)):
  total = total + item_price[grocery_list[i]]
print("Purchase Total: $" + str(total))
