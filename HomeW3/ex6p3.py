#

user_answer = input("Please, input your word:").lower()
def int_func(word):
    word = list(word)
    new_list = []
    new_list.append(word[0])
    new_list = str(new_list).upper()
    new_list = list(new_list)
    word.insert(0, new_list[2])
    word.pop(1)
    word = "".join(word)
    return word
print(int_func(user_answer))

