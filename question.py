class NounQuestion:
    def __init__(self, content):
        self.in_language = content.get('in_language', 'german')
        self.out_language = content.get('out_language', 'english')
        self.question = content.get(self.in_language)[0]
        self.correct_answer = content.get(self.out_language, '')

    def __str__(self):
        return f'''Translate to {self.out_language}: 
{self.question}'''

    def get_hint(self):
        return self.correct_answer

    def get_input_question(self):
        return self.question

    def get_correct_answer(self):
        return self.correct_answer

    def check_answer(self, user_answer):
        if user_answer in self.correct_answer:
            return True
        else:
            return False
