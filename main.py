print("""
                                  |>>>
                    |>>>      _  _|_  _         |>>>
                    |        |;| |;| |;|        |
                _  _|_  _    \\.    .  /    _  _|_  _
               |;|_|;|_|;|    \\:. ,  /    |;|_|;|_|;|
               \\..      /    ||;   . |    \\.    .  /
                \\.  ,  /     ||:  .  |     \\:  .  /
                 ||:   |_   _ ||_ . _ | _   _||:   |
                 ||:  .|||_|;|_|;|_|;|_|;|_|;||:.  |
                 ||:   ||.    .     .      . ||:  .|
                 ||: . || .     . .   .  ,   ||:   |      
                 ||:   ||:  ,  _______   .   ||: , |            
                 ||:   || .   /+++++++\    . ||:   |
                 ||:   ||.    |+++++++| .    ||: . |
              __ ||: . ||: ,  |+++++++|.  . _||_   |
     ____--`~    '--~~__|.    |+++++++|----~    ~`---,              
--~                   ~---__|,--~'                  ~~----_____-~'  """)
 
print()
print("Welcome to The Troll Toll!")
print()

import time

def play_tolltroll():

    name = input("What is your name young knight? > ").title()
    time.sleep(.5)

    print()
    print(f'Princess: "Help me {name}"! I was minding my business on a leisurely stroll, when suddenly KIDNAPPED by a hideous troll!"')
    time.sleep(2)
    
    print()

    print('Troll: "If you want your princess returned to thee, you must first answer my questions three!" ')
    time.sleep(2)
    print()

    print("Do you dare to save the heir? (y or n?)")
    
    while True:
        user_answer = input("> ").lower()
        print()

        if user_answer == "y":
            main_loop()
            break
        elif user_answer == "n":
            print("okay...coward..")
            print()
            print("goodbye!")
            break
        else:
            print("Please respond 'y' or 'n':")

answer = "sidewalk"

def word_scrambler(answer):
    import random
    scramble_word = random.sample(answer, len(answer))
    scramble_word = "".join(scramble_word)

    return scramble_word

import sys

def play_unscramble():
   
    attempts = 3
    threshold = 0

    while attempts > threshold:
        scrambled_word = word_scrambler(answer)
        print(f"Question # 1: Unscramble the following word: {scrambled_word}")
        print()

        user_guess = input("> ").lower()
        print()
        
        if user_guess == answer:
            print("Hip hip hooray! That is correct...")
            print("...but the following question is harder yet! ")
            time.sleep(2)
            print()
            return True
            break
        else:
            print("Wrong guess!")
            attempts = attempts - 1
            print(f"Attempts left: {attempts}")
            time.sleep(1.5)
            print()
            print(f"Hint: the word begins with '{answer[0].title()}' ")
            time.sleep(1.5)
            print()

    else:

        return False

def play_trivia():
    print("Question # 2: On March 8th, 2021, The Wall Street Journal published an article titled: 'How do you solve a problem like Korea?' This article title rhymes with and is referencing a song from this hit 1959 musical about a would-be nun who cares for seven children in the Austrian countryside.")
    print()
    print("A) Mamma Mia!")
    print("B) Candide")
    print("C) The Sound of Music")
    print("D) Into the Woods ")
    print()


    attempts = 3
    threshold = 0 

    while attempts > threshold: 
        print("Choose A, B, C, or D")
        user_answer = input("> ")
        user_answer = user_answer.lower()
        print()

        if user_answer == "c":
            print("You're doing quite well, you may advance..")
            print("...to a final round, to a game of chance!")
            time.sleep(2.5)
            print()
            return True
            break
            
        elif user_answer == "A" or "B" or "D":
            print("Wrong guess!")
            attempts = attempts - 1
            print(f"Attempts left: {attempts}")
            print()
            time.sleep(1)
            print("Hint: the family's eldest child is 'Sixteen Going on Seventeen' ♫")
            time.sleep(2)
            print()
        else:
            print("Incorrect input! Please choose either A, B, C, or D")
            print()
    else:
        return False

def rolling_the_dice():

    from random import randint

    dice_1 = randint(1, 6)
    dice_2 = randint(1, 6)
    user_roll = dice_1 + dice_2

    print(f"Dice 1 = {dice_1}")
    print(f"Dice 2 = {dice_2}")
    time.sleep(1.5)
    print(f"Good roll! You rolled {user_roll}!")
    time.sleep(1)
    print()

    return user_roll

def play_dice():

    print(
        "Question # 3: Roll two dice and guess whether the sum of both dice will be 7 and above or below 7."
    )
    print()

    attempts = 3
    threshold = 0  

    while attempts > threshold:
        user_guess = input("above or below? > ").lower()
        
        print()
        user_roll = rolling_the_dice()
        if user_guess == "above":
            if user_roll >= 7:
                return True
                break
            else:
                print("Wrong guess!")
                attempts = attempts - 1
                print(f"Attempts left: {attempts}")
                time.sleep(1.5)
                print()
            
        elif user_guess == "below":
            if user_roll < 7:
                return True
                break
            else:
                print("Wrong guess!")
                attempts = attempts - 1
                print(f"Attempts left: {attempts}")
                time.sleep(1.5)
                print()
        
        else:
            input("You must choose either Above or Below!")
    else:
        return False

def main_loop():
    if play_unscramble() == False or play_trivia() == False or play_dice() == False:
        print("Maximum number of attempts exceeded!")
        print()
        print("GAME OVER!")
        sys.exit()

    else: 
        print("You beat me this time, well aren't you plucky... ")
        print("...if we meet again you won't be so lucky!!!!")
        print()
        print("""                                A    
(,);    /\                 A    H    
(  ^_   ||       ...       H MM HA   
' /  \  ||      (()))     AH^HH^HH   
  L |=) ||      {' ())    HH_HH_HH   
   ) -  ||       )_ (() AAxHHHHxAxH  
 (_   \====  @  (   (_) HHHH/^\HHHH  
 | (___/{ }   \7 \ _) |_HHHH___HHHHH_  """)

        sys.exit()


play_tolltroll()
    

    
     


    
