#Build a manual exponent machine

#Iterative version
def manual_exponent(num, exp):
    i = 1
    num1 = num
    while exp > i:
        num1 *= num
        i += 1
    print(num1)


manual_exponent(2, 4)
print(2**4)

#Functional Approach
#Reduce Function
from functools import reduce

def manual_exponent(num, exp):
    computed_list = [num] * exp
    return (reduce(lambda total, element: total * element, computed_list))

#How the lamda/reduce logic works. Lambda is an anonymous function that takes in arguments but give only 1 expression. It's like doing:
def lambda(total, element):
    return total * element

#Reduce takes in a function as one of it's arguments, then also takes in a list. It saves a result from one iteration then continues going over the list until it has exhausted the list, 'reducing' everything into 1 value. 
