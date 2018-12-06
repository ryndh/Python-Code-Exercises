#find number with most digits in an array


def find_longest(arr):
    longest = 1
    for el in arr: 
        if len(str(el)) > len(str(longest)):
            longest = el
    return longest 

print(find_longest([1,100,2,3001,5]))

#Simpler solution from codewars:
# def find_longest(xs):
#     return max(xs, key=lambda x: len(str(x)))