#Three lists variant of FizzBuzz
#range of 1000
#put every 3rd into a list
#put remaining odds into list
#put remaining evens into list

def triple_lists(n):
  thirds = []
  evens = []
  odds = []
  for num in range(n):
    if num % 3 == 0:
      thirds.append(num)
    elif num % 2 == 0:
      evens.append(num)
    elif num % 2 == 1:
      odds.append(num)
  print(thirds)
  print(evens)
  print(odds)

triple_lists(100)
