# Given two arrays a and b write a function comp(a, b) (compSame(a, b) in Clojure) that checks whether the two arrays have the "same" elements, with the same multiplicities. "Same" means, here, that the elements in b are the elements in a squared, regardless of the orde

# a1 = [121, 144, 19, 161, 19, 144, 19, 11]
# a2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]

def comp(array1, array2):
    if array1 == None or array2 == None:
        return False
    elif len(array1) + len(array2) == 0: 
        return True
    else:
        if len(set(array1)) == len(set(array2)):
            for number in array1:
                if number ** 2 not in array2:
                    return False 
            return True
        else:
            return False

#Better solution via Codewars:

# def comp(array1, array2):
#     try:
#         return sorted([i ** 2 for i in array1]) == sorted(array2)
#     except:
#         return False

# Totally forgot about list equality in python while doing this...
# Was treating it like arrays in JS...