

f = open("sample2.txt", 'w')

# print(f)
# print("hello")

text = f.write("Neha")

print(text)
f.close()


f = open("sample2.txt", 'r')

text = f.read()
print(text)

