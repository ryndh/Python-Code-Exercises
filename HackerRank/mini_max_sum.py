# Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.
# For example, . Our minimum sum is  and our maximum sum is . We would print
# 16 24
# Function Description
# Complete the miniMaxSum function in the editor below. It should print two space-separated integers on one line: the minimum sum and the maximum sum of  of  elements.
# miniMaxSum has the following parameter(s):
# arr: an array of  integers
# Input Format
# A single line of five space-separated integers.
# Constraints

# Output Format
# Print two space-separated long integers denoting the respective minimum and maximum values that can be calculated by summing exactly four of the five integers. (The output can be greater than a 32 bit integer.)
# Sample Input
# 1 2 3 4 5
# Sample Output
# 10 14

def miniMaxSum(arr):
    max = 0
    min = sum(arr)
    for i in range(len(arr)):
        value = sum(arr) - arr[i]
        print(value)
        if value > max:
            max = value
        if value < min:
            min = value
    print(str(min) + ' ' + str(max))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
