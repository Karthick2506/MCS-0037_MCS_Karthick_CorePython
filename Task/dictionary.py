dict1 = {
    "x": 500,
    "y": 897,
    "z": 345,
    "i": 809,
    "a": 900,
    "b": 122,
    "c": 456
}
print("The values in the dictionaries are:", dict1.values())
max_val = max(dict1.values())
min_val = min(dict1.values())
print("The Maximum Value in the Dictionary:", max_val)
print("The Maximum Value in the Dictionary:", min_val)
print("--------The first 3 highest value in a dictionary--------")
sorted_val = sorted(dict1.values(), reverse = True)
count = 0
print("The Highest 3 values in a dictionary are:")
for i in sorted_val:
    print(i)
    count = count + 1
    if count == 3:
        break


