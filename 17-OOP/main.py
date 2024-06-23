from quiz_brain import Quiz



if __name__ == "__main__":
    quiz = Quiz()
    while(quiz.reached_limit() == False):
        quiz.next_question()

