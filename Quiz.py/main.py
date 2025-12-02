from question_model import Questions
from data import question_data
from quiz_brain import QuizBrain


question_bank =[]
for question in question_data['results']:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Questions(question_text,question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()
print("you have completed a Quiz!")
print(f"your final score is {quiz.score}/{quiz.question_num}") 

