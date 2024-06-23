class Question():
    """Class containing the question"""
    
    def __init__(self, question: str, answer : str) -> None:
        
        self.question : str = question
        self.answer : str = answer
        
    def report(self) -> None:
        print(f"Question: {self.question} --> {self.answer}")
    
    def print_question(self) -> None:
        print(self.question)
        
        
    
    
    