#  CPF (Brazilian document for civilian)

documentNumber = input('Type your CPF document (Only numbers): ')

newCPF = documentNumber[:-2]
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

sequence = newCPF == str(newCPF[0]) * len(documentNumber)

if documentNumber == newCPF and not sequence:
    print('valid')
else:
    print('Invalid')

print(newCPF)
