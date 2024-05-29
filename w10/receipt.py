
import csv
from datetime import datetime

def main():
    filename = "request.csv"
    key_column_index = 0
    name_index = 1
    price_index = 2
    quantity_index = 1
    sales_tax_amount = .06
    current_datetime = datetime.now()
    coupon = False
    try:
        print("Jenny's Fresh Market Place")
        with open(filename, "rt") as requestfile:
            requestfile = csv.reader(requestfile)
            next(requestfile)
            total_items = 0
            subtotal = 0
            products_dict = read_dict("products(1).csv", key_column_index)
            for line in requestfile:
                quantity = float(line[quantity_index])
                total_items += quantity
                product_num = str(line[key_column_index])
                product_line = products_dict[product_num]
                price_of_item = float(product_line[price_index])
                total_price_of_items = quantity * price_of_item
                subtotal += total_price_of_items
                if product_num == "H001": # this is 8 rolls toilet tissue
                    coupon = True
            print(f"Your total number of items: {total_items}")
            print(f"Your subtotal is: {subtotal:.2f}")
            sales_tax = subtotal * sales_tax_amount
            print(f"Sales tax: {sales_tax:.2f}")
            grand_total = subtotal + sales_tax
            print(f"Your total is: {round(grand_total, 2)}")
            print("Thank You!")
            print(current_datetime)
            if coupon == True:
                print(f"Get 1$ off the next time you buy a package of '8 rolls toilet tissue' and \n"
                "mention the coupon code: Never Felt Better!")
    except FileNotFoundError as file_not_found_error:
        print(file_not_found_error)
        print("The file was not found")
    except PermissionError as permission_error:
        print(permission_error)
        print("Authority to view file was not given. ")
    except KeyError as key_error:
        print(key_error)
        print("Wrong user input. ")
    else:
                """PART 2: 
        Print the store name at the top of the receipt.
    Print the list of ordered items.
    Sum and print the number of ordered items.
    Sum and print the subtotal due.
    Compute and print the sales tax amount. Use 6% as the sales tax rate.
    Compute and print the total amount due.
    Print a thank you message.
    Get the current date and time from your computer's operating system and print the current date and time.
    Include a try block and except blocks to handle FileNotFoundError, PermissionError, and KeyError."""
        
    
def read_dict(products_file, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    product_dict = {}
    with open(products_file, "rt") as read_file:
        read_file = csv.reader(read_file)
        next(read_file)
        for line in read_file:
            prod_num = line[key_column_index]
            product_dict[prod_num] = line
    return product_dict

if __name__ == "__main__":
    main()