from random import randint
from click import clear
from logo import logo

class Game:
    def __init__(self):
        self.round = 1
        self.win = 0

    def game_header(self):
        print("Welcome to")
        print(logo)
        print("*******************************************\n")
        print("I'm thinking of a number between 1 and 100.\n")
        
    def set_difficulty(self):
        set_level =  True
        difficulty = input("Choose a difficulty.\ne for 'easy' | i for intermediate | h for 'hard': ").lower()
        
        while set_level:
            if difficulty == "e":
                set_level = False
                return 8
            elif difficulty == "i":
                set_level = False
                return 5
            elif difficulty == "h":
                set_level = False
                return 3
            else:
                difficulty = input("e for 'easy' | i for intermediate | h for 'hard': ").lower()

    def generate_random_number(self):
        return randint(1, 101)

    def guessing_number(self, attempts):
        attempts = attempts
        remained = attempts
        number_to_guess = self.generate_random_number()

        guessing = True
        while guessing:
            print(f"\nYou've {remained}/{attempts} remaining to guess the number.")
    
            guess = int(input("\nMake a guess: "))
            
            if number_to_guess > guess:
                print("Too low!")
                remained -= 1
                print(f"You've {remained}/{attempts} remaining")
            
            if number_to_guess < guess:
                print("Too high!")
                remained -= 1
                print(f"You've {remained}/{attempts} remaining")
    
            if number_to_guess == guess and remained >= 0:
                print(f"\nYeah {guess}!. You got it at attempt no. {attempts - remained}!")
                self.win += 1
                guessing = False
    
            if number_to_guess != guess and remained == 0:
                print(f"\nSorry, you are out of attempt!\nThe answer is {number_to_guess}.")
                guessing = False
        
    def on_game(self):
        self.game_header()
        attempts = self.set_difficulty()
        self.guessing_number(attempts)

    def off_game(self):
        print("Bye bye!")
        print("\n*******************************************\n")
        print(f"You've played {self.round} {'games' if self.round > 1 else 'game'}.")
        
        if self.win:
            print(f"Hooray! You've won {self.win} {'times' if self.win > 1 else 'time'}.")
        else:
            print(f"You didn't won any for this time! Try again next time.")
        
    def start_game(self):
        self.on_game()

        while input("\nPlay? 'y' to continue or enter to exit: ") == "y":
            clear()
            self.round += 1
            self.on_game()
        else:
            clear()
            self.off_game()


guessing_number = Game()
guessing_number.start_game()

