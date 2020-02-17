from uuid import uuid4
from etwas import connection
from question import NounQuestion


class Challenge:
    def __init__(self, **parameters):
        self.id = uuid4()
        self.category = parameters.get('category', 'nouns')
        self.question_amount = parameters.get('question_amount', 1)
        self.data = connection(self.category).aggregate([{'$sample': {'size': self.question_amount}}])
        self.questions_obj_list = []

        for document in self.data:
            self.questions_obj_list.append(NounQuestion(document))

    def check_amount(self):
        questions_found = len(self.questions_obj_list)
        if questions_found < self.question_amount:
            print(f'Questions requested: {self.question_amount}, found only {questions_found}, proceeding!')

    def score(self):
        pass

    def process(self):
        self.check_amount()
        for question in self.questions_obj_list:
            print(question)
            answer = input('Answer:')
            if question.check_answer(answer):
                print('Correct!')
            else:
                print('Wrong answer!')


challenge1 = Challenge(category='nouns', question_amount=2)
challenge2 = Challenge()

challenge1.process()
