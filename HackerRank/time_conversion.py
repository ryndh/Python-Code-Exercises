# Given a time in -hour AM/PM format, convert it to military (24-hour) time.
# Note: Midnight is 12:00:00AM on a 12-hour clock, and 00:00:00 on a 24-hour clock. Noon is 12:00:00PM on a 12-hour clock, and 12:00:00 on a 24-hour clock.
# Function Description
# Complete the timeConversion function in the editor below. It should return a new string representing the input time in 24 hour format.
# timeConversion has the following parameter(s):
# s: a string representing time in  hour format
# Input Format
# A single string  containing a time in -hour clock format (i.e.:  or ), where  and .
# Constraints
# All input times are valid
# Output Format
# Convert and print the given time in -hour format, where .
# Sample Input 0
# 07:05:45PM
# Sample Output 0
# 19:05:45

def timeConversion(s):
    if s[-2:] == 'PM':
        if s[0:2] == '12':
            return s[:-2]
        else:
            return str(int(s[0:2]) + 12) + s[2:-2]
    else:
        if s[0:2] == '12':
            return '00' + s[2:-2]
        else:
            return s[:-2]

if __name__ == '__main__':

    s = input()

    print(timeConversion(s))
