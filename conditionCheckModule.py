class ConditionCheckClass:
    condition_check = True
    expense_adding_check = True

def condition_and_user_response():
    ConditionCheckClass.condition_check = True

#By this function checks if user wants to add new expense or not
def user_response_check_function(condition_value):
    if condition_value == "yes":
        ConditionCheckClass.condition_check = True
    else:
        ConditionCheckClass.condition_check = False
        ConditionCheckClass.expense_adding_check = False
