from utilclasses import Permutations, SubSets


finished = False


def get_utils_class(**kwargs):
    if kwargs["type"] == "permutations":
        p = Permutations(**kwargs)
    if kwargs["type"] == "subsets":
        p = SubSets(**kwargs)
    return p


def backtrack(a, **kwargs):
    """

    :param a: List of items that make the current solution
    :param kwargs:
    :return: None
    """

    utilsclass = kwargs.pop("utilsclass", None)

    if utilsclass is None:
        utilsclass = get_utils_class(**kwargs)

    global finished

    if utilsclass.is_a_solution(a):
        utilsclass.process_solution(a)

    else:
        c = utilsclass.construct_candidates(a)
        for cand in c:
            ap = a + [cand]
            utilsclass.make_move(ap)
            backtrack(ap, utilsclass=utilsclass)
            utilsclass.unmake_move(ap)
            if finished:
                break

    return


if __name__ == "__main__":

    backtrack([], type="subsets", maxlen=3)
