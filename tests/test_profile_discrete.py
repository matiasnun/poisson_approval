from fractions import Fraction
from poisson_approval import ProfileDiscrete, StrategyOrdinal, PLURALITY, ANTI_PLURALITY


def test_normalization():
    profile = ProfileDiscrete({('abc', 0.2): 1, ('acb', 0.4): 1})
    assert profile.abc == 0.5


def test_plurality():
    """
        >>> profile = ProfileDiscrete({('abc', 0.2): 1, ('acb', 0.4): 1}, voting_rule=PLURALITY)
        >>> profile
        ProfileDiscrete({'abc': {0.2: 0.5}, 'acb': {0.4: 0.5}}, voting_rule='Plurality')
        >>> print(profile)
        <abc 0.2: 0.5, acb 0.4: 0.5> (Condorcet winner: a) (Plurality)
    """
    pass


def test_anti_plurality():
    """
        >>> profile = ProfileDiscrete({('abc', 0.2): 1, ('acb', 0.4): 1}, voting_rule=ANTI_PLURALITY)
        >>> profile
        ProfileDiscrete({'abc': {0.2: 0.5}, 'acb': {0.4: 0.5}}, voting_rule='Anti-plurality')
        >>> print(profile)
        <abc 0.2: 0.5, acb 0.4: 0.5> (Condorcet winner: a) (Anti-plurality)
    """
    pass


def test_misc_forms_of_input():
    """
        >>> profile = ProfileDiscrete({('abc', 0.2): 0, ('abc', 0): Fraction(3, 7), ('bca', 1): Fraction(4, 7)})
        >>> profile
        ProfileDiscrete({}, d_weak_order_share={'a>b~c': Fraction(3, 7), 'b~c>a': Fraction(4, 7)})
        >>> print(profile)
        <a>b~c: 3/7, b~c>a: 4/7> (Condorcet winner: b, c)
    """
    pass


def test_strategy_weak_order():
    """
        >>> profile = ProfileDiscrete({('abc', 0.3): Fraction(1, 7), 'a~b>c': Fraction(2, 7), 'c>a~b': Fraction(4, 7)})
        >>> strategy = StrategyOrdinal({'abc': 'a'}, profile=profile)
        >>> print(strategy.tau)
        <a: 1/7, ab: 2/7, c: 4/7> ==> c
    """
    pass
