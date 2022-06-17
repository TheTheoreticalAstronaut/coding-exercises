# Implement a function that takes as input a list of strings and returns
# that same list with (i) any upper case alphabetical characters converted
# to lower case, and (ii) sorted. Notice the order: strings should first be
# converted to lower case and only then sorted.
#
# Sorting rules:
# 1) The strings in the input will only contain the characters a-z, A-Z, 0-9 and ' ' (space).
# 2) The sorting order is ' ' (space), 0-9, a-z.
#    Example: if input=["G", " ", "2"], then output=[" ", "2", "g"].
# 3) The input may contain empty strings. If so, these should come before any non-empty strings.
# 4) The input strings may contain several characters. If so, the first non-matching character decides the order.
#    Example: if input=["HI", "hElLO"], then output=["hello", "hi"].
# 5) Numbers should be matched according to the sorting order of their digits.
#    Example: if input=["8", "20"], then output=["20", "8"].
# 6) If there are no non-matching characters between two strings, the one with the lowest number of characters comes first.
#    Example: if input=["Hello World", "hello"], then output=["hello", "hello world"].
def sort_strings_lowercase(list):
    pass
