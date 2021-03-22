names = ["Anna", "Béla", "Dávid", "Bence"]
"""
print(names[0])

print("The length of the list is: ", str(len(names)))

#beépített parancs lista létrehozáshoz

num  = list( ( 1,2,3,4,5,6,7,8 ) )

nevek = [ "Anna", "Elizabeth", "George", "Tom", "Adam", "Chris", "Peter"]
"""


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
"""
lista = []

i = 0
while i < 60:
    lista.append(i)
    i += 1
print(lista)
print(lista[10:40])
"""

"""
# task 4 - páros és páratlan számok szelekciója

odd_numbers = []
even_numbers = []

j = 0

while j < 20:
    if j % 2 == 1:
        odd_numbers.append(j)
    else:
        even_numbers.append(j)
    j += 1
print(odd_numbers)
print(even_numbers)
"""

"""
# task 5 - append, insert, pop, remove

cars = ["opel", "subaru", "audi", "bmw", "nissan", "Suzuki", "sajt"]

print(cars)
cars.remove("bmw")
cars.pop(3)
print(cars)
cars.insert(1, "jeep")
print(cars)
"""

"""
# task 6 - sum of items

NumberList = [21,245,254,7654,534]
i = 0
szumma = 0

while i < len(NumberList):
    szumma += NumberList[i]
    i += 1
print(szumma)
print(sum(NumberList))
"""