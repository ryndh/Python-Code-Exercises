# Sum of Pairs

# Given a list of integers and a single sum value, return the first two values (parse from the left please) in order of appearance that add up to form the sum.

# sum_pairs([4, 3, 2, 3, 4],         6)
# #          ^-----^         4 + 2 = 6, indices: 0, 2 *
# #             ^-----^      3 + 3 = 6, indices: 1, 3
# #                ^-----^   2 + 4 = 6, indices: 2, 4
# #  * entire pair is earlier, and therefore is the correct answer
# == [4, 2]

# sum_pairs([10, 5, 2, 3, 7, 5],         10)
# #              ^-----------^   5 + 5 = 10, indices: 1, 5
# #                    ^--^      3 + 7 = 10, indices: 3, 4 *
# #  * entire pair is earlier, and therefore is the correct answer
# == [3, 7]

def sum_pairs(ints, s):
    original_list = list(ints)
    working_nums = [0,0, len(ints)]
    for number in range(len(ints) - 1):
        current_num = ints.pop(0)
        for num in ints:
            if current_num + num == s:
                list_check = list(original_list)
                first = list_check.index(current_num)
                list_check.pop(first)
                second = list_check.index(num) if list_check.index(num) > first else first
                working_nums = [current_num, num, second] if second < working_nums[2] else working_nums
    print(working_nums if working_nums[2] < len(original_list) else None)

##MUCH Simpler solutions via codewars....yikes.
# def sum_pairs(nums, sum_value):
#     seen = set()
#     for num in nums:
#         diff = sum_value - num
#         if diff in seen:
#             return [diff, num]
#         seen.add(num)

# sum_pairs([10, 5, 2, 3, 7, 5], 10)
# sum_pairs([0, 0, -2, 3], 2)