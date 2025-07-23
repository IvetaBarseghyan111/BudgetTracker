count = 0 #Creation of count variable which will be used in transaction ID (it will be increased every time,
# when user will do new purchase)
transaction_history = [] #Creation empty list in which should be added user's every transaction info

#Function creation of transaction history adding every time user do new purchase
def transaction_list_extending():
   transaction_history.extend(["\n", user_name,"-",str(count), ',', "Expense-", str(expense),",","Balance after expense-",
                               str(balance),",", "Active_loan-", str(active_loan)])

while True: #Username saving loop
    user_name = input("Please enter username:  ").strip().title()
    if not user_name or user_name.isspace():
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

    if balance < 0 or active_loan < 0: #Check balance and active loan are not 0
        print("One of the values from balance or active_loan is invalid. Please check again.")
    else:
        while condition_check:
            expense = float(input("Enter the price: "))
            if expense > 0:
                if balance >= expense:
                    count += 1
                    balance -= expense
                    transaction_list_extending()
                    print(f"Payment completed successfully.") #After purchase done, increment count by 1 and add it
                    # in transaction_history list
                else:
                   user_response = input(f"Not enough balance. Do you want to cover the remaining amount from your "
                                         f"active loan? Please enter Yes or No ").strip().lower()
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
                       print(f"There are no available funds in your balance and active loan.")
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
                print("Expense must be greater than zero.")
                continue
            new_expense = input("Do you want to enter another expense.Please enter Yes or No ").strip().lower()
            if new_expense == "yes":
                condition_check = True
            else:
                condition_check = False

    transaction_for_user = tuple(transaction_history)#Logic of transaction_history data type changing
    print(f"Transaction history of {user_name}")
    print(" ".join(transaction_for_user)) #Logic of transaction history printing changes more user-friendly

except ValueError:
    print("Invalid input. Please enter a valid number")