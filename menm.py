import random

kleurenList = ["oranje", "geel", "groen", "bruin"]

def zakkenVullerList(nummer):
    list = []
    for x in range(0, nummer):
        kleur = kleurenList[random.randint(0, len(kleurenList)) - 1]
        list.append(kleur)
    return list

def zakkenVullerDictionary(nummer):
    dictionary = {}
    for x in range(0, nummer):
        kleur = kleurenList[random.randint(0, len(kleurenList)) - 1]
        try:
            if dictionary[kleur] > 0:
                dictionary[kleur] += 1
        except:
            dictionary[kleur] = 1
    return dictionary

inputNum = int(input("Vul hier een nummer in:\n"))
print(zakkenVullerList(inputNum))
print(zakkenVullerDictionary(inputNum))