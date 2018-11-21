import simplegui
import random
import math

num_range = 100
secret = 0
user_guess = 0
num_guesses = 7


def new_game():
    global secret, num_range, num_guesses
    secret = random.randrange(0, num_range)
    if num_range == 100:
        num_guesses = 7
    elif num_range == 1000:
        num_guesses = 10
    print ""
    print "New game. Range is (0 to " + str(num_range) + ")"
    print "Number of remaining guesses is " + str(num_guesses)


def number_of_guesses():
    global num_guesses
    num_guesses = num_guesses - 1
    if num_guesses > 0:
        print "Number of remaining guesses is " + str(num_guesses)
    else:
        print "You ran out of guesses. The number was " + str(secret)
        new_game()


def range100():
    global num_range
    num_range = 100
    new_game()


def range1000():
    global num_range
    num_range = 1000
    new_game()


def input_guess(guess):
    global secret, user_guess
    user_guess = int(guess)
    print ""
    if user_guess == secret:
        print "Guess was " + str(user_guess)
        print "Correct!"
        new_game()
    elif user_guess > secret:
        print "Guess was " + str(user_guess)
        print "Lower!"
    elif user_guess < secret:
        print "Guess was " + str(user_guess)
        print "Higher!"
    else:
        print "Oh, something went wrong!"
    number_of_guesses()
frame = simplegui.create_frame("Guess the number", 200, 200)

frame.add_button('Range is [0, 100]', range100, 200)
frame.add_button('Range is [0, 1000]', range1000, 200)
frame.add_input('Enter guess', input_guess, 50)

frame.start()
new_game()
