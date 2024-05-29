from datetime import datetime
subtotal = float(input("Please enter the subtotal: "))
current_day = datetime.now().weekday()
discount_rate = 0.10
sales_tax = 0.06
if (current_day == 1 or current_day == 2):
    if subtotal >= 50:        
        discount = subtotal * discount_rate
        subtotal = subtotal - discount
        print(f'Discount amount: {discount:.2f}')
    else:
        difference = 50 - subtotal
        print(f"The difference to get the discount is {difference:.2f}.")
    
sales_tax_value = subtotal * sales_tax
print(f"Sales tax amount: {sales_tax_value:.2f}")

total = subtotal + sales_tax_value
print(f"Total: {total:.2f}")
