"""
Problem 85: Counting rectangles
https://projecteuler.net/problem=85

Solution:
Lets try to find the formula for the number of rectangles in an n-by-n rectangle.
For simplicity's sake, lets start with a 2x2 rectangles can be made:
- 1x1 blocks: fits 4 times
- 2x1 rectangles: fits 2 times
- 1x2 rectangles: fits 2 times
- 2x2 blocks: fits 1 time
Trying this out by hand shows that there is a simple formula that captures this:

SUM(i=1 to n) SUM(j=1 to m) i*j

which can be simplified to SUM(i=1 to n) n*m(m+1)/2 (using the triangle number sum)
or even further simplified to (n*(n+1)*m*(m+1)/2).

It remains to compute n, m such that the number of rectangles is closest to 2 mil.
This I implemented not so efficiently by using two while loops, but it seals the deal.
"""

def count(n, m):
    """Counts the number of rectangles in a n-by-m rectangle."""
    return((n*(n+1)*m*(m+1))//4)



def counting_rectangles(target):
    """Computes the area of a n-by-m rectangle that can fit the nearest
    number of rectangles close to target."""
    n, m = [0, 0]
    error = target
    area = 0
    while count(n, m) < target:
        n += 1
        m = 0
        while count(n, m) < target:
            m += 1
            new_error = abs(count(n, m) - target)
            if new_error < error:
                error = new_error
                area = n*m
        m = 1
    return(area)


if __name__ == "__main__":
    print(counting_rectangles(2*10**6))
