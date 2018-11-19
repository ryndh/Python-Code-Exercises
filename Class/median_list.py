#FIND MEDIAN OF A LIST

#Tools:
#Math Library
#Sorted Function
#List Slicing
#Computations


sale_prices = [
  100,
  83,
  220,
  40,
  100,
  400,
  10,
  1,
  3
]


import math

def sorter(li):
    length = len(li)
    almost_middle = length/2
    middle = math.ceil(almost_middle)
    sorted_list = sorted(li)
    median = sorted_list[middle - 1]


    print(median)

sorter(sale_prices)