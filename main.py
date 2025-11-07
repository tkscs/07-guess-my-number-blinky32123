# the user will choose a number
# this program will guess the number
# the user will say "yes" or "higher" or "lower"
# the program will ask to play again or exit


import random as r
x=7 #(1-10)
min_y = 1
max_y = 10
print( min_y, " ", max_y)
y=r.randint(min_y,max_y)
print(y)
guess = 1

while (y != x) : 
    z=input(f"my number is:")
    if z=="higher":
        min_y = y
    elif z=="lower":
        max_y = y

    print( min_y, " ", max_y)
    y=r.randint(min_y,max_y)
    print(y)
    guess = guess + 1

if (y == x):
    print("I won in", guess, "guesses")    