#  Generating a random CPF number 
from random import randint

number = str(randint(100000000, 999999999))

newCPF = number
reverse = 10
total = 0

for index in range(19):
    if index > 8:
        index -= 9

    total += int(newCPF[index]) * reverse

    reverse -= 1
    if reverse < 2:
        reverse = 11
        d = 11 - (total % 11)

        if d > 9:
            d = 0
        total = 0
        newCPF += str(d)

print(newCPF)
