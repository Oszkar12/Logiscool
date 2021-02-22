''''
print("Macska".replace('a','e'))

print(input("Adj meg egy szöveget:\n"))

print(input("Adj meg egy szöveget:\n").__len__())

print(input("Adj meg egy szöveget:\n").count())

print(input("Adj meg egy szöveget:\n").split(" "))

print(input("Adj meg egy szöveget:\n").capitalize())


print(input("Adj meg egy szöveget:\n").find("lorem"))

print(input("Adj meg egy szöveget:\n").startswith("lorem"))
'''
# print(input("Adj meg egy szöveget:\n").endswith("dolor"))
# 1.feladat
print("You will face many defeats in life, but never yourself be defeated".count(" ") + 1)
# 2.feladat
word = input("which word to find:")
x = []
string = "You will face many defeats in life, but never yourself be defeated"
x = string.split(" ")
print(x)
for a in x:
    if a == word:
        print(a.upper())
