# Homework 1
# Lisa Chen


import sys
import os
import pathlib
import re
import pickle

# Person class with values of the file
class Person():
    # assigns the given values as needed
    def __init__(self, last, first, mi, id, phone):
        self.last = last
        self.first = first
        self.mi = mi
        self.id = id
        self.phone = phone

    # displays the needed info
    def display(self):
        print("Employee id: " + self.id)
        print("\n" + self.first + self.mi + self.last)
        print("\n" + self.phone)

# This function process the text to be more standardized
def text_processing(read_text):
    # split on comma to get fields as text variables
    comma_split = re.split(',', read_text)
    # modify last and first name to be in Capital case if needed
    if comma_split[0:1].isupper():
        comma_split[5:6].capitalize()
        comma_split[10:11].capitalize()
        comma_split[15:16].capitalize()
        comma_split[20:21].capitalize()
    else:
        first_last_name = comma_split[0:1]
        first_last_name.capitalize()
        comma_split[5:6].capitalize()
        comma_split[10:11].capitalize()
        comma_split[15:16].capitalize()
        comma_split[20:21].capitalize()
    # modify middle initial to be single uppercase letter if needed. X is used if one is missing
    mid_name = comma_split[2]
    if mid_name == "":
        comma_split[2] = "X" # assigns X to blank middle initial
    else:
        mid_name.capitalize() # capitalize middle initial
    if comma_split[7] == "":
        comma_split[7] = "X" # assigns X to blank middle initial
    else:
        mid_name.capitalize() # capitalize middle initial
    if comma_split[12] == "":
        comma_split[12] = "X"  # assigns X to blank middle initial
    else:
        mid_name.capitalize()  # capitalize middle initial
    if comma_split[17] == "":
        comma_split[17] = "X"  # assigns X to blank middle initial
    else:
        mid_name.capitalize()  # capitalize middle initial
    if comma_split[22] == "":
        comma_split[22] = "X"  # assigns X to blank middle initial
    else:
        mid_name.capitalize()  # capitalize middle initial

    # modify id if needed where id should be 2 letters followed by 4 digits (employee_id)
    person_ID = comma_split[3]
    id_check = re.search("[a-zA-Z]{2}\d{4}", person_ID) #checks for 2 letters and 4 digits
    if id_check != 'None':
        person_ID = comma_split[8]
    else:
        print("ID invalid: " + id) # displays error msg
        print("\nID is two letters followed by 4 digits") # displays error msg
        # If id not in correct format, display error msg and user asked to re-enter a valid id
        comma_split[3] = input("\nPlease enter a valid id:") # displays error msg
        person_ID = comma_split[13] # sets new id num
    if id_check != 'None':
        person_ID = comma_split[13]
    else:
        print("ID invalid: " + id) # displays error msg
        print("\nID is two letters followed by 4 digits") #displays error msg
        # If id not in correct format, display error msg and user asked to re-enter a valid id
        comma_split[13] = input("\nPlease enter a valid id:") #takes in new id
        person_ID = comma_split[18] # sets new id number
    if id_check != 'None':
        person_ID = comma_split[18]
    else:
        print("ID invalid: " + id) # displays error msg
        print("\nID is two letters followed by 4 digits") #displays error msg
        # If id not in correct format, display error msg and user asked to re-enter a valid id
        comma_split[18] = input("\nPlease enter a valid id:") # takes in new id num
        person_ID = comma_split[23] #sets new id
    if id_check != 'None':
        person_ID = comma_split[23]
    else:
        print("ID invalid: " + id) # prints out error msg
        print("\nID is two letters followed by 4 digits") #prints out error msg
        # If id not in correct format, display error msg and user asked to re-enter a valid id
        comma_split[23] = input("\nPlease enter a valid id:") # takes in new id
        person_ID = comma_split[23] # sets new id

    # modify phone number if needed to be in form 999-999-9999
    phone_num = comma_split[4]
    phone_num_check = re.search("[-]{1}\d{3}[-]{1}\d{3}[-]{1}\d{3}", phone_num)
    if phone_num_check == "None":
        print("Phone " + phone_num + "is invalid") # prints out error msg
        print("\nEnter phone number in form 123-456-7890") # prints out error msg
        phone_num = input("\nEnter phone number:") # takes in new phone number
    phone_num = comma_split[9]
    phone_num_check = re.search("[-]{1}\d{3}[-]{1}\d{3}[-]{1}\d{3}", phone_num)
    if phone_num_check == "None":
        print("Phone " + phone_num + "is invalid")  # prints out error msg
        print("\nEnter phone number in form 123-456-7890")  # prints out error msg
        phone_num = input("\nEnter phone number:")  # takes in new phone number
    phone_num = comma_split[14]
    phone_num_check = re.search("[-]{1}\d{3}[-]{1}\d{3}[-]{1}\d{3}", phone_num)
    if phone_num_check == "None":
        print("Phone " + phone_num + "is invalid")  # prints out error msg
        print("\nEnter phone number in form 123-456-7890")  # prints out error msg
        phone_num = input("\nEnter phone number:")  # takes in new phone number
    phone_num = comma_split[19]
    phone_num_check = re.search("[-]{1}\d{3}[-]{1}\d{3}[-]{1}\d{3}", phone_num)
    if phone_num_check == "None":
        print("Phone " + phone_num + "is invalid")  # prints out error msg
        print("\nEnter phone number in form 123-456-7890")  # prints out error msg
        phone_num = input("\nEnter phone number:")  # takes in new phone number
    phone_num = comma_split[24]
    phone_num_check = re.search("[-]{1}\d{3}[-]{1}\d{3}[-]{1}\d{3}", phone_num)
    if phone_num_check == "None":
        print("Phone " + phone_num + "is invalid")  # prints out error msg
        print("\nEnter phone number in form 123-456-7890")  # prints out error msg
        phone_num = input("\nEnter phone number:")  # takes in new phone number

    person = Person(comma_split)  # Person object
    Dict = {id: person}  # person object saved to dictionary of person where id is the key
    # checks for duplicate id and prints out error msg
    if len(comma_split) != len(set(comma_split)):
        print("There is an ID repeated in the input file. Try again.")
        quit()
    else:
        employ_dict = Dict
    # returns dict of persons to main function
    return employ_dict

