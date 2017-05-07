"""
Neel worked on this.
"""
import json
from pattern.en import positive

def main():
    i = 0
    i1=1909
    f = open('Bernie_NYC.txt', "r")
    f1 = open('bernie_nyc_testing.txt', "w")
    for line in f:
        test = []
        test.append(i)
        test.append(line)
        i += 1
        f1.write(json.dumps(test))
        f1.write('\n')

    

if __name__ == '__main__':
    main()