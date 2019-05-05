def convBitsToBytes(fileName):
    intTab = []
    output = []

    with open(fileName, 'r') as input:
        while True:
            byte = input.read(8)
            if not byte:
                break;
            intTab.append(byte)
        intTab.pop()

        for oneInt in intTab:
            output.append(int(oneInt, 2))
        intTab.clear()

        intTab = bytearray(output)
        return intTab
