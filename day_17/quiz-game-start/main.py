from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for ele in question_data:
    new_question = Question(ele["question"], ele["correct_answer"])
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz!")
print(f"Your final score is {quiz.score}/{len(question_bank)}")
