import random

kleuren = ["oranje", "geel", "groen", "bruin"]

def zakkenVuller(nummer):
    list = []
    for x in range(0, nummer):
        kleur = kleuren[random.randint(0, len(kleuren)) - 1]
        list.append(kleur)
    return list

inputNum = int(input("Vul hier een nummer in:\n"))

print(zakkenVuller(inputNum))