from random import random, randint


def main() -> None:
    rock = '''
        _______
    ---'   ____)
        (_____)
        (_____)
        (____)
    ---.__(___)
    '''

    paper = '''
        _______
    ---'   ____)____
            ______)
            _______)
            _______)
    ---.__________)
    '''

    scissors = '''
        _______
    ---'   ____)____
            ______)
        __________)
        (____)
    ---.__(___)
    '''
    
    lista = []
    lista.append(rock)
    lista.append(paper)
    lista.append(scissors)
    
    print("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors." )
    choose = int(input())
    
    print(lista[choose])
    
    computer_choose = randint(0,2)
    
    print(f"Computer chose:\n{lista[computer_choose]}")
    
    if computer_choose == choose:
        print("SET")
        return None
    elif computer_choose==2:
        computer_choose == -1
        
    if computer_choose+1 == choose:
        print("You Win")
    else:
        print("You Lose")
    
    
    
    
    
    
    
    return None

if __name__ == "__main__":
    
    main()