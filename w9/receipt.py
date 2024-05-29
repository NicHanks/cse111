
import csv

def main():
    key_column_index = 0
    name_index = 1
    price_index = 2
    quantity_index = 1
    products_dict = read_dict("products.csv", key_column_index)
    print(products_dict)
    with open("request.csv", "rt") as request:
        read_file = csv.reader(request)
        next(read_file)
        for row_list in read_file:
            key = row_list[key_column_index]
            quantity = int(row_list[quantity_index])
            value = products_dict[key]
            price = value[price_index]
            name = value[name_index]
            print(name, quantity, "@", price)
    
def read_dict(filename, key_column_index):
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
    with open(filename, "rt") as readfile:
        read_file = csv.reader(readfile)
        next(read_file)
        for line in read_file:
            prod_num = line[key_column_index]
            product_dict[prod_num] = line
    return product_dict
if __name__ == "__main__":
    main()