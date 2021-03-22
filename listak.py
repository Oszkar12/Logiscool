names = ["Anna", "Béla", "Dávid", "Bence"]

print(names[0])

print("The length of the list is: ", str(len(names)))

#beépített parancs lista létrehozáshoz

num  = list( ( 1,2,3,4,5,6,7,8 ) )

nevek = [ "Anna", "Elizabeth", "George", "Tom", "Adam", "Chris", "Peter"]
"""
# task 1



j = len(nevek)


while j > len(nevek) - 1 or j < -len(nevek):
    j = int(input("Give me a valid index\n"))
    if j < len(nevek) and j >= -len(nevek):
        print(nevek[j])
    else:
        print("There is no item in the list.")
"""

"""
# task 2
szam = 0
i = 0

for j in nevek:
    print(j)
    szam += 1

while i < len(nevek):
    szam += 1
    print(nevek[i])
    i += 1
print(szam)
"""

# task 3

lista = []

i = 0
while i < 60:
    lista.append(i)
    i += 1
print(lista)
