from question_model import Question
from data import question_data
from typing import List

class Quiz():
    
    def __init__(self) -> None:
        
        self.questions : List[Question] = [ Question(question=question["text"],answer=question["answer"]) for question in question_data]
        self.question_number : int = 0
        self.score : int = 0
    
    def next_question(self) -> None:
        
        self.questions[self.question_number].print_question()
        self.question_number += 1
        user_answer : str = input("True or False? ----> ")

        is_correct : bool = self.check_result(user_answer, self.questions[self.question_number-1].answer)
        
        
        
        
    def check_result(self, user_answer : str, correct_answer : str) -> None:
        
        if user_answer.lower() == correct_answer.lower():
            print("You are right!")
            self.score += 1
        else:
            print("You are wrong")
        
        print(f"Your score is {self.score}/{self.question_number}")
            
        
    
    def reached_limit(self,) -> bool:
        
        if len(self.questions) > self.question_number:
            return False
        
        return True
        
        
        
        
        
    
        
        
    