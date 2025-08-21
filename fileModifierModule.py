import os

def customer_data_reading():
    global file_content
    global file_lines
    file_input_path = input("Input file path ")
    with open(file_input_path, 'r') as file_content:
        file_lines = file_content.readline()

def transaction_history_adding_into_file(first_name,last_name,count,expense,balance,active_loan):
    file_output_path = os.path.join(os.getcwd(), "transactions.txt")
    with open(file_output_path, 'a') as output_file_content:
        output_file_content.write(f"Customer ID-{first_name} {last_name} {count},Expense -{expense}, Balance after "
                                  f"expense-{balance},Active loan-{active_loan}, \n")
