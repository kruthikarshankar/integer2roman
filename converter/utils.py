__author__ = 'kruthika'

# Symbol map for conversion from Integer to Roman numeral
symbol_map = (("M", 1000), ("CM", 900), ("D", 500), ("CD", 400), ("C", 100), ("XC", 90), ("L", 50), ("XL", 40),
              ("X", 10), ("IX", 9), ("V", 5), ("IV", 4), ("I", 1))


def int2roman(n):

    '''
        Converts an integer between 1 and 3999 to Roman numeral
        Input: Integer (n)
        Output: Roman numeral
    '''

    # Checking for exceptions. (Second level.)
    if not isinstance(n, int):
        raise NotAnIntegerError("Only integers can be converted to roman")
    if not (0 < n < 4000):
        raise OutOfRangeError("Entered number should be in the range 1 to 3999")

    # Calculating roman numeral value by using divmod
    roman_value = []
    for symbol, value in symbol_map:
        (m, n) = divmod(n, value)
        roman_value.append(symbol * m)
    return "".join(roman_value)


# Defining basic exception classes
class ConversionError(Exception):
    pass


class OutOfRangeError(ConversionError):
    pass


class NotAnIntegerError(ConversionError):
    pass

