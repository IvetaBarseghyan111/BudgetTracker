import logging
import conditionCheckModule
import fileModifierModule

logging.basicConfig(filename = "logsFile",
                    filemode = "w",
                    level = logging.DEBUG,
                    format = '%(levelname)s - %(message)s - %(asctime)s ')


# Class of PersonBudget with attributes, constructor, class and static methods
class PersonBudget:
    transaction_history = [] # Creation empty list in which should be added user's transaction info
    count = 0  # Creation of count variable which will be used in transaction ID it will be increased every time,when
    # user will do new purchase
    def __init__(self,customer_first_name,customer_last_name):
        self.customer_first_name = customer_first_name
        self.customer_last_name = customer_last_name
    def set_balance(self, customer_balance):
        self.__customer_balance = customer_balance
    def set_loan(self, customer_active_loan):
        self.__customer_active_loan = customer_active_loan
    def get_balance(self):
        return self.__customer_balance
    def get_loan(self):
        return self.__customer_active_loan
    @classmethod
    # This function adds all necessary info of user purchase. This will show user's transaction history
    def set_transaction_list_extending(cls, customer_first_name,customer_last_name, customer_expense,
                                       customer_balance, customer_active_loan):
            cls.transaction_history.extend(["\n",customer_first_name,customer_last_name,str(customer_info.count),
                                            "Expense-",customer_expense, "Balance after expense-", customer_balance,
                                            "Active loan-", customer_active_loan])
    @classmethod
    def get_transaction_list_extending(cls):
        return cls.transaction_history

    @staticmethod #Statc method for validations of first and last name
    def user_personal_info_validation(personal_info, max_validation):
        while True: #First and last name saving loop
            value = (input(f"Enter your {personal_info}:  ").strip().title())
            if not value or value.isspace():
                print(f"{personal_info.title()} cannot be empty or just spaces. Try again.")
                logging.warning(f"{personal_info.title()} consist of spaces or empty")
                continue
            elif len(value) > 30:
                print(f"{personal_info.title()} cannot exceed {max_validation} characters.")
                logging.warning(f"{personal_info.title()} is more then 30 chars")
                continue
            else:
                print(f"{personal_info.title()} saved successfully.")
                logging.info(f"{personal_info.title()} saved successfully.")
                return value

    @staticmethod #Statc method for validations of balance and active loan
    def finance_info_validation(finance_data):
        while True:
            value = input(f"Enter your {finance_data} amount: ")
            if value.isdigit():
                value = float(value)
                print(f"{finance_data} saved successfully.")
                logging.info(f"{finance_data} saved successfully")
                return value
            else:
                print(f"Invalid input. {finance_data}must be a number.")
                logging.warning(f"Invalid input of {finance_data}")
                continue


#By this file appending files all content is deleted before new data adding into file
with open("transactions.txt", "a+") as file:
    file.seek(0)
    file.truncate(0)


