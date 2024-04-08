# quiz game

from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

# create question bank
question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# create quiz brain
quiz = QuizBrain(question_bank)

# start quiz
while quiz.still_has_questions():
    quiz.next_question()
