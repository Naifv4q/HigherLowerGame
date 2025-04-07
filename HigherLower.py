import random
from os import system
import HigherLowerArt
from HigherLowerGameData import data
from time import sleep

def higher_lower():
    system("cls")
    is_true=True
    score=0

    #Here the program choses 2 random numbers to to fetch a random website index from the data file by it
    random_choice_A=random.randint(0,18)
    random_choice_B=random.randint(0,18)
    #if both numbers match, this if condition ensures that they are different
    if random_choice_A==random_choice_B:
        random_choice_B=random.randint(0,18)
    
    #The loop below makes sure the game is running until it is terminated by the user
    while is_true:
        print(HigherLowerArt.logo)
        if score>0:
            print("============================================")
            print(f"You're right ! Current score: {score}")
            print("============================================")
        print("Which website is more visited in KSA ?")
        print(f"Compare A: {data[random_choice_A]["Website"]} : {data[random_choice_A]["Visits"]} visits")
        print(HigherLowerArt.vs)
        print(f"Against B: {data[random_choice_B]["Website"]}")
        dec=input("Which website has more visits? Type 'A' or 'B': ").upper()
        #After the user input his guess, the if conditions below check which website has more visits by checking their rank from the data file, 
        #after the check is succesful and user choice is correct, choice B becomes A, and the new choice B is taken at random, 
        #and if the user have chosen a correct answer, he gets one points to his score.
        #Lastly if the user guess is wrong, this loop terminates, ending the game.
        if data[random_choice_A]["Rank"] < data[random_choice_B]["Rank"] and dec=="A":
            score+=1
            random_choice_A = random_choice_B
            random_choice_B = random.randint(0, 18)
            if random_choice_A == random_choice_B:
                random_choice_B = random.randint(0, 18)
            system("cls")

        elif data[random_choice_A]["Rank"] > data[random_choice_B]["Rank"] and dec=="A":
            print(f"Sorry, that's the wrong answer. Final score: {score}")
            is_true=False

        elif data[random_choice_A]["Rank"] < data[random_choice_B]["Rank"] and dec=="B":
            print(f"Sorry, that's the wrong answer. Final score: {score}")
            is_true=False

        elif data[random_choice_A]["Rank"] > data[random_choice_B]["Rank"] and dec=="B":
            score += 1
            random_choice_A =random_choice_B
            random_choice_B = random.randint(0, 18)
            if random_choice_A == random_choice_B:
                random_choice_B = random.randint(0, 18)
            system("cls")
            
#The function is called to start the game, and the loop below it gives the user the ability to replay the game and try again, or close the game.
higher_lower()
keepGoing=True
while keepGoing:
    userDec = input("Would you like to try again? 'y' or 'n': ").lower()
    if userDec=="y":
        higher_lower()
    elif userDec=="n":
        print("Maybe another time :) Goodbye !")
        keepGoing=False
    else:
        print("Invalid input !")
