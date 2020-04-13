#--------------------------------------Version1-------------------------------------------------------------------------
the_list = []
"""
while True:
    user_answer = input("Input numbers with space:").split(" ")
    if user_answer == ["$"]:
        print(sum(the_list))
        break


    elif "$" in user_answer:
        is_enter = input("Press Enter to continue")
        for i, item in enumerate(user_answer[:user_answer.index("$")]):
            user_answer[i] = int(item)
        total = sum(user_answer[:user_answer.index("$")])
        the_list.append(total)
     else:
        is_enter = input("Press Enter to continue")
        for i, item in enumerate(user_answer):
            user_answer[i] = int(item)
        total = sum(user_answer)
        the_list.append(total)
    print(sum(the_list))
    """
#--------------------------------------------------Version2-------------------------------------------------------------
def integer(inputin):
    for i, item in enumerate(inputin):
        inputin[i] = int(item)
the_list = []
while True:
    user_answer = input("Input numbers with space:").split(" ")
    if user_answer == ["$"]:
        print(sum(the_list))
        break

    elif "$" in user_answer:
        is_enter = input("Press Enter to continue")
        integer(user_answer)
        total = sum(user_answer[:user_answer.index("$")])
        the_list.append(total)
    else:
        is_enter = input("Press Enter to continue")
        integer(user_answer)
        total = sum(user_answer)
        the_list.append(total)
    print(sum(the_list))















