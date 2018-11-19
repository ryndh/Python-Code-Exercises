#Jordan's solution

import operator
from functools import reduce

def dynamic_reducer(chicken, op):
    operators = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,
    }

    return reduce((lambda total, element: operators[op](total, element)), chicken)



total = dynamic_reducer([1, 2, 3], '+') 

print(total)
