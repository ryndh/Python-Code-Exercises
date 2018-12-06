# Given: an array containing hashes of names

# Return: a string formatted as a list of names separated by commas except for the last two names, which should be separated by an ampersand.

def namelist(names):
    other = []
    if len(names) > 1:
        for obj in names[0:-1]:
            other.append((obj['name']))
        almost =  ', '.join(other)
        return almost + f' & {list(names[-1].values())[0]}'
    elif len(names) == 1:
        return names[0]['name']
    else:
        return ''



print(namelist([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ]))

#alternative solution via codewars:
# def namelist(names):
#     if len(names) > 1:
#         return '{} & {}'.format(', '.join(name['name'] for name in names[:-1]), 
#                                 names[-1]['name'])
#     elif names:
#         return names[0]['name']
#     else:
#         return ''
