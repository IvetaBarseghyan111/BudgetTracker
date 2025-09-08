class ConditionCheckClass:
    user_data_adding_check = True
    condition_check = True

    @classmethod
    def condition_and_user_response(cls):
        ConditionCheckClass.condition_check = True

    @classmethod
    #By this function checks if user wants to add new expense or not
    def user_response_check_function(cls, condition_value = True):
        while True:
            condition_value = input("Do you want to enter another expense.Please enter Yes or No ").strip().lower()
            if condition_value == "yes":
                cls.condition_check = True
                cls.user_data_adding_check = True
                break
            elif condition_value not in ["yes", "no"]:
                print("Please answer with Yes or No")
                continue
            else:
                cls.condition_check = False
                cls.user_data_adding_check = False
                break

