
# def pretty_price(value, option):
#     start = str(math.floor(value))
#     newoption = str(option)
#     add_me = newoption[-2:]
#     final = start + "." + add_me
#     print(final)

# pretty_price(1.20, .09)

def simpler(value, option):
    return float(".".join([str(int(value)), str(option)[-2:]]))

print(simpler(3.209, .99))

#Jordan's solution
# def pretty_price(gross_price, extension):
#     if isinstance(extension, int):
#         extension = extension * 0.01

#     return int(gross_price) + extension

# print(pretty_price(3.20, 99))
# print(pretty_price(3.99, 0.20))
# print(pretty_price(3.20, .95))
# print(pretty_price(3, 95))
# print(pretty_price(3, 2))