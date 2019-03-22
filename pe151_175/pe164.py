"""
Problem 164: Numbers for which no three consecutive digits have a sum greater
than a given value.
https://projecteuler.net/problem=164

Solution:
- Find the pool of 3-digit numbers such that the sum does not exceed 9.
- Define

ways[n][m]: possible ways of writing an n-digit number s.t. the first
three are m (with leading zeros).
o"""
def pe164(N):
    """Returns the number of N-digit numbers that can be written
    such that no three consecutive digits have a sum greater than 9. """
    def get_last_two_digits(m):
        """Gets the last two digits of m including leading zeros."""
        m = str(m)
        if len(m) < 3:
            while len(m) < 3:
                m = '0' + m
        return(m[1:])


    def digit_sum(n):
        sum = 0
        for c in str(n):
            sum += int(c)
        return(sum)

    pool = [i for i in range(1000) if digit_sum(i) < 10]
    ways = [[0]*1000 for n in range(N+1)]

    for n in range(3, N+1):
        for m in pool:
            if n == 3:
                ways[n][m] = 1
            elif n == N and m < 100:
                ways[n][m] = 0
            else:
                m23 = get_last_two_digits(m)
                for i in range(9-digit_sum(m23)+1):
                    ways[n][m] += ways[n-1][int(m23 + str(i))]
    return(sum([ways[N][i] for i in range(1000)]))


if __name__ == "__main__":
    print(pe164(20))
