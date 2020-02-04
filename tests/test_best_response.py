from poisson_approval import *


def test_best_response():
    """
        >>> tau = TauVector({'a': 9/15, 'b': 4/15, 'ac': 1/15, 'bc': 1/15})
        >>> best_response = BestResponse(tau, 'abc')
        >>> best_response.ballot
        'a'
        >>> best_response.threshold_utility
        1
    """
    pass


def test_correct_identification_of_easy_easy_edge_case():
    tau = TauVector({'a': 0.24382716330832704, 'ab': 0.0011384657401753433,
                     'ac': 0.25507268421895707, 'b': 0.2550449552509131,
                     'bc': 0.24379357320990255, 'c': 0.001123158271724989})
    assert 0 <= tau.d_ranking_best_response['cab'].threshold_utility <= 1


def test_offset_method_with_trio_approximation():
    tau = TauVector({
        'a': 0.2438625672480171, 'ab': 0.0011437146863146892,
        'ac': 0.25503412377742823, 'b': 0.25503005949673074,
        'bc': 0.24380331566218985, 'c': 0.0011262191293193397
    })
    assert 0 <= tau.d_ranking_best_response['acb'].threshold_utility <= 1