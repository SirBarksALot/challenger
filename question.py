class NounQuestion:
    def __init__(self, content, **params):
        self.content = content
        self.in_language = params.get('in_language', 'german')
        self.out_language = params.get('out_language', 'english')
        self.question = self.content.get(self.in_language)[0]
        self.correct_answer = self.content.get(self.out_language, '')

    def __str__(self):
        return f'''Translate to {self.out_language}:
{self.question}'''

    def get_input_question(self):
        return self.question

    def check_answer(self, user_answer):
        if user_answer in self.correct_answer:
            return True
        else:
            return False
