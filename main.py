full_name= "John Smith"

try:
    balance = float(input("Enter the balance: "))
    expense = float(input("Enter the price: "))
    active_loan = float(input("Enter the active_loan: "))
    if expense < 0 or balance < 0 or active_loan < 0:
        print("One of the values from balance, expense or active_loan is invalid. Please check again.")
    else:
        if balance < expense:
            print(f"There is no enough founds: Your Current balance is {round(balance,2) }.Do you want to pay from active loan too?")
            user_response = input("Please enter Yes or No ")
            if user_response == "Yes" and expense - balance <= active_loan:
                active_loan_after_expense = active_loan - (expense - balance)
                print(f"Payment successfully done: Current active loan is {round(active_loan_after_expense, 2)}.")
            elif user_response == "Yes" and expense - balance > active_loan:
                print(f"Payment process was cancelled.There is no enough founds in active loan.")
            else:
                print(f"Payment process was cancelled")
        else:
            balance_after_expense = balance - expense
            print(f"Payment successfully done:Current balance is {round(balance_after_expense, 2)}")
except:
    print("Please enter the integer")



