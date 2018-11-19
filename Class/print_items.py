points = {
    "steph": 51,
    "klay" : 52,
    "KD"   : 41,
}

# print("S " + points["steph"]* "$")
# print("K " + points["klay"]* "$")
# print("KD " + points["KD"]* "$")

def printer(library):
    for key in library:
        print(key[0] + library[key] * "$")

printer(points)