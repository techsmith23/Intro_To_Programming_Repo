import time
import random

food = random.choice(["Bacon", "Sausage", "Ham", "Fries", "Mac & Cheese"])


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


def valid_input(prompt, choice1, choice2):
    while True:
        response = input(prompt).lower()
        if response == choice1:
            return response
        elif response == choice2:
            return response
        else:
            print_pause("Invalid Choice. Please try again")


def intro():
    print_pause("Welcome to My Kitchen!")
    print_pause("I am so glad that you are here today!")
    print_pause("We are going to be cooking up 3 meals,")
    print_pause("And I need your help to see which dish would be the best.")
    print_pause("Let's do this!!!")


def accept_cooking():
    response = valid_input("Do you accept this challenge?", "yes", "no")

    if response == "yes":
        print_pause("Here we go in 3, 2, 1....")
        ingredients(food)
    elif response == "no":
        print_pause("Please, I can't do this without you!")
        new_game()


def ingredients(food):
    print_pause("We are using " + food + "!")
    print_pause("to make either a burger or a pizza")
    response = valid_input("Which would you like?", "burger", "pizza")

    if response == "burger":
        print_pause("We are making a " + food + " Cheeseburger!")
        print_pause("Get ready in 3, 2, 1.....")
        burger(food)
    else:
        print_pause("Chicago Deep Dish " + food + " Pizza!")
        print_pause("Get ready in 3, 2, 1.....")
        pizza(food)


def burger(food):
    print_pause("Okay, so we are going to get started making our burgers!!!")
    print_pause("Step 1: Get the buns.")
    print_pause("Step 2: Get the lettuce, cheese, tomatoes, and pickles")
    print_pause("Step 3: Go and add your " + food + " to your burger")
    print_pause("Enjoy your " + food + " Cheeseburger with Fries!")
    new_game()


def pizza(food):
    print_pause("Okay, so we are going to start making our Deep-Dish Pizza!")
    print_pause("Step 1: Make the dough and put it into the pan.")
    print_pause("Step 2: Put all the sauces and cheeses together.")
    print_pause("Step 3: Add " + food + " to the dish and bake it.")
    print_pause("Enjoy your Deep-Dish Pizza!")
    new_game()


def new_game():
    response = valid_input("Do you want to play again?", "yes", "no")
    if response == "yes":
        print_pause("Okay! Let's go!")
        play_food_game()
    elif response == "no":
        print_pause("Thank you for your time. Goodbye!")
        exit(0)


def play_food_game():

    intro()
    accept_cooking()
    ingredients(food)
    burger(food)
    pizza(food)
    new_game()

play_food_game()
