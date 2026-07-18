def greet_costumer():
    print("Welcome To Te Lemonade stand!")
    print("Freash Lemonade Only Made For You!")
greet_costumer()
price_per_cup = float(input("Enter The Price Per Cup:"))
cups_sold = int(input("Enter The Number Of Cups Sold:"))
def calculate_total(price, cups):
    total = price*cups
    return total
total_cost = calculate_total(price_per_cup, cups_sold)
rounded_total = round(total_cost, 2)
print("Total Cost:",rounded_total)
amount_paid = float(input("Enter The Amount Paid By The Costumer:"))
def calculate_change(paid, total):
    change = paid - total
    return change
change_due = calculate_change(amount_paid,rounded_total)
rounded_change = round(change_due,2)
print("")
print("=====LEMONADE STAND RECEPIT=====")
print("Price Per Cup:",price_per_cup)
print("Cups Sold", cups_sold)
print("Total Cost", rounded_total)
print("Amount Paid",amount_paid)
print("Change Due",rounded_change)
print("=============================")
