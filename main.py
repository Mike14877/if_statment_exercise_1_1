
def back():
    answer = input("Do you wanna continue ? 'Yes' Or 'No' : ")
    get_answer = answer.lower()
    if get_answer == "yes" or get_answer == "y":
        return compare_number()
    else :
        back_to_compare = input("Enter 'COMPARE to return the function ")
        if back_to_compare == "COMPARE":
            return compare_number()
        else :
            return back()
    # print((get_answer))


def compare_number():
    num_1 = int(input("Please Enter the 1st Number : "))
    num_2 = int(input("Please Enter the 2nd Number : "))
    if num_1 == num_2:
        print("The 1st and 2nd number are equal")
        return back()
    elif num_1 > num_2:
        print("The 1st number is greater 2nd number")
        return back()
    elif num_1 < num_2:
        print("The 1st number is less 2nd number")
        return back()


compare_number()
