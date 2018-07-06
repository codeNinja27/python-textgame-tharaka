# name: Tharaka
# date: 2018-07-03
# description: Text-based Ramen adventure game

#Still working refactoring this code and adding more contetnt

# import pygame
import pyglet
import random
import time
import datetime

#Music from Naruto
music = pyglet.resource.media('music.mp3')  #Song need to stop when there is a soundeffect and need to infinitely loop until you quit the game.
# music.play()

# pyglet.app.run()


#Intro
def displayIntro():

    print("")
    print('''
    ****************************************
    *                                      *
    *      Welcome to Ramen Adventure!     *
    *                                      *
    ****************************************
    ''')
    print("")
    print("")
    print("It's the beginning of your quest to find the perfect Ramen shop.")
    print("Legend says that a stranger with crazy thumbs will guide travelers to it.")
    print("As you wonder, you reach a fork in the road. One will lead to the where all the famous Ramen shops resides and the other will lead you to the crazy thumb district, where people with crazy thumbs live.")
    print("")

#Choosing path
def choosePath():
    path = ""
    while path != "right" and path != "left": # input validation
        path = input("Which path will you choose? (right or left): ")

    return path


#Getting current time and check if it within the valid shop hours
def checkTime():
    timestamp1 = datetime.datetime.now().hour

    if timestamp1 >= 0 and timestamp1 <= 20:
        return True
    else:
        return False


#Guess Number
def guessNum(guess):
    print('Your guess', guess)
    # correctNum = random.randint(1, 10)
    correctNum = 7
    correctNumStr = str(correctNum)
    print('Correct Number', correctNum)
    if guess == correctNumStr:
        return True
    else:
        return False

#See if the chosen path is the correct path
def checkPath(chosenPath):
    print("You head down the path...")
    time.sleep(2)
    print("It's a road with only one light pole. You can barely see two 3 feet from you...")
    time.sleep(2)
    print("Suddenly you hear foot steps behind you...")
    time.sleep(2)
    print("Your heart starts to beat faster and faster...")
    time.sleep(2)
    print("You summed up the courage to turn around and see a shadowy figure reach out to you...")
    print()

    correctPath = "left"

    if chosenPath == str(correctPath):
        print("You start running for your life but you couldn't get far before the stranger catch up to you.")
        time.sleep(1)
        print("Before you can respond the stranger speaks to you with a super excited voice. 'I have been waiting for you!'")
        time.sleep(1)
        print("You found Crazy Thumb Mckoy!")
        print("")

        print("Crazy Thumb Mckoy seems to be suspicious of you...")
        time.sleep(2)
        print("It looks as if he is reliving the horrors of guiding the wrong person to the perfect ramen shop...")
        time.sleep(2)
        print("Legend says that ramen shop got bad yelp reviews after the visit of that one person and had to move into the shady part of the town...")
        time.sleep(2)
        print("Crazy Thumb Mckoy was never the same.")
        time.sleep(2)
        print("He decided to give you a test.")
        print("")

        guess = input("Pick a number between 1 and 10!: ")
        
        if guessNum(guess):
            print("")
            print("You pass!")
            time.sleep(2)
            print("He started guiding you trough a maze full of buildings. You probably won't be able to find your way out but its all worth for the perfect ramen.")
            time.sleep(2)
            ch1 = str(input("He gives you an expired ticket. Do you want to take it? [y/n]: "))
            if ch1 in ['y', 'Y', 'Yes', 'YES', 'yes']:
                ticket = 1
            else:
                ticket = 0
            print("He suddenly stops and points to a worn out stand and disapears.")
            time.sleep(2)
            print("You slowly walks toward the shop that looks like a replica from Naruto ramen shop but with a darker atmosphere.")
            time.sleep(2)
            print("There is a sign posted outside...")

            if checkTime():
                print("The shop is open. Come on in!")
                time.sleep(2)
                ch2 = str(input("Do you want to enter the shop? [y/n]: "))
                if ch2 in ['y', 'Y', 'Yes', 'YES', 'yes']:
                    print("You enter the shop.")
                    time.sleep(1)
                    print("There is a talking ramen cup in your way (It's late). It's asking you for a ticket")
                    time.sleep(2)
                    if ticket == 1:
                        print("You showed it the ticket and it melts away.") 
                    else:
                        print("The ramen cup eats you.")
                        print('''
                        ****************************************
                        *                                      *
                        *               Game Over              *
                        *                                      *
                        ****************************************
                        ''')
                        sound = pyglet.resource.media('end.wav', streaming=False)
                        sound.play()
                else:
                    print("You walks away from your dreams...")
                    print('''
                    ****************************************
                    *                                      *
                    *               Game Over              *
                    *                                      *
                    ****************************************
                    ''')
                    sound = pyglet.resource.media('end.wav', streaming=False)
                    sound.play()
            else:
                #Sound Effect when you lose
                sound = pyglet.resource.media('end.wav', streaming=False)
                sound.play()
                print("The shop is closed at the moment. Come back another time!")
                print('''
                ****************************************
                *                                      *
                *               Game Over              *
                *                                      *
                ****************************************
                ''')
                sound = pyglet.resource.media('end.wav', streaming=False)
                sound.play()
        else:
            #Sound Effect when you lose
            sound = pyglet.resource.media('end.wav', streaming=False)
            sound.play()
            print("")
            print("You can't be trusted...")
            print('''
            ****************************************
            *                                      *
            *               Game Over              *
            *                                      *
            ****************************************
            ''')
            sound = pyglet.resource.media('end.wav', streaming=False)
            sound.play()
    else:
        print("You start running for your life but you couldn't get far before the stranger catch up to you.")
        time.sleep(1)
        print("The last thing you see is a pair of chopsticks reaching toward your face.")
        time.sleep(1)
        print("You became another victim of the chopstick killer.")
        print("")
        print('''
        ****************************************
        *                                      *
        *               Game Over              *
        *                                      *
        ****************************************
        ''')
        #Sound Effect when you lose
        # music.time.sleep(1)
        sound = pyglet.resource.media('end.wav', streaming=False)
        sound.play()


#Play again?
playAgain = "yes"
while playAgain == "yes" or playAgain == "y":
    displayIntro()
    choice = choosePath()
    checkPath(choice) # choice is equal to "right" or "left"
    playAgain = input("Do you want to play again? (yes or y to continue playing): ")