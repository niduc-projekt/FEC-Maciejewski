import random, sys

with open(sys.argv[1],'w') as file:
    #print(sys.argv[1])
    amount = int(sys.argv[2])
    for i in range(0,amount):
        file.write(str(random.randint(0,1)))