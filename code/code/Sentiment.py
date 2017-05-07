"""
Nisarg worked on this.
"""

import json
from pattern.en import positive


def main():
    i = 0
    f = open('Bernie_NYC.txt', "r")
    for line in f:
        #tweet = json.loads(line)
        if positive(str(line), threshold=0.1):
            file = open('Bernie_Positive_tweets.txt', "a")
            file.write(json.dumps(line) + '\n')
            i += 1
            file.close()
        else:
            file1 = open('Bernie_Negative_tweets.txt', "a")
            file1.write(json.dumps(line) + '\n')
            file1.close()


if __name__ == '__main__':
    main()
