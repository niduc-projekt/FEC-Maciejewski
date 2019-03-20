import random, sys

probability = float(sys.argv[1])

with open(sys.argv[2],'r') as input:
    with open(sys.argv[3],'w') as output:
        while True:
            i = input.read(1)
            if not i: break
            if random.random() < probability:
                i = str((int(i)+1)%2)
            output.write(i)