from sympy import sieve
from quicktions import Fraction as F
from collections import defaultdict


def next_states(state, N):
    """Returns a dictionary of the possible next states
    and its probablity as key-value pairs.

    E.g. if state = (1, 2) then it should return
    {(1, 2, 1): 1/2, (1, 2, 3): 1/2}
    """
    candidates = {}
    d = state[-1]
    if d == 1:
        new_state = list(state) + [2]
        candidates[tuple(new_state)] = F(1, 1)
    elif d == N:
        new_state = list(state) + [N-1]
        candidates[tuple(new_state)] = F(1, 1)
    else:
        for x in [1, -1]:
            candidates[tuple(list(state) + [d + x])] = F(1, 2)

    return candidates


def sequence_probability(state, seq, primes):
    """Given a state, calculate the probability that the sequence will be heard.

    Skip the first position in the state.

    E.g. if seq = (1, 2, 3) and target_sound = 'PPP' then it should return
    p = 1/3*2/3*2/3 = 4/27
    """
    p = F(1, 1)
    # print(state, seq)
    for i, n in enumerate(state):
        if n in primes:
            if seq[i] == 'P':
                p *= F(2, 3)
            else:
                p *= F(1, 3)
        else:
            if seq[i] == 'P':
                p *= F(1, 3)
            else:
                p *= F(2, 3)
    return p


def p329(N, seq):
    """Finds the probability that the prime frog hears the given sequence
    on N squares. Answer given in fraction p/q reduced form."""
    T = len(seq)
    board = range(1, 501)
    primes = set(sieve.primerange(1, N+1))
    expected = 0

    for start in board:
        current, next = {(start,): F(1, 1)}, defaultdict(int)
        for t in range(T-1):
            for curr_state, p in current.items():
                for next_state, q in next_states(curr_state, N).items():
                    next[next_state] += p*q
            current = next
            next = defaultdict(int)

        for state, p in current.items():
            expected += p * sequence_probability(state, seq, primes)

    return expected * F(1, N)


if __name__ == "__main__":
    print(p329(500, 'PPPPNNPPPNPPNPN'))
