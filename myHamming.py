from hamming import encode, decode, syndrome, correct, str_to_bin
import itertools
import numpy as np

input = '1010101010101010101111101011'#przykladowe wejscie, ciagi nie musza byc wielokrotnoscia 8

def zakoduj(input):#input jako string 0 i 1, funkcja koduje i przygotowuje dane wyjsciowe do przejscia przez kanal
    binar_input = str_to_bin(input)
    encodedd_data = encode(binar_input)
    #print(encodedd_data)
    cos = list(itertools.chain.from_iterable(encodedd_data.tolist()))#cos to lista 0 i 1 po zakodowania gotowa od przejscia przez kanał
    #print(cos)
    return cos #zwraca liste np. [0,1,0,1,1] gotowa do przejscia przez kanal

def zdekoduj(input): #funkcja przywraca liste do formy kompatybilnej z bilioteka, wykonuje naprawe kodem Hamminga i zwraca zdekodowana liste jako wyjscie kanalu
    cos =np.reshape(np.array(input), (-1, 8))#powrot do poprzedniej formy list listy kompatybilnej z biblioteka, uzywane po powrocie z kanalu
    #print(cos)
    syndrom = syndrome(cos)
    corected = correct(cos, syndrom)#proba naprawy bledow w kodzi
    myoutput = decode(corected)#dekodowanie kodu hamminga
    #print(myoutput)
    return myoutput#funkcja zwraca liste zdekodowana

def wydrukuj(myoutput):#przyjmuje liste 0 i 1 do wydrukowania
    with open('wyjscie.txt', 'w+') as output:
        for numb in myoutput:
            output.write(str(numb))
