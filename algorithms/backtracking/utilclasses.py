class Utils:
    def __init__(self, **kwargs):
        self.maxlen = kwargs["maxlen"]

    def make_move(self, a):
        pass

    def unmake_move(self, a):
        pass


class SubSets(Utils):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def is_a_solution(self, a):
        return len(a) == self.maxlen

    def process_solution(self, a):
        print ([i+1 for i,x in enumerate(a) if x==1])

    def construct_candidates(self, a):
        return [1, 0]


class Permutations(Utils):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def is_a_solution(self, a):
        return len(a) == self.maxlen

    def process_solution(self, a):
        print(a)

    def construct_candidates(self, a):
        return [i for i in range(self.maxlen) if i not in a]

