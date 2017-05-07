# -*- coding: utf-8 -*-
"""
Created on Wed May 11 19:41:22 2016

@author: Nisarg
"""

import json
from pattern.en import positive


def main():
    i = 0
    f = open('TRUMP_DC_DATA.txt', "r")
    for line in f:
        #tweet = json.loads(line)
        if positive(str(line), threshold=0.1):
            file = open('trump_dc_positive.txt', "a")
            file.write(json.dumps(line) + '\n')
            i += 1
            file.close()
        else:
            file1 = open('trump_dc_negative.txt', "a")
            file1.write(json.dumps(line) + '\n')
            file1.close()


if __name__ == '__main__':
    main()