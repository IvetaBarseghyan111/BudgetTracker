import logging
import json
import os

# Class of PersonBudget with attributes, constructor, class and static methods
class PersonBudget:
    def __init__(self, customer_first_name, customer_last_name, customer_balance, customer_active_loan):
        self.customer_first_name = customer_first_name
        self.customer_last_name = customer_last_name
        self._customer_balance = customer_balance
        self._customer_active_loan = customer_active_loan
        self._transaction_history = [] #Empty list of transaction history
        self._count = 0 #Variable which will be used in transaction ID it will be increased every time,when
        # user will do new purchase

    def get_balance(self):
        return self._customer_balance

    def get_loan(self):
        return self._customer_active_loan

    def fund_calculator(self, customer_expense, include_loan=False):
        if customer_expense <= self._customer_balance:
            self._customer_balance -= customer_expense
            return True
        elif include_loan and customer_expense <= (self._customer_balance + self._customer_active_loan):
            self._customer_active_loan = self._customer_active_loan - (customer_expense - self._customer_balance)
            self._customer_balance = 0
            return True
        else:
            return False

    # Adds all necessary info of user purchase. This will show in user's transaction history
    def set_transaction_list_extending(self, customer_expense):
        self._count += 1
        self._transaction_history.extend([
            {
                'First Name': self.customer_first_name,
                'Last Name': self.customer_last_name,
                'ID': self._count,
                'Expense': customer_expense,
                'Balance After': self._customer_balance,
                'Active Loan After': self._customer_active_loan,
               }
        ])

    def get_transaction_list(self):
        return self._transaction_history

    # Adds all necessary info of user purchase. This will show in user's transaction history
    def transaction_history_adding_into_file(self, customer_expense):
        file_output_path = os.path.join(os.getcwd(), "transactions.txt")
        with open(file_output_path, 'a') as output_file_content:
            output_file_content.write(f"{
                {
                    'First Name': self.customer_first_name,
                    'Last Name': self.customer_last_name,
                    'ID': self._count,
                    'Expense': customer_expense,
                    'Balance After': self._customer_balance,
                    'Active Loan After': self._customer_active_loan,
                }
            } \n")

    def transaction_history_adding_into_json(self, customer_expense):
        pass

    @staticmethod  # Static method for validations of first and last name
    def user_personal_info_validation( personal_info, max_validation):
        while True:  # First and last name saving loop
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

    @staticmethod  #Static method for validations of balance and active loan
    def finance_info_validation(finance_data):
        while True:
            value = input(f"Enter your {finance_data} amount: ")
            try:
                value = float(value)
                print(f"{finance_data} saved successfully.")
                logging.info(f"{finance_data} saved successfully")
                return value
            except ValueError:
                print(f"Invalid input. {finance_data}must be a number.")
                logging.warning(f"Invalid input of {finance_data}")



class OnlineBudget(PersonBudget):
    def __init__(self,customer_first_name, customer_last_name, customer_balance, customer_active_loan, online_loan):
        super().__init__(customer_first_name, customer_last_name, customer_balance, customer_active_loan)
        self._online_loan = online_loan

    def get_online_loan(self):
        return self._online_loan

    def fund_calculator(self, customer_expense, include_loan=False, include_online_loan = False):
        if customer_expense <= self._customer_balance:
            self._customer_balance -= customer_expense
            return True
        elif include_loan and customer_expense <= (self._customer_balance + self._customer_active_loan):
            self._customer_active_loan = self._customer_active_loan - (customer_expense - self._customer_balance)
            self._customer_balance = 0
            return True
        elif include_online_loan and customer_expense <= (self._customer_balance + self._customer_active_loan +
                                                          self._online_loan):
            self._online_loan = self._online_loan - (customer_expense - self._customer_balance -
                                                     self._customer_active_loan)
            self._customer_balance = 0
            self._customer_active_loan = 0
            return True
        else:
            return False


    # Adds all necessary info of user purchase. This will show in user's transaction history
    def set_transaction_list_extending(self, customer_expense):
        self._count += 1
        self._transaction_history.extend([
            {
                'First Name': self.customer_first_name,
                'Last Name': self.customer_last_name,
                'ID': self._count,
                'Expense': customer_expense,
                'Balance After': self._customer_balance,
                'Active Loan After': self._customer_active_loan,
                'Online Loan After': self._online_loan,
            }
        ])

    # Adds all necessary info of user purchase. This will show in user's transaction history
    def transaction_history_adding_into_file(self, customer_expense):
        file_output_path = os.path.join(os.getcwd(), "transactions.txt")
        with open(file_output_path, 'a') as output_file_content:
            output_file_content.write(f"{
                {
                    'First Name': self.customer_first_name,
                    'Last Name': self.customer_last_name,
                    'ID': self._count,
                    'Expense': customer_expense,
                    'Balance After': self._customer_balance,
                    'Active Loan After': self._customer_active_loan,
                    'Online Loan After': self._online_loan,
                }
            } \n")

    def transaction_history_adding_into_json(self, customer_expense):
        pass
