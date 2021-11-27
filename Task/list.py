'''list contains group of strings. convert each word to capital letter and print'''
li1 = ["hai", "hello", "everybody"]
print("List before converting:", li1)
li2 = []
for i in li1:
    up = i.upper()
    li2.append(up)
print("List after converting:", li2)

