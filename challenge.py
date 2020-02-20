from etwas import connection
from question import NounQuestion
from score import Score
from logger import Challengelog


class Challenge:
    def __init__(self, **parameters):
        self.category = parameters.get('category', 'nouns')
        self.question_amount = parameters.get('question_amount', 1)
        self.data = connection(self.category).aggregate([{'$sample': {'size': self.question_amount}}])
        self.score = Score(0)
        self.questions_obj_list = []
        self.questions_list = []
        self.answers_list = []

        for document in self.data:
            question_obj = NounQuestion(document)
            self.questions_obj_list.append(question_obj)
            self.questions_list.append(question_obj.get_input_question())

        self.q_provided = len(self.questions_obj_list)

    def check_amount(self):
        questions_found = len(self.questions_obj_list)
        print(questions_found)
        if questions_found < self.question_amount:
            print(f'Questions requested: {self.question_amount}, found only {questions_found}, proceeding!')

    def process(self):
        self.check_amount()
        for question in self.questions_obj_list:
            self.questions_list.append(question.get_input_question())
            print(question)
            answer = input('Answer: ')
            self.answers_list.append(answer)
            if question.check_answer(answer):
                print('Correct!')
                self.score += 1
            else:
                print('Wrong answer!')

    def final_result(self):
        return f'{self.score}/{self.q_provided}'

    def insert_log_to_db(self):
        log = Challengelog(
            q_requested=self.question_amount,
            q_provided=self.q_provided,
            category=self.category,
            score=self.score,
            questions=self.questions_list,
            answers=self.answers_list
        )
        log_id = log.insert_to_db()
        return f"Inserting log to db: {log_id}"


challenge1 = Challenge(category='nouns', question_amount=4)
challenge2 = Challenge()

challenge1.process()
challenge1.insert_log_to_db()
