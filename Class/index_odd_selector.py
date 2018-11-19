
#Create program that returns index item of list
tags= ['stuff', 'more stuff', 'computers', 'coding', 'programming', 'developer', 'data'
def finder(li, element):
    index_num = li.index(element)
    print(index_num)

finder(tags, 'computers')


#Return random item from list
import random 

def randomizer(li):
    print(random.choice(li))

randomizer(tags)


#Create Program that returns odd items from a list. 
odd = [0, 1, 2, 3, 5, 7, 8, 9, 10]

def odd_selector(li):
    for x in li:
        if x % 2 == 1:
            print(x)

odd_selector(odd)