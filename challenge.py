from uuid import uuid4
from etwas import connection
from question import NounQuestion
from score import Score


class Challenge:
    def __init__(self, **parameters):
        self.id = uuid4()
        self.category = parameters.get('category', 'nouns')
        self.question_amount = parameters.get('question_amount', 1)
        self.data = connection(self.category).aggregate([{'$sample': {'size': self.question_amount}}])
        self.questions_obj_list = []
        self.score = Score(0)

        for document in self.data:
            self.questions_obj_list.append(NounQuestion(document))

    class Validation:
        def __int__(self, decorated_func):
            self._decorated = decorated_func

        def __call__(self, *args, **kwargs):
            questions_found = len(self._decorated['questions_obj_list'])
            print(questions_found)
            return self._decorated
            #if questions_found < self.question_amount:
            #    print(f'Questions requested: {self.question_amount}, found only {questions_found}, proceeding!')

    @Validation
    def process(self):
        #self.check_amount()
        for question in self.questions_obj_list:
            print(question)
            answer = input('Answer:')
            if question.check_answer(answer):
                print('Correct!')
                self.score += 1
            else:
                print('Wrong answer!')

    def final_result(self):
        return f'{self.score}/{self.questions_obj_list}'


challenge1 = Challenge(category='nouns', question_amount=5)
challenge2 = Challenge()

challenge1.process()
