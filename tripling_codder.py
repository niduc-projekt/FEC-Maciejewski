import sys

with open(sys.argv[1],'r') as input:
    with open(sys.argv[2],'w') as output:
        while True:
            i = input.read(1)
            if not i: break
            for n in range(0,3):
                output.write(i)