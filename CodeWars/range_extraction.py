# Range Extraction
# A format for expressing an ordered list of integers is to use a comma separated list of either

# individual integers
# or a range of integers denoted by the starting integer separated from the end integer in the range by a dash, '-'. The range includes all integers in the interval including both endpoints. It is not considered a range unless it spans at least 3 numbers. For example ("12, 13, 15-17")
# Complete the solution so that it takes a list of integers in increasing order and returns a correctly formatted string in the range format.

def solution(args):
    args.sort()
    staging = [ args[0] ]
    final = []
    for n in args[1:]:
        if staging[-1] == n - 1:
            staging.append(n)
            if args[-1] == n:
                if len(staging) > 2:
                    final.append(str(staging[0]) + '-' + str(staging[-1]))
                else:
                    for item in staging:
                        final.append(str(item))
        else:
            if len(staging) > 2:
                final.append(str(staging[0]) + '-' + str(staging[-1]))
                staging = [n]
                if args[-1] == n:
                    final.append(str(n))
            else:
                for item in staging:
                    final.append(str(item))
                    staging = [n]
                if args[-1] == n:
                    final.append(str(n))

    return ','.join(final)

    




# print(solution([-3, -6, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 17, 15, 19, 18, 20]))
# # returns "-6,-3-1,3-5,7-11,14,15,17-20"

#loop over array
#decide if numbers are sequential
#if sequential and more than 3, return beginning and end with dash.
#all other numbers return normally. 
print(solution([-75,-73,-70,-68,-67,-65, -64, -63,-60,-59,-57,-54,-53,-50, -49,-48,-46,-45,-42]))


#Other solution via codewars:

# def solution(args):
#     out = []
#     beg = end = args[0]
    
#     for n in args[1:] + [""]:        
#         if n != end + 1:
#             if end == beg:
#                 out.append( str(beg) )
#             elif end == beg + 1:
#                 out.extend( [str(beg), str(end)] )
#             else:
#                 out.append( str(beg) + "-" + str(end) )
#             beg = n
#         end = n
    
#     return ",".join(out)