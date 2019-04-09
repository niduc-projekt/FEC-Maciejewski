import bchlib
import hashlib
import os
import random
import numpy
from base64 import b64encode


class BCH:
    def __init__(self, p, b):
        self.bch_polynomial = p
        self.bch_bits = b
        self.obj = bchlib.BCH(self.bch_polynomial, self.bch_bits)

    def encode(self, data):
        data = bytearray(data)
        ecc = self.obj.encode(data)
        packet = data + ecc
        return numpy.array(packet)
        #return packet

    def decode(self, packet):
        packet = bytearray(packet)
        data, ecc = packet[:-self.obj.ecc_bytes], packet[-self.obj.ecc_bytes:]

        decoded = self.obj.decode(data, ecc)
        data_decoded = decoded[1]

        return numpy.array(data_decoded)
        #return data+ecc

    def bitflip(self, packet):
        byte_num = random.randint(0, len(packet) - 1)
        bit_num = random.randint(0, 7)
        packet[byte_num] ^= (1 << bit_num)
        return packet


my_BCH = BCH(8219,16)#tworzenie obiektu BCH
data = os.urandom(512)#losowanie 512 bajtow danych
print(numpy.array(bytearray(data)))#pokaz wylosowane bajty
print('\n')

data_encoded = my_BCH.encode(data)#kodowanie danych
print(data_encoded)#drukowanie zakodowanych danych
print('\n')

for _ in range(1024):#psucie zakodowanych danych
    data_coruptet = my_BCH.bitflip(data_encoded)

print(data_coruptet)
print('\n')

data_decoded = my_BCH.decode((data_coruptet))#dekodowanie zepsutych danych

print(data_decoded)

if numpy.array(bytearray(data)).all() == data_decoded.all():
    print('udalo sie')
else:
    print('porazka')