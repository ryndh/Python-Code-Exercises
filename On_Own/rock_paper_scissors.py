
def rocker():
    while True:
        print("Let's play Rock, Paper, Scissors!!!")
        p1_choice = input("Player 1 choice: ")
        p2_choice = input("Player 2 choice: ")
        if (p1_choice.lower() == "rock" or p1_choice.lower() =="paper" or p1_choice.lower() =="scissors") and (p2_choice.lower() == "rock" or p2_choice.lower() =="paper" or p2_choice.lower() =="scissors"):
            winner_one = f"Player ONE is the winner! {p1_choice} was a good choice!"
            winner_two = f"Player TWO is the winner! {p2_choice} was a good choice!"
            if p1_choice.lower() == p2_choice.lower():
                print("It's a tie! Try again")
                continue
            elif p1_choice.lower() == "rock" and p2_choice.lower() == "scissors":
                print(winner_one)
            elif p1_choice.lower() == "paper" and p2_choice.lower() == "rock":
                print(winner_one)
            elif p1_choice.lower() == "scissors" and p2_choice.lower() == "paper":
                print(winner_one)
            elif p1_choice.lower() == "rock" and p2_choice.lower() == "paper":
                print(winner_two)
            elif p1_choice.lower() == "paper" and p2_choice.lower() == "scissors":
                print(winner_two)
            elif p1_choice.lower() == "scissors" and p2_choice.lower() == "rock":
                print(winner_two)
            start_over = input("Do you want to play again? y/n?: ")
            if start_over.lower() == "y":
                continue
            else:
                return False
        else:
            print("You need to choose 'rock', 'paper', or 'scissors'")
rocker()

#======================================================================================================
#Other possible solution listed on site:

# print('''Please pick one:
#             rock
#             scissors
#             paper''')

# while True:
#     game_dict = {'rock': 1, 'scissors': 2, 'paper': 3}
#     player_a = str(input("Player a: "))
#     player_b = str(input("Player b: "))
#     a = game_dict.get(player_a)
#     b = game_dict.get(player_b)
#     dif = a - b

#     if dif in [-1, 2]:
#         print('player a wins.')
#         if str(input('Do you want to play another game, yes or no?\n')) == 'yes':
#             continue
#         else:
#             print('game over.')
#             break
#     elif dif in [-2, 1]:
#         print('player b wins.')
#         if str(input('Do you want to play another game, yes or no?\n')) == 'yes':
#             continue
#         else:
#             print('game over.')
#             break
#     else:
#         print('Draw.Please continue.')
#         print('')
