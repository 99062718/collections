import random

spelList = ['Monopoly', 'Yathzee', 'Bridge', 'Poker', 'Pesten', 'Mens erger je niet', 'Cluedo']

def spelProgramma(spelList, minimum, maximum):
    newSpelList = []
    aantalLoops = random.randint(minimum, maximum)
    for x in range(aantalLoops):
        randomNum = random.randint(0, len(spelList) - 1)
        newSpelList.append(spelList[randomNum])
    return newSpelList

print(spelProgramma(spelList, 2, 4))