from functools import reduce


def is_substring(s, substring):
    return substring in s


def final_check(s, N):
    """Check if the final string consists of distinct subsequences."""
    s = s + s[:N-1]
    return len(set([s[i:i+N] for i in range(2**N)])) == 2**N


def pe265(N):
    """Computes S(N): the set of unique numeric representations."""
    L = []

    def extend(seq, tail, N):
        """Recursively extends a binary sequence with 0 or 1
        as long as the tail (current subsequence) is not repeated."""
        if len(seq) == 2**N:
            if final_check(seq, N):
                L.append(seq)
        else:
            for i in range(2):
                candidate = tail[1:] + f'{i}'
                if not is_substring(seq, candidate):
                    extend(seq + f'{i}', candidate, N)

    extend('0'*N, '0'*N, N)
    S = reduce(lambda a, b: a + b,
               map(lambda x: int(x, 2), L))

    return S


if __name__ == "__main__":
    N = 5
    print(pe265(N))
