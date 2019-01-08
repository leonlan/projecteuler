"""
Problem 17: Number letter counts
https://projecteuler.net/problem=17

Solution:
In order to count the number letter counts, we first need to keep track
of the inconsistencies of all English numbers, e.g. one, two, thirty, etc.
When we have initialized a dictionary of such numbers, then we can
compute the number letter counts for numbers that follow a consistent pattern.
"""


# Initialization of inconsistent numbers
single_digit = {
    1:3,
    2:3,
    3:5,
    4:4,
    5:4,
    6:3,
    7:5,
    8:5,
    9:4,
    0:0}

double_digit = {
    00:0,
    10:3,
    11:6,
    12:6,
    13:8,
    14:8,
    15:7,
    16:7,
    17:9,
    18:8,
    19:8,
    20:6,
    30:6,
    40:5,
    50:5,
    60:5,
    70:7,
    80:6,
    90:6}


def number_letter_count():
    """Returns the total number of letters needed to write out all
    numbers up to 1000 in words."""
    count = len('onethousand')

    for i in range(1, 1000):
        c = count
        numlen = len(str(i))
        for j in range(numlen, 0, -1):
            curr_digit = int(str(i)[numlen-j])

            # Hundreds case
            if j == 3:
                count += single_digit[curr_digit] + len('hundred')
                if str(i)[-2:] == '00':
                    break
                else:
                    count += len('and')

            # Tenths case
            elif j == 2:
                twodigits = int(str(i)[-2:])

                if twodigits in double_digit:
                    count += double_digit[twodigits]
                    break
                else:
                    count += double_digit[int(str(curr_digit)+'0')]

            # Ones case
            else:
                count += single_digit[curr_digit]
    return(count)


if __name__ == "__main__":
    print(number_letter_count())
