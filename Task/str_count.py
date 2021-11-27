'''Print all the repeated characters and count occurrences of that character'''

str1 = "karnataka"
dummy = []
for char in str1:
    if str1.count(char) > 1:
        if char not in dummy:
            dummy.append(char)
print(dummy)
# print("K Occured:", str1.count("k"), "times")
# print("A Occured:", str1.count("a"), "times")


