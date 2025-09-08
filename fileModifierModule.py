import logging
import os
import json

# By this file appending files all content is deleted before new data adding into file
def file_previous_data_deleting():
    with open("transactions.txt", "a+") as file:
        file.seek(0)
        file.truncate(0)
    with open("transactions.json", "w") as file:
        file.truncate(0)

def customer_data_reading_and_assigning_from_file():
    while True:
        try:
            file_input_path = input("Input file path ")
            with open(file_input_path, 'r') as file_content:
                file_lines = file_content.readline()
            user_info = file_lines.split(',')  # By this line string in customerData was split and returned  as list
            user_info_values = []

            for pair in user_info:  # For loop which split each value of user_info list and add it to new user_info_values list
                value = pair.split('=')[1]  # Value of first index in user_info list assigned to value var
                user_info_values.append(value)  # Value var is appended to new user_info_values list

            # Code below this line, extract value of specified index and assigns it to specified variables
            first_name = user_info_values[0]
            last_name = user_info_values[1]
            balance = float(user_info_values[2])
            active_loan = float(user_info_values[3])

        except FileNotFoundError:  # Handling of not found customer data file
            print("File was not found")
            logging.warning("File of customer data reading was not found")
            continue
        except PermissionError:  # Handling of access permission of customer data file
            print("No permission to access the file.")
            logging.warning("No permission to access the customer data reading file")
            continue
        else:
            print("Data loaded successfully from current file")
            logging.info("Data successfully loaded from customer data reading file")
            return first_name, last_name, balance, active_loan


def customer_data_reading_and_assigning_from_json():
    file_input_path = os.path.join(os.getcwd(), "transactions.json")
    with open(file_input_path, 'r') as json_file:
        data = json.load(json_file)

    first_name = data["first_name"]
    last_name = data["last_name"]
    balance = float(data["balance"])
    active_loan = float(data["active_loan"])
    return first_name, last_name, balance, active_loan
