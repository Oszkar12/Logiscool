
"""

# task 1 - Akasztófa
life = 9

puzzle = input("Kitalálandó szó:")


puzzle = []
for betu in puzzle_in:
    puzzle.append(betu)

my_solution = []


for betu in puzzle:
    if betu == " ":
        my_solution.append(" ")
    else:
        my_solution.append("*")

while life > 0 and puzzle != my_solution:
    print()
    # Kiíratás a kialálandó szónak
    for betu in my_solution:
        print(betu, end = "")

    print("")

    # incoming guess letter
    tip = input(" Tip a letter:\n")


    for i,betu in enumerate(puzzle):
        if tip == puzzle[i]:
            my_solution[i] = tip
    else:
        print("incorrect guess")




if life>0:
    print("You won")
else:
    print("Game over dude")

"""

"""
#  task 2 - prime factor of a number

szam = int(input("Adj meg egy számot\n"))

prime_factor= []

i = 2
while 1 < szam:
    while szam % i == 0:
        szam /= i
        prime_factor.append(i)
    i +=1
print(prime_factor)
"""

# lkkt

num_1 = int(input("Adj meg egy számot\n"))
num_2 = int(input("Adj meg egy másik számot\n"))


if num_1 > num_2:
    lcm = num_1
else:
    lcm = num_2



