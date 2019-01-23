# In this simple Kata your task is to create a function that turns a string into a Wave. You will be passed a string and you must return that string in an array where an uppercase letter is a person standing up.

def wave(str):
    some_arr = []
    for num in range(len(str)):
        if str[num].isalpha():
            some_arr.append(str[:num] + str[num].upper() + str[num + 1:])
    print(some_arr)

wave("hello there ")


# Simpler solution via codewars:
# def wave(str):
#     return [str[:i] + str[i].upper() + str[i+1:] for i in range(len(str)) if str[i].isalpha()]