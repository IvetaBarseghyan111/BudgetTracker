user_name = "John Smith"

try:
    balance = float(input("Enter the balance: "))
    active_loan = float(input("Enter the active_loan: "))
    condition_check = True

    if balance < 0 or active_loan < 0:
        print("One of the values from balance or active_loan is invalid. Please check again.")
    else:
        while condition_check:
            expense = float(input("Enter the price: "))
            if expense > 0:
                if balance >= expense:
                    balance -= expense
                    print(f"Payment successfully done: Current balance is {round(balance, 2)}")
                else:
                    print(f"There is no enough founds in current balance: Your Current balance is {round(balance, 2)}.Do you want to pay from active loan too?")
                    user_response = str.lower(input("Please enter Yes or No "))
                    if user_response == "yes" and expense - balance <= active_loan:
                        active_loan -= (expense - balance)
                        balance = 0
                        print(f"Payment successfully done: Current active loan is {round(active_loan, 2)}.")
                    elif user_response == "yes" and expense - balance > active_loan:
                        print(f"Payment process was cancelled.There is no enough founds in active loan.")
                        break
                    else:
                        print(f"Payment process was cancelled")
                        break
            else:
                print("Please add valid expense value")
                break
            new_expense = str.lower(input("Do you want to add new expense. Please add Yes or No "))
            if new_expense == "no":
                condition_check = False
except:
    print("Please add numeric value")

