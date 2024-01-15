from data import question_data
from question import Question
from quiz_brain import QuizBrain

questions: list[Question] = []

for q in question_data:
    questions.append(Question(q["text"], bool(q["answer"])))

quiz = QuizBrain(questions)

while True:
    continue_quiz = quiz.next_question()
    if not continue_quiz:
        exit(0)
