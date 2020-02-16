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

    def process(self):
        for question in self.questions_obj_list:
            print(question)
            answer = input('Answer:')
            if question.check_answer(answer):
                print('Correct!')
            else:
                print('Wrong answer!')


challenge1 = Challenge(category='nouns', question_amount=5)
challenge2 = Challenge()

challenge2.process()
