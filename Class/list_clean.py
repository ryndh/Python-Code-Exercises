#Take in list and remove first and last items

def checker(some_list):#Bad practice, not recommended but works
    del some_list[0]
    del some_list[-1]
    print(some_list)

checker([1,2,3,4,5,6,7])

def better(something): #Better solution, but not the best. 
    new = [something[1:-1]]
    print(new)

better([1,2,3,4,5,6,7])

def unpacker(some_list): #Best solution to the problem. 
    _, *two, _ = some_list
    print(two)

unpacker([1,2,3,4,5,6,7])