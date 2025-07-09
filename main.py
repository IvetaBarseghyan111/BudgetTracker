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

count = 0
transaction_history = []

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
                    transaction_history.extend([count,'.',"Expense-",expense,"Balance after expense-",balance,"Active_loan-",active_loan,'.'])
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
                       balance = 0
                       print(f"Payment completed successfully.")
                       count += 1
                       transaction_history.extend([count,'.',"Expense-",expense,"Balance after expense-",balance,"Active_loan-",active_loan,'.'])
                   elif user_response_check and (balance == 0 and active_loan == 0):
                       print(f"There are no available funds in your balance and active loan.")
                       break
                   elif user_response == "yes" and expense - balance > active_loan:
                       print(f"Not enough active loan. You can enter expense smaller then {active_loan}")
                       count += 1
                       balance = 0
                       transaction_history.extend([count, '.', "Expense-", expense, "Balance after expense-", balance, "Active_loan-",
                            active_loan,"Transaction was cancelled"'.'])
                       continue
                   else:
                       print(f"Payment cancelled by user")
                       break
            else:
                print("Expense must be greater than zero.")
                continue
            new_expense = input("Do you want to enter another expense.Please add Yes or No ").strip().lower()
            if new_expense == "yes":
                condition_check = True
            else:
                condition_check = False


except ValueError:
    print("Invalid input. Please enter a valid number")


transaction_history_for_user = []

for num in  transaction_history:
    transaction_history_for_user.append(str(num))

print(" ".join(transaction_history_for_user))







