import myHamming
from generator import generate_bits
from Gilbert_Channel import passing
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt

quantity_parameters = [100000, 200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000, 1000000]

#GtoB, BtoG, errorInGood, errorInBad
gilbert_parameters = [(0.000101648, 0.914789, 0.000001, 0.31,'idealny'), (0.000196854, 0.509547, 0.000053513, 0.65, 'dobry'),
                      (0.000396854, 0.2768, 0.0003631513, 0.9, 'niezly'), (0.00496854, 0.2768, 0.000053513, 0.9, 'sredni'),
                      (0.00496854, 0.04, 0.0003631513, 0.99999, 'zly'), (0.00496854, 0.004, 0.0003631513, 0.99999, 'fatalny')]

alfa_list = []
BER_list = []

####HAMMING

for parameters in gilbert_parameters:
    for quantity in quantity_parameters:
        bitsList = generate_bits(quantity)
        bits = ''.join(str(x) for x in bitsList)
        encode = myHamming.zakoduj(bits)
        alfa = len(encode)/len(bitsList)
        #print('%.15f'%alfa)
        corrupted = passing(parameters[0],parameters[1],parameters[2],parameters[3], encode)
        decode = myHamming.zdekoduj(corrupted)

        # print(bitsList)
        # print(decode)
        #policzenie bledów
        errors = 0
        for i in range(len(bits)):
            if bitsList[i] != decode[i]:
                errors+=1
        #print(errors)
        BER = errors/len(bitsList)
        #BER_list[index].append(BER)
        print('BER dla '+str(quantity)+' '+parameters[4]+' %.15f'%BER)

######BCH
