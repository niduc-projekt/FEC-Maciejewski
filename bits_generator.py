import random, sys

with open('bits.txt','w') as file:
    #print(sys.argv[1])
    amount = int(sys.argv[1])
    for i in range(0,amount):
        file.write(str(random.randint(0,1)))