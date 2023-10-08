import random
from colorama import Fore
import time

loads = ["Loading...", "Almost done...", "Connecting...", "Running..."]
for i in range(4):
    print("\n\n" + random.choice(loads))
    time.sleep(0.5)
            
def generate_random_value():
    value = random.choice([random.randint(1, 100), random.uniform(1, 100), 
                           random.choice(['True', 'False']), 
                           ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=5))])
    return value

def play_guessing_game():
    while True:
        random_value = generate_random_value()
        
        print(Fore.CYAN + "\nWelcome to the Guess the Data Type game!")
        print(Fore.YELLOW + "\nHere's a randomly generated value. Try to guess its data type.")
        print(Fore.WHITE + "Value:", random_value)

        guess = input(Fore.BLUE + "Enter your guess (string, integer, boolean, or real): ").lower()
        
        if guess == 'string' and isinstance(random_value, str):
            print(Fore.LIGHTGREEN_EX + "Correct! The data type is string.")
        elif guess == 'integer' and isinstance(random_value, int):
            print(Fore.LIGHTGREEN_EX + "Correct! The data type is integer.")
        elif guess == 'boolean' and isinstance(random_value, bool):
            print(Fore.LIGHTGREEN_EX + "Correct! The data type is boolean.")
        elif guess == 'real' and isinstance(random_value, float):
            print(Fore.LIGHTGREEN_EX + "Correct! The data type is real.")
        else:
            print(Fore.RED + "Incorrect. The data type is:", type(random_value).__name__)

        play_again = input(Fore.LIGHTMAGENTA_EX + "Do you want to play again? (yes/no): ").lower()
        if play_again not in ['yes', 'y']:
            break

if __name__ == "__main__":
    play_guessing_game()
