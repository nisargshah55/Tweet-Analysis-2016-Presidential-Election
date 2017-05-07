# -*- coding: utf-8 -*-
"""
Created on Wed May 11 22:54:54 2016

@author: Nisarg
"""

import json
from pattern.en import positive

def main():
    i = 0
    i1=1909
    f = open('TRUMP_MILWAUKEE_DATA.txt', "r")
    f1 = open('trump_milwaukee_testing.txt', "w")
    for line in f:
        test = []
        test.append(i)
        test.append(line)
        i += 1
        f1.write(json.dumps(test))
        f1.write('\n')

    

if __name__ == '__main__':
    main()