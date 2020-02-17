class Score:
    """
    This class takes care of score operations.

    You can either do operations on two Score objects or on object and int.
    """
    def __init__(self, initial_score):
        self.score = initial_score

    def __add__(self, other):
        return self.score + other

    def __mul__(self, other):
        return self.score * other

    def __rmul__(self, other):
        return self.__mul__(other)
