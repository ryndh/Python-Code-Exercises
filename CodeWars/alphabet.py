#Alphabet as numbers. 
#Print out a string as numbers corresponding to letter spot in alphabet. 
# def alphabet_position(text):
#     alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
#     new_string = ''
#     for letter in text:
#         if letter.isalpha():
#             alpha_val = str(alphabet.index(letter.lower()) +1)
#             new_string += alpha_val + " "
#     final = new_string.strip()
#     return final

# print(alphabet_position("Hello!"))

#Best way of implementing:
def alphabet_position(text):
    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())
