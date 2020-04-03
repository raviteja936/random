
def is_a_solution(a, **kwargs):
    try:
        maxlen = kwargs["maxlen"]
    except:
        print("maxlen not given")
        return

    return (len(a) == maxlen)

def process_solution(a, **kwargs):
    print(a)

def construct_candidates(a, **kwargs):
    try:
        maxlen = kwargs["maxlen"]
    except:
        print("maxlen not given")
        return

    return [i for i in range(maxlen) if i not in a]

def make_move(a, **kwargs):
    pass

def unmake_move(a, **kwargs):
    pass
