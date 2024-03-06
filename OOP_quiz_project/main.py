from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

#new_q = Question()

question_bank=[]

for item in question_data:
    q = item["question"]
    a = item["correct_answer"]
    question_bank.append(Question(q, a))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()


print("You've Completed the quiz")
print(f"Your Final score was: {quiz.score}/{quiz.question_number}")
