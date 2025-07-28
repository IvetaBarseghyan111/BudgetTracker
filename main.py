import os
count = 0 #Creation of count variable which will be used in transaction ID it will be increased every time,
# when user will do new purchase
transaction_history = [] #Creation empty list in which should be added user's transaction info
condition_check = True
user_response_check = True
expense_adding_check = True
#This function adds all necessary info of user purchase. This will show user's transaction history
def transaction_list_extending():
   transaction_history.extend([first_name,last_name,str(count), "Expense-", str(expense),
                               "Balance after expense-",str(balance), "Active_loan-", str(active_loan), "\n"])

#By this function user should be able to continue new purchase adding also it checks user want to pay with loan or not
def condition_and_user_response():
    global condition_check
    condition_check = True
    global user_response_check
    user_response_check = True

while expense_adding_check:#While loop of how user should add first,last name, balance and loan 1.from file
    # 2.Manually inputting
    expense_adding_condition = input("Do you want to enter your balance and loan manually? Type yes or no: ").strip().lower()
    if expense_adding_condition == "yes":
        while True: #First and last name saving loop
            first_name = input("Enter your first name:  ").strip().title()
            if not first_name or first_name.isspace():
                print("First name cannot be empty or just spaces. Try again.")
                continue
            elif len(first_name) > 30:
                print("First name cannot exceed 30 characters.")
                continue
            else:
                print("First name saved successfully.")
                break
        while True:
            last_name = input("Enter your last name: ").strip().title() #First name saving loop
            if not last_name or last_name.isspace():
                print("Last name cannot be empty or just spaces. Try again.")
                continue
            elif len(last_name) > 70:
                print("Last name cannot exceed 70 characters.")
                continue
            else:
                print("Last name saved successfully.")
                break
        while True:
            balance = input("Enter your balance amount: ")
            if balance.isdigit():
                balance = float(balance)
                print("Balance saved successfully.")
                break
            else:
                 print("Invalid input. Balance must be a number.")
                 continue
        while True:
            active_loan = input("Enter your active loan amount: ")
            if active_loan.isdigit():
                active_loan = float(balance)
                print("Active loan was successfully saved")
                break
            else:
                print("Invalid input. Loan amount must be a number..")
                continue
        condition_and_user_response()#After all necessary info submitting start of price inputting. Logic of
            # price will work
    elif expense_adding_condition == "no": #After this line user's first/last name, balance and loan values should be
        # extracted from customerData file
        try:
            file_input_path = os.path.join(os.getcwd(), "customerData.txt")
            with open(file_input_path, 'r') as file_content:
                file_lines = file_content.readline()
            key_value_pairs = file_lines.split(',')#By this line string in customerData was split and returned as list
            file_dict = {}#Creation of empty dictionary in which should be added customerData's list single item as key
            # value
            for pair in key_value_pairs: #For loop of customerData's list single item split, which was added to dict as
            # key and value
                key, value = pair.split("=")
                file_dict[key.strip()] = value.strip()
             #Logic below this line is of values get from dictionary and assigning to corresponding variable
            first_name = file_dict.get('first_name')
            last_name = file_dict.get('last_name')
            balance = float(file_dict.get('balance'))
            active_loan = float(file_dict.get('loan'))
            expense_adding_check = False
            condition_and_user_response()
        except FileNotFoundError:
            print("File was not found")
            break
        else:
            print("Data loaded successfully from current file")
    elif not expense_adding_condition or expense_adding_condition not in ["yes", "no"]:#Logic of when user do not
        # answer with correct option
        print("Invalid input. Please type yes or no.")
        continue
    while condition_check:
        expense = input("Enter the expense amount: ")
        if expense.isdigit() and float(expense) > 0:
            expense = float(expense)
            if balance >= expense:
                count += 1
                balance -= expense
                transaction_list_extending()
                print(f"Payment completed successfully.") #After purchase done, increment count by 1 and add it
                            # in transaction_history list
            else:
                user_response = (input(f"Insufficient balance. Do you want to use your loan to cover the remaining amount? (yes/no):" )
                                 .strip().lower())
                if user_response == "yes": #Check of payment completion with active loan
                    user_response_check = True
                else:
                    user_response_check = False
                if user_response_check and expense - balance <= active_loan: #Logic of payment completion from
                                # balance and active loan, new values assigning to balance and active loan
                    active_loan -= (expense - balance)
                    balance = 0
                    count += 1
                    transaction_list_extending()
                    print(f"Payment completed successfully.")
                elif user_response_check and (balance == 0 and active_loan == 0): #Logic of balance and active
                                # loan amount when they are 0
                    print(f"You have no funds left in balance or loan.")
                    break
                elif user_response == "yes" and expense - balance > active_loan: #Logic of active loan and
                                # entered price checking, when active loan < price , user should input new price
                    print(f"Not enough active loan. Your current active loan is {active_loan}")
                    count += 1
                    transaction_list_extending()
                    transaction_history.append("Not enough funds.Payment was cancelled")
                    continue
                else: #Logic of payment cancelled by user, when user type no for new price adding
                    print(f"Payment cancelled by user")
                    break
        else:
            print("Invalid amount. Expense must be greater then 0.")
            continue
        new_expense = input("Do you want to enter another expense.Please enter Yes or No ").strip().lower()
        if new_expense == "yes":
            condition_check = True
        else:
            condition_check = False
            expense_adding_check = False
transaction_for_user = tuple(transaction_history)
file_output_path = os.path.join(os.getcwd(), "transactions.txt")
with open(file_output_path, 'r+') as output_file_content:
    output_file_content.write(f"Transaction history of {first_name} {last_name} \n")
    for item in transaction_for_user:
        if item == "\n":
            output_file_content.write("\n")
        else:
            output_file_content.write(str(item) + " ")
