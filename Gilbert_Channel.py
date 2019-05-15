import random, sys


def passing(G_B, B_G, errorInGood, errorInBad, data):#dla listy danych wersja
    state=1                 #1-GOOD 0-BAD
    probG_B=G_B             #0.01 szansa na przejscie do zlego stanu
    #probG_G =1- G_B        # 0.99 szansa zostania w dobrym stanie---niepotrzebne
    probB_G=B_G             #szansa wrocenia do dobrego stanu, 1/B_G to srednia dlugosc serii bledow seria dlugosci 10= B_G= 0.1
    #probB_B =1-B_G         #szansa zostania w zlym stanie---niepotrzebne
    output =[]

    for bit in data:
        if state == 1:
            if random.random() < probG_B:
                state = 0
            if random.random() < errorInGood:  # prawd. wystapienia bledu w stanie 1
                bit = (bit + 1) % 2  # zamiana bitu 1 na 0 i na odwrot
        else:
            if random.random() < probB_G:
                state = 1
            if random.random() < errorInBad:  # prawd. wystapienia bledu w stanie 0
                bit = (bit + 1) % 2  # zamiana bitu 1 na 0 i na odwrot
        output.append(bit)

    #print(output)
    return output