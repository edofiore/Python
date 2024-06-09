import os

def moltiplication(n1: float,n2: float) -> float:
    """return moltiplication"""
    return n1*n2

def division(n1: float,n2: float):
    """return division"""
    return n1/n2

def plus(n1: float,n2: float) -> float:
    """return addition"""
    return n1+n2

def minus(n1: float,n2: float) ->float:
    """return minus"""
    return n1-n2




def main() -> None:
    
    # Dictionary of functions
    o = {
        "+": plus,
        "-": minus,
        "*": moltiplication,
        "/": division
    }
    

    n1 = float(input("What's the first number? "))
    print("+\n-\n/\n*\n")
    
    continue_flag = True
    
    while(continue_flag):
        operation = input("Pick an operation: ")
        n2 = float(input("What's the next number? "))
        
        
        # create a function variable
        function = o[operation]
        res = function(n1,n2)
        
        
        # if operation == "+":
        #     res = plus(n1,n2)
        # elif operation == "-":
        #     res = minus(n1,n2)
        # elif operation == "/":
        #     res = division(n1,n2)
        # else:
        #     res = moltiplication(n1,n2)
        
        res = round(res,2)
        print(f"{n1} {operation} {n2} = {res}")
        
        cont = input(f"Type 'y' to continue calculating with {res} o type 'n' to restart a new one: ")
        if cont == "y":
            n1 = res
        else:
            continue_flag = False
            
    main()
            


if __name__ == "__main__":

    main()