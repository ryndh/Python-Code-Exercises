#matrix incrementing exercise
def manual_incrementing_matrix(n):
  matrix= [ [ None for y in range(n)]for x in range(n) ]

  counter = 0 

  for id, el in enumerate(matrix):
    for nested_idx, nested_el in enumerate(el):
      matrix[id][nested_idx] = counter + nested_idx

    counter += 1

  return matrix

print(manual_incrementing_matrix(4))