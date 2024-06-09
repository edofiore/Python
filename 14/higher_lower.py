from random import randint ,choice
from data import data
from typing import Dict



def check_result(dict_comparison : Dict[str,Dict[str,str|int]] , choose : str, current_score : int) -> bool:
    """Check response and return True or False"""
    
    against = ["A","B"]
    against.remove(choose)
    if dict_comparison[choose]['follower_count'] > dict_comparison[against[0]]['follower_count']:
        current_score += 1
        return True , current_score  # in order to modify the current score in highlower function, we must return the local value (being an int, it is passed by copy)    
    return False , current_score

    

def higherlower() -> None:
    
    current_score = 0
    dict_comparision = {"A" : data[randint(0,len(data)-1)],
                        }
    
    correct_flag = True
    
    while(correct_flag == True):
        
        dict_comparision["B"] = data[randint(0,len(data)-1)]
        # dict_comparision["B"] = choice(data)
        
        while(dict_comparision["A"] == dict_comparision["B"]):
            dict_comparision["B"] = data[randint(0,len(data)-1)]

        print(f"COMPARE A: {dict_comparision['A']['name']}, {dict_comparision['A']['description']} from {dict_comparision['A']['country']}")
        print(f"vs\nCOMPARE B: {dict_comparision['B']['name']}, {dict_comparision['B']['description']} from {dict_comparision['B']['country']}")
    
        choose : str= input("Who has more followers?: Type 'A' or 'B': ")

        correct_flag, current_score = check_result(dict_comparision,choose,current_score)
        
        dict_comparision["A"] = dict_comparision[choose]
        
        
    print(f"Sorry, you are wrong. Final Score: {current_score}")
    
    
if __name__ == "__main__":

    higherlower()
    