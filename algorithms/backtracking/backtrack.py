from utils import *

finished = False


def backtrack(a, **kwargs):
    """

    :param a: List of items that make the current solution
    :param kwargs:
    :return: None
    """

    global finished

    if is_a_solution(a, **kwargs):
        process_solution(a, **kwargs)

    else:
        c = construct_candidates(a, **kwargs)
        for cand in c:
            ap = a + [cand]
            make_move(a, **kwargs)
            backtrack(ap, **kwargs)
            unmake_move(a, **kwargs)
            if finished:
                break

    return
