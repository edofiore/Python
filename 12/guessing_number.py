from random import randint

# define costant values
ANSWER : int = randint(1,100)

HIGH_TURNS : int = 5
MEDIUM_TURNS : int= 8
LOW_TURNS : int = 10

# set turns

def get_turns() -> int:
    """Return turns based on input"""
    level = input("level: \nHigh\nMedium\nEasy\n")
    
    if level.lower() == "high":
        return HIGH_TURNS
    elif level.lower() == "medium":
        return MEDIUM_TURNS
    else:
        return LOW_TURNS
    
def check(guess : int) -> bool:
    """Return a flag depending on the check"""
    if ANSWER == guess:
        print("YOU DID IT!!")
        return True
    else:
        if(ANSWER<guess):
            print("Too high")
        else:
            print("Too low")
            
        return False
    

def game():
    
    turns : int = get_turns()
    print(f"You have {turns} guesses available\n")

    victory_flag = False
    
    while(turns > 0 and not victory_flag):
        guess = int(input("Guess the number: "))
        
        victory_flag = check(guess)
        turns -=1
        
    print(f"Random number was: {ANSWER}")
        


if __name__ == "__main__":
    game()

    