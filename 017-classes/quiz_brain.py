from question import Question


class QuizBrain:
    def __init__(self, questions: list[Question]):
        self.question_list = questions
        self.question_idx = 0
        self.score = 0

    def next_question(self) -> bool:
        """Present the next question to user, score it and return whether to continue or not"""
        continue_quiz = True
        if self.question_idx < len(self.question_list):
            question = self.question_list[self.question_idx]
            answer = input(f"Qu.{self.question_idx + 1} - {question.text} : (T)rue or (F)alse ? : ")[0].lower()
            if answer == 't' or answer == 'f':
                if (answer == 't' and question.answer) or (answer == 'f' and not question.answer):
                    self.score += 1
                print(f"The correct answer was: {question.answer}")
                print(f"Your current score is: {self.score}/{self.question_idx + 1}")
                self.question_idx += 1
            elif answer == 'x' or answer == 'q':
                continue_quiz = False
        else:
            print("No more questions available")
            continue_quiz = False

        if not continue_quiz:
            print(f"Your final score was: {self.score}/{self.question_idx}")

        return continue_quiz
