import sys

with open(sys.argv[1],'r') as input:
    with open(sys.argv[2],'w') as output:
        while True:
            triple = input.read(3)
            if not triple: break
            ones = triple.count('1')
            if ones >= 2:
                output.write('1')
            else:
                output.write('0')





