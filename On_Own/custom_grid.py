#Create a custom grid

def make_board():
    grid = input("Give me a grid! Example '3x3' :")
    columns, _, rows = grid.partition("x")
    for _ in range(int(rows)):
        print(" --- "* int(columns))
        print("|    " * (int(columns)+1))
    print(" --- "* int(columns))
make_board()
