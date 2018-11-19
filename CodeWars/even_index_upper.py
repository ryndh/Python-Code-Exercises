#Make even indexes in a word uppercase
def to_weird_case(string):
    new = string.split()
    final = []
    for word in new:
        working = list(word)
        for idx, letter in enumerate(working):
            if idx % 2 == 0:
                working[idx]=letter.upper()
            words = ''.join(working)
        final.append(words)
    return " ".join(final)
            

print(to_weird_case("hello there"))

#Better solution...
def to_weird_case_word(string):
    return "".join(c.upper() if i%2 == 0 else c for i, c in enumerate(string.lower()))