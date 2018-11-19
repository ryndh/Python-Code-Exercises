#One that didn't work with the score variable outside:
# def yahtzee():
#     global score #Need to declare that score is global and can be changed because it is an int, which is immutable. Lists and Dictionaries are being imported because they are mutable. 
#     roll_one_saved = []
#     roll_two_saved = []
#     roll_three_total = []
#     print("Ready to roll??\n==========")
#     while True:

import random
import sys

roll_outcomes = [1,2,3,4,5,6]
tally = {
    "ones" : None,
    "twos" : None,
    "threes" : None,
    "fours" : None,
    "fives" : None,
    "sixes" : None,
    "3 of a kind" : None,
    "4 of a kind" : None,
    "full house" : None,
    "small straight" : None,
    "large straight" : None,
    "chance" : None,
    "yahtzee" : None,
}
def yahtzee(number):
    roll_one_saved = []
    roll_two_saved = []
    roll_three_total = []
    score = number
    print("Ready to roll??\n==========")
    while True:
        if None in tally.values():
            ready = input("Type 'roll' to get going!!: ")
            if ready.lower() == 'roll':
                roll_one = {
                    "dice a" : random.choice(roll_outcomes),
                    "dice b" : random.choice(roll_outcomes),
                    "dice c" : random.choice(roll_outcomes),
                    "dice d" : random.choice(roll_outcomes),
                    "dice e" : random.choice(roll_outcomes),
                }
                for key, value in roll_one.items():
                    print(f'{key} -- {value}')   
                while True:
                    save = input("Do you want to save any dice? Enter one of the dice letters you want to save, or type 'roll two' :")
                    if save.isalpha() and len(save) == 1 and f'dice {save}' in roll_one:
                        roll_one_saved.append(roll_one.pop(f'dice {save}'))
                    elif save.lower() == "roll two":
                        print("Alright! Let's roll!!\n=======")
                        roll_two = {}
                        for n in range(5 - len(roll_one_saved)):
                            roll_two[f'dice {chr(n + 97)}'] = random.choice(roll_outcomes)
                        for key, value in roll_two.items():
                            print(f'{key} -- {value}')
                        while True:
                            save_two = input("Do you want to save any dice? Enter one of the dice letters you want to save, or type 'roll three' :")
                            if save_two.isalpha() and len(save_two) == 1 and f'dice {save_two}' in roll_two:
                                roll_two_saved.append(roll_two.pop(f'dice {save_two}'))
                            elif save_two.lower() == "roll three":
                                print("Alright! Final roll!!\n=======")
                                roll_three = {}
                                for n in range(5 - len(roll_one_saved)-len(roll_two_saved)):
                                    roll_three[f'dice {chr(n + 97)}'] = random.choice(roll_outcomes)
                                for key, value in roll_three.items():
                                    print(f'{key} -- {value}')
                                    roll_three_total.append(value)
                                final = roll_one_saved + roll_two_saved + roll_three_total
                                print(f'With your final roll, the dice numbers you have to work with are:\n {final}')
                                print("How would you like to score this?")
                                for key, value in tally.items():
                                    if value == None:
                                        print(key)
                                while True:
                                    attempt = input("Category: ")
                                    if attempt.lower() == "ones":
                                        if tally["ones"]==None:
                                            for n in final:
                                                if n == 1:
                                                    score += 1
                                            tally["ones"] = "done"
                                            print(f'Your score after this turn is {score}')
                                            yahtzee(score)
                                        else:
                                            print("You already scored that category")
                                    elif attempt.lower() == "twos":
                                        if tally["twos"]==None:
                                            for n in final:
                                                if n == 2:
                                                    score += 2
                                            tally["twos"] = "done"
                                            print(f'Your score after this turn is {score}')
                                            yahtzee(score)
                                        else:
                                            print("You already scored that category")
                                    elif attempt.lower() == "threes":
                                        if tally["threes"] == None:
                                            for n in final:
                                                if n == 3:
                                                    score += 3
                                            tally["threes"] = "done"
                                            print(f'Your score after this turn is {score}')
                                            yahtzee(score)
                                        else:
                                            print("You already scored that category")
                                    elif attempt.lower() == "fours":
                                        if tally["fours"] == None:
                                            for n in final:
                                                if n == 4:
                                                    score += 4
                                            tally["fours"] = "done"
                                            print(f'Your score after this turn is {score}')
                                            yahtzee(score)
                                        else:
                                            print("You already scored that category")
                                    elif attempt.lower() == "fives":
                                        if tally["fives"]==None:
                                            for n in final:
                                                if n == 5:
                                                    score += 5
                                            tally["fives"] = "done"
                                            print(f'Your score after this turn is {score}')
                                            yahtzee(score)
                                        else:
                                            print("You already scored that category")
                                    elif attempt.lower() == "sixes":
                                        if tally["sixes"] == None:
                                            for n in final:
                                                if n == 6:
                                                    score += 6
                                            tally["sixes"] = "done"
                                            print(f'Your score after this turn is {score}')
                                            yahtzee(score)
                                        else:
                                            print("You already scored that category")
                                    elif attempt.lower() == "chance":
                                        if tally["chance"] == None:
                                            for n in final:
                                                score += n
                                            tally["chance"] = "done"
                                            print(f'Your score after this turn is {score}')
                                            yahtzee(score)
                                        else:
                                            print("You already scored that category")
                                    elif attempt.lower() == "3 of a kind" or attempt.lower() == "three of a kind":
                                        if tally["3 of a kind"] == None:
                                            final.sort()
                                            if final[0] == final[2] or final[1] == final[3] or final[2] == final[4]:
                                                for n in final:
                                                    score += n
                                                tally["3 of a kind"] = "done"
                                                print(f'Your score after this turn is {score}')
                                                yahtzee(score)
                                            else:
                                                score += 0
                                                tally["3 of a kind"] = "done"
                                                yahtzee(score)
                                        else:
                                            print("You already scored that category")
                                    elif attempt.lower() == "4 of a kind" or attempt.lower() == "four of a kind":
                                        if tally["4 of a kind"]==None:
                                            final.sort()
                                            if final[0] == final[3] or final[1] == final[4]:
                                                for n in final:
                                                    score += n
                                                tally["4 of a kind"] = "done"
                                                print(f'Your score after this turn is {score}')
                                                yahtzee(score)
                                            else:
                                                score +=0
                                                tally["4 of a kind"] = "done"
                                                yahtzee(score)
                                        else:
                                            print("You already scored that category")
                                    elif attempt.lower() == "yahtzee":
                                        if tally["yahtzee"]==None:
                                            check = set(final)
                                            if len(check)==1:
                                                score += 50
                                                tally["yahtzee"] = "done"
                                                print("You scored 50 for that YAHTZEE!")
                                                print(f'Your score after this turn is {score}')
                                                yahtzee(score)
                                            else:
                                                score += 0
                                                tally["yahtzee"] = "done"
                                                yahtzee(score)
                                        else:
                                            print("You already scored that category")
                                    elif attempt.lower() == "full house":
                                        if tally["full house"]==None:
                                            final.sort()
                                            if (final[0] == final[1] and final[2] == final[4]) or (final[0] == final[2] and final[3] == final[4]):
                                                score += 25
                                                tally["full house"] = "done"
                                                print(f'Your score after this turn is {score}')
                                                yahtzee(score)
                                            else:
                                                score += 0
                                                tally["full house"] = "done"
                                                yahtzee(score)
                                        else:
                                            print("You already scored that category")
                                    elif attempt.lower() == "large straight":
                                        if tally["large straight"]==None:
                                            final.sort()
                                            x = final[0]
                                            for n in final[1:]:
                                                if n - 1 == x:
                                                    x = n
                                                else:
                                                    score += 0
                                                    tally["large straight"] = "done"
                                                    print(f'Your score after this turn is {score}')
                                                    yahtzee(score)
                                            score += 40
                                            tally["large straight"] = "done"
                                            print(f'Your score after this turn is {score}')
                                            yahtzee(score)
                                        else:
                                            print("You already scored that category")
                                    elif attempt.lower() == "small straight":
                                        if tally["small straight"]==None:
                                            remove_duplicates = set(final)
                                            final1 = list(remove_duplicates)
                                            final1.sort()
                                            if (final1[0] + 1 == final1[1] and final1[1] + 1 ==final1[2] and final1[2] +1 == final1[3]):
                                                score += 30
                                                tally["small straight"] = "done"
                                                print(f'Your score after this turn is {score}')
                                                yahtzee(score)
                                            else:
                                                score += 0
                                                tally["small straight"] = "done"
                                                yahtzee(score)
                                        else:
                                            print("You already scored that category")
                                    else:
                                        print("That's not a valid category")
            
        else:
            print(f'Your final score is {score}')
            sys.exit()
            
yahtzee(0)