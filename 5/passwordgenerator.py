from random import randint



def main() -> str:
    
    #Password Generator Project

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    print("Welcome to the PyPassword Generator!")
    
    nr_letters= int(input("How many letters would you like in your password?\n")) 
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))
    
    password = ""
    
    possibilities = [letters,numbers,symbols]
    p = [nr_letters,nr_numbers,nr_symbols]
    
    for i in range(nr_letters+nr_symbols+nr_numbers):
        print(p)
        
        for j in range(0,len(p)):
        
            if p[j] == 0:
                p.remove(p[j])
                possibilities.pop(j)
                break
            
        rand = randint(0,len(possibilities)-1)
        
        p[rand] -= 1
        
        rand_element = randint(0,len(possibilities[rand])-1)
        
        password += possibilities[rand][rand_element]
    
    return password
    
        
if __name__ == "__main__" :
    print(main())