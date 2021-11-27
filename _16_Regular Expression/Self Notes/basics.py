"""Regular Expression"""
'''
Regular Expression is a sequence of characters that defines a search pattern.
'''




import re
test_str = "hai i am karthick"
x = re.search("^am$", test_str)
if x:
    print("it is present")
else:
    print("it is not present")


'''
RegEx Functions

The re module offers a set of functions that allows us to search a string for a match:

1. findall :	Returns a list containing all matches
2. search  :	Returns a Match first occurence object if there is a match anywhere in the string
3. split   :	Returns a list where the string has been split at each match
4. sub     :	Replaces one or many matches with a string

'''
'''
. - Period
A period matches any single character (except newline '\n').

^ - Caret
The caret symbol ^ is used to check if a string starts with a certain character.

$ - Dollar
The dollar symbol $ is used to check if a string ends with a certain character.

* - Star
The star symbol * matches zero or more occurrences of the pattern left to it.

+ - Plus
The plus symbol + matches one or more occurrences of the pattern left to it.

? - Question Mark
The question mark symbol ? matches zero or one occurrence of the pattern left to it.

{} - Braces
Consider this code: {n,m}. This means at least n, and at most m repetitions of the pattern left to it.

\A - Matches if the specified characters are at the start of a string.

\b - Matches if the specified characters are at the beginning or end of a word.

\B - Opposite of \b. Matches if the specified characters are not at the beginning
or end of a word.

\d - Matches any decimal digit. Equivalent to [0-9]
\D - Matches any decimal digit. Equivalent to [0-9]

[abc]----> a, b or c
[^abc]----> anycharacter except a b c
[a-z]----> a to z
[A-Z]----> A to Z
[a-z A-Z]----> a to z, A to Z
[0-9]----> 0 to 9

Quantifiers:
------------
[  ]?  occurs 0 or 1 time

[  ]+  occurs 1 or more times

[  ]*  occurs 0 or more times

[  ]{n}  occurs n times

[  ]{n,}  occurs n or more times

[  ]{y,z}  occurs atleast y times but less than z times

'''
