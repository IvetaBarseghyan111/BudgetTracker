import logging
import conditionCheckModule
import fileModifierModule
from personBudgetClass import OnlineBudget

logging.basicConfig(filename="logsFile",
                    filemode="w",
                    level=logging.DEBUG,
                    format='%(levelname)s - %(message)s - %(asctime)s ')


# By this file appending files all content is deleted before new data adding into file
fileModifierModule.file_previous_data_deleting()

while conditionCheckModule.ConditionCheckClass.user_data_adding_check: #While loop of how customer info should be added
    expense_adding_condition = (input("How do you want to add customer info 1.Manually 2.From text file 3.From JSON file: ")
                                .strip().lower())

    if expense_adding_condition == "manually":
        #User's firs_name, last_nae,balance, active_loan values assigning after personBudget class @staticmethod
        #validations passing
        first_name = OnlineBudget.user_personal_info_validation("first name", 30)
        last_name = OnlineBudget.user_personal_info_validation("last name", 70)
        balance = OnlineBudget.finance_info_validation("balance")
        active_loan = OnlineBudget.finance_info_validation("active loan")
        online_loan = OnlineBudget.finance_info_validation("online loan")
        customer_info = OnlineBudget(first_name, last_name, balance, active_loan, online_loan) #OnlineBudget class
        # calling with
        # two parameters
        conditionCheckModule.ConditionCheckClass.condition_and_user_response() #After all necessary info submitting
        # start of price inputting. Logic of expense adding should work

    elif expense_adding_condition == "text file":  # After this line user's first/last name, balance and loan values
        # should be extracted from customerData file

        #Customer info assigning from file
        first_name, last_name, balance, active_loan, online_loan \
            = fileModifierModule.customer_data_reading_and_assigning_from_file()

        # Creation of customer info object when data is from file
        customer_info = OnlineBudget(first_name, last_name, balance, active_loan, online_loan)

        conditionCheckModule.ConditionCheckClass.user_data_adding_check = False
        conditionCheckModule.ConditionCheckClass.condition_and_user_response()

    elif expense_adding_condition == "json":
        pass

    elif expense_adding_condition not in ["manually", "text file", "json"]:  # Logic of when user do not answer with
        # correct  option of how should be added user's info
        print("Invalid input. Please type yes or no.")
        logging.warning("Invalid input of how user's data should be added from file or manually")
        continue

    while conditionCheckModule.ConditionCheckClass.condition_check:  # Logic of expense adding
        expense = input("Enter the expense amount: ")

        if customer_info.get_balance() == 0 and customer_info.get_loan() == 0 and customer_info.get_online_loan() == 0:
            # Logic of balance and active loan amount when they are 0
            print(f"You have no funds left in balance or loan.")
            logging.info("User does not have funds in balance or loan")
            conditionCheckModule.ConditionCheckClass.user_data_adding_check = False
            break

        if expense.isdigit() and float(expense) > 0:
            expense = float(expense)

            if customer_info.fund_calculator(expense):
                print(f"Payment completed successfully.")  # After purchase done,all info added to transaction_history list
                # and into transactions.txt file
                logging.info("Payment completed successfully")
            else:
                user_response = (
                    input(f"Insufficient balance. Do you want to use your loan to cover the remaining amount?"
                          f" (yes/no):  ").strip().lower())
                if user_response == "yes":
                    if customer_info.fund_calculator(expense, True):
                        print(f"Payment completed successfully.")
                        logging.info("Payment completed successfully")
                    else:
                        user_response = (input(f"Insufficient Active Loan. Do you want to use your online loan to "
                                               f"cover the remaining amount?" f" (yes/no):  ").strip().lower())
                        if user_response == "yes":
                            if customer_info.fund_calculator(expense, True, True):
                                print(f"Payment completed successfully.")
                                logging.info("Payment completed successfully")
                            else:
                                print(f"Not enough active loan and online loan. Your current active loan is"
                                      f" {customer_info.get_loan()}, your current online loan is"
                                      f" {customer_info.get_online_loan()}")
                                logging.info("Not enough funds in active loan and online loan")
                                continue

                else:  # Logic of payment cancelled by user, when user type no for payment from active loan
                    conditionCheckModule.ConditionCheckClass.user_data_adding_check = False
                    break
        else:
            print("Invalid amount. Expense must be greater then 0.")  # Expense validation check
            logging.warning("Expense must be greater than 0")
            continue

        customer_info.set_transaction_list_extending(expense)
        customer_info.transaction_history_adding_into_file(expense)

        conditionCheckModule.ConditionCheckClass.user_response_check_function()

    print(customer_info.get_transaction_list()) #Transaction history displaying