# function to open file for non-window operating systems
def other_OS_method(filepath):
    with open(os.path.join(os.getcwd(), filepath), 'r') as f:
        text_in = f.read().splitlines() # splitting up text as needed
        return text_in

# function to open files in windows
def win_method(filepath):
    with open(pathlib.Path.cwd().joinpath(filepath), 'r') as f:
        text_in = f.read().splitlines() # splitting up text as needed
        return text_in

def main():
    # ensures file can be opened in windows or mac and sets up input file
    if len(sys.argv) < 2:
        print('You need to enter a filename as a system arg') # displays error message
        quit() # quits program if user didn't enter filename as sysarg
    else:
        file_path = sys.argv[1] # # sets up sysargv for the file name
        read_text = win_method(file_path)  # function call for opening file
        if read_text < 1:
            file_path = sys.argv[1]  # # sets up sysargv for the file name
            read_text = other_OS_method(file_path) # function call for opening file

    employ_dict = text_processing(read_text[1:]) # calls text processing function and gets rid of the 1st line in file

    # Dictionary saved as pickle file
    pickle.dump(employ_dict, open('employ_dict.pickle', 'wb'))

    # open pickle file to read
    employ_dict_in = pickle.load(open('employ_dict.pickle', 'rb'))

    # print out person's info using Person class display method()
    print("\n\nEmployee list:")
    for employee_id in employ_dict_in.keys():
        employ_dict_in[employee_id].display()

if __name__ == '__main__':
    main()



