
import csv

def main():
    student_dict = read_dict("students.csv")
    print(student_dict)
    inumber = input("Inumber: ")
    find_inumber(inumber, student_dict)

def find_inumber(inumber, student_dict):
    if inumber in student_dict:    
        value = student_dict[inumber]
        name = value[1]
        print(name)
    else:
        print("No such student")
    
def read_dict(filename):
    """Read the contents of a CSV file into a
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
    Return: a dictionary that contains
        the contents of the CSV file.
    """
    student_dict = {
        }
    with open(filename) as file:
        reader = csv.reader(file)
        next(reader)
        for row_list in reader:
            inumber = row_list[0].strip()
            name = row_list[1].strip()
            student_dict[inumber] = row_list
    return student_dict

if __name__ == "__main__":
    main()