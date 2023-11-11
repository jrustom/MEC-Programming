

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
        '0': '00000', '1': '00001', '2': '00010', '3': '00011',
        '4': '00100', '5': '00101', '6': '00110', '7': '00111',
        '8': '01000', '9': '01001', 'a': '01010', 'b': '01011',
        'c': '01100', 'd': '01101', 'e': '01110', 'f': '01111',
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
