# quiz game

from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

# create question bank
question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# create quiz brain
quiz = QuizBrain(question_bank)

# start quiz
while quiz.still_has_questions():
    quiz.next_question()


print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
