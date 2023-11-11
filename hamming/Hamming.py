

import numpy as np
import pprint
class Hamming:

    def __init__(self):

        self.tet = ""


testing = "000010010000001000000001100000000100:530CQI9e4560a7c1266d8CQIb5fCQI8dCQIa328c3ecfCQId91b763eb0dCQIaa4d2424c1fCQId7fd31f3134806b9695e309dCQIced13cf9a43549fa2183742e7c63"

permutationMatrix = testing.split(':')[0]
cqiNonsense = testing.split(':')[1]


def cqiToBinary(cqi):

    cqiMapping = {
        '0': '0000', '1': '0001', '2': '0010', '3': '0011',
        '4': '0100', '5': '0101', '6': '0110', '7': '0111',
        '8': '1000', '9': '1001', 'a': '1010', 'b': '1011',
        'c': '1100', 'd': '1101', 'e': '1110', 'f': '1111',
        'CQI' : '10000',
    }


    res = ""

    i = 0
    while i < len(cqi):

        if cqi[i] == 'C':
            res += cqiMapping['CQI']
            i += 3

        else:
            res += cqiMapping[cqi[i]]
            i += 1

    return res
