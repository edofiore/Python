import os



def main() -> None:
    
    print("Welcome to the secret auction program\n")
    go_on = "yes"
    bidders = {}
    
    while(go_on == "yes".lower()):
        name = input("What is your name? ")
        bid = int(input("What's your bid? $"))
        
        if not bidders:
            max_key = name
        else:
            if bidders[max_key] < bid:
                max_key = name
        bidders[name] = bid
        go_on = input("Are there any other bidders? Type 'yes' or 'no'.\n")
        os.system("cls")
    
    print(f"The winner is {max_key} with a bid of {bidders[max_key]} $\n")
    
if __name__ == "__main__":
    main()
    