while conditionCheckModule.ConditionCheckClass.expense_adding_check:#While loop of how user should add first,last name,
    # balance and loan 1.From file 2.Manually inputting
    expense_adding_condition = input("Do you want to enter your balance and loan manually? Type yes or no: ").strip().lower()
    if expense_adding_condition == "yes":
        first_name = PersonBudget.user_personal_info_validation("first name", 30)#User's first
        # name assign
        last_name = PersonBudget.user_personal_info_validation("last name", 70)#User's last name
        #assign
        customer_info = PersonBudget(first_name, last_name) # PersonBudget class calling with two parameters
        balance = PersonBudget.finance_info_validation("balance") # User's balance value assign
        customer_info.set_balance(balance) #Users balance value set to class setter method of balance
        active_loan = PersonBudget.finance_info_validation("active loan")# User's active loan value assign
        customer_info.set_loan(active_loan) #Users active loan value set to class setter method of active loan
        conditionCheckModule.condition_and_user_response() #After all necessary info submitting start of price
        # inputting. Logic of expense adding should work
    elif expense_adding_condition == "no": #After this line user's first/last name, balance and loan values should be
        # extracted from customerData file
        try:
            fileModifierModule.customer_data_reading() #All actions of customer data imported from fileModifierModule
            user_info = fileModifierModule.file_lines.split(',')#By this line string in customerData was split and returned
            # as list
            user_info_values =[]
            for pair in user_info: # For loop which split each value of user_info list and add it to new
                # user_info_values list
                value = pair.split('=')[1]
                user_info_values.append(value)
            #Code below this line, extract value of specified index and assigns it to specified variables
            first_name = user_info_values[0]
            last_name =  user_info_values[1]
            balance = float(user_info_values[2])
            active_loan = float(user_info_values[3])
            conditionCheckModule.ConditionCheckClass.expense_adding_check = False
            conditionCheckModule.condition_and_user_response() ###Check
        except FileNotFoundError: # Handling of not found customer data file
            print("File was not found")
            logging.warning("File of customer data reading was not found")
            continue
        except PermissionError: #Handling of access permission of customer data file
            print("No permission to access the file.")
            logging.warning("No permission to access the customer data reading file")
            continue
        else:
            print("Data loaded successfully from current file")
            logging.info("Data successfully loaded from customer data reading file")
    elif expense_adding_condition not in ["yes", "no"]:#Logic of when user do not answer with correct option of
        # how should be added user's info from file of manually
        print("Invalid input. Please type yes or no.")
        logging.warning("Invalid input of how user's data should be added from file or manually")
        continue
    while conditionCheckModule.ConditionCheckClass.condition_check: #Logic of expense adding
        expense = input("Enter the expense amount: ")
        if expense.isdigit() and float(expense) > 0:
            expense = float(expense)
            if customer_info.get_balance() >= expense:
                customer_info.count += 1
                customer_info.set_balance(customer_info.get_balance() - expense)
                customer_info.set_transaction_list_extending(customer_info.customer_first_name,
                                                             customer_info.customer_last_name,
                                                             str(expense),str(customer_info.get_balance()),
                                                                              str(customer_info.get_loan()))

                fileModifierModule.transaction_history_adding_into_file(customer_info.customer_first_name,
                                                                        customer_info.customer_last_name,
                                                                        customer_info.count,
                                                                        expense,
                                                                        customer_info.get_balance(),
                                                                        active_loan)
                print(f"Payment completed successfully.") #After purchase done, increment count by 1 and add it in
                # transaction_history list
                logging.info("Payment completed successfully")
            else:
                user_response = (input(f"Insufficient balance. Do you want to use your loan to cover the remaining amount?"
                                       f" (yes/no):  " ).strip().lower())
                if user_response == "yes" and expense - customer_info.get_balance() <= customer_info.get_loan():
                    #Logic of payment completion from balance and active loan, new values assigning to balance and active loan
                    customer_info.set_loan(customer_info.get_loan() - (expense - customer_info.get_balance()))
                    customer_info.set_balance(0)
                    customer_info.count += 1
                    customer_info.set_transaction_list_extending(customer_info.customer_first_name,
                                                                 customer_info.customer_last_name,
                                                                 str(expense), str(customer_info.get_balance()),
                                                                 str(customer_info.get_loan()))

                    fileModifierModule.transaction_history_adding_into_file(customer_info.customer_first_name,
                                                                            customer_info.customer_last_name,
                                                                            customer_info.count,
                                                                            expense,customer_info.get_balance(),
                                                                            customer_info.get_loan())
                    print(f"Payment completed successfully.")
                    logging.info("Payment completed successfully")
                elif user_response == "yes" and (customer_info.get_balance() == 0 and customer_info.get_loan() == 0):
                              #Logic of balance and active loan amount when they are 0
                    print(f"You have no funds left in balance or loan.")
                    logging.info("User does not have funds in balance or loan")
                    conditionCheckModule.ConditionCheckClass.expense_adding_check = False
                    break
                elif user_response == "yes"  and expense - customer_info.get_balance() > customer_info.get_loan(): #Logic
                    # of active loan and entered price checking, when active loan < price , user should input new price
                    print(f"Not enough active loan. Your current active loan is {customer_info.get_loan()}")
                    logging.info("Not enough funds in active loan")
                    continue
                else: #Logic of payment cancelled by user, when user type no for payment from active loan
                    conditionCheckModule.ConditionCheckClass.expense_adding_check = False
                    break
        else:
            print("Invalid amount. Expense must be greater then 0.") #Expense validation check
            logging.warning("Expense must be greater than 0")
            continue
        new_expense = input("Do you want to enter another expense.Please enter Yes or No ").strip().lower()
        conditionCheckModule.user_response_check_function(new_expense)

    transaction_for_user = tuple(customer_info.get_transaction_list_extending())
    print(" ".join(transaction_for_user))


