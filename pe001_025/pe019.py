"""
Problem 19: Counting Sundays
https://projecteuler.net/problem=19

Solution:
Python has a very useful datetime module for these kind of problems.
It includes the date object, which can be easily used to calculate
the difference in days between dates. Moreover, since we know that
the first day of the 20th century occured on a Monday, we know that
if the difference of any day and the first day is 6 modulo 7, then
it must be a Sunday.

"""
import datetime as dt


def counting_sundays():
    """Counts the number of Sundays that occured on the first of the
    month during the twentieth century."""
    start_date = dt.date(1900, 1, 1)  # This is a Monday
    count = 0
    for year in range(1901, 2000+1):
        for month in range(1, 12+1):
            if (dt.date(year, month, 1) - start_date).days % 7 == 6:
                count += 1
    return(count)


if __name__ == "__main__":
    print(counting_sundays())
