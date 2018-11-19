#Binary number generated from list of 1's and 0's
# def binary(some_list):
#     reversed = some_list[::-1]
#     counter = 0
#     total = 0
#     for number in reversed:
#         if number == 1:
#             total += (2 ** counter)
#         counter += 1
#     return(total)



# binary([1,0,1,0])

#Best way to solve.
def binary_array_to_number(arr):
  return int("".join(map(str, arr)), 2)

print(binary_array_to_number([1,0,0,1,1]))
