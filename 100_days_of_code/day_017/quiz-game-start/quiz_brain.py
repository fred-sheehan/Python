class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0


    def next_question(self):
        for question in self.question_list:
            self.question_number += 1
            user_answer = input(f"Q.{self.question_number}: {question.text} (True/False): ")
            self.check_answer(user_answer, question.answer)
            print(f"Your current score is: {self.score}/{self.question_number}")


    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
        else:
            self.score


    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            print("You've completed the quiz")
            print(f"Your final score was: {self.score}/{self.question_number}")
            return False
