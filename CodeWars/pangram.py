import string

def is_pangram(s):
    check = set(s.lower())
    final = []
    for let in check:
        if let.isalpha():
            final.append(let.lower())
    final.sort()
    verify = "".join(final)
    letters = string.ascii_lowercase
    if verify == letters:
        return True
    else:
        return False