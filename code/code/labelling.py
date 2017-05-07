"""
Nisarg worked on this.
"""


import json
from pattern.en import positive


def main():
    i = 0
    i1=1786
    f = open('Bernie_Negative_tweets.txt', "r")
    f1 = open('bernie_nyc_0.txt', "w")
    for line in f:
        test = []
        test.append(i)
        test.append(0)
        test.append(line)
        i += 1
        f1.write(json.dumps(test))
        f1.write('\n')

    f = open('Bernie_Positive_tweets.txt', "r")
    f1 = open('bernie_nyc_1.txt', "w")
    for line in f:
        test = []
        test.append(i1)
        test.append(1)
        test.append(line)
        i1 += 1
        f1.write(json.dumps(test))
        f1.write('\n')

if __name__ == '__main__':
    main()
