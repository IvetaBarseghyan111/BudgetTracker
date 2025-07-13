count = 0
transaction_history = []

def transaction_list_extending():
   transaction_history.extend(["\n", str(count), '.', "Expense-", str(expense), "Balance after expense-", str(balance), "Active_loan-",
    str(active_loan)])

while True:
    user_name = input("Please enter username:  ")
    if not  user_name or user_name.isspace():
        print("Please provide valid username")
        continue
    elif len(user_name) > 30:
        print("Username max length can not exceed 30 characters")
        continue
    else:
        print("Username was successfully saved")
        break

try:
    balance = float(input("Enter the balance: "))
    active_loan = float(input("Enter the active_loan: "))
    condition_check = True
    user_response_check = True

    if balance < 0 or active_loan < 0:
        print("One of the values from balance or active_loan is invalid. Please check again.")
    else:
        while condition_check:
            expense = float(input("Enter the price: "))
            if expense > 0:
                if balance >= expense:
                    count += 1
                    balance -= expense
                    transaction_list_extending()
                    print(f"Payment completed successfully.")
                else:
                   print(f"Not enough balance. Do you want to cover the remaining amount from your active loan?")
                   user_response = input("Please enter Yes or No ").strip().lower()
                   if user_response == "yes":
                       user_response_check = True
                   else:
                       user_response_check = False

                   if user_response_check and expense - balance <= active_loan:
                       active_loan -= (expense - balance)
                       print(f"Payment completed successfully.")
                       balance = 0
                       count += 1
                       transaction_list_extending()
                   elif user_response_check and (balance == 0 and active_loan == 0):
                       print(f"There are no available funds in your balance and active loan.")
                       break
                   elif user_response == "yes" and expense - balance > active_loan:
                       print(f"Not enough active loan. Your current active loan is {active_loan}")
                       count += 1
                       transaction_list_extending()
                       transaction_history.append("Not enough funds")
                       continue
                   else:
                       print(f"Payment cancelled by user")
                       break
            else:
                print("Expense must be greater than zero.")
                continue
            new_expense = input("Do you want to enter another expense.Please enter Yes or No ").strip().lower()
            if new_expense == "yes":
                condition_check = True
            else:
                condition_check = False

    transaction_for_user = tuple(transaction_history)
    print(f"Transaction history of {user_name}")
    print(" ".join(transaction_history))

except ValueError:
    print("Invalid input. Please enter a valid number")


