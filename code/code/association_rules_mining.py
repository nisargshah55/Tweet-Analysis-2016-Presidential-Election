"""
Neel and Nisarg worked on this.

"""
import Orange
import json


raw_data = []
f1=open('association_training.txt', "r")
for line in f1:
    raw_data.append(json.loads(line))

a='\n'
#write data
f = open('data.basket', 'w')
for item in raw_data:
    b=str(item)
    f.write(b)
    f.write('\n')

f.close()

# Load data from the text file: data.basket
data = Orange.data.Table("data.basket")



rules = Orange.associate.AssociationRulesSparseInducer(data, support = 0.5)


# print out rules
print "%4s %4s  %s" % ("Supp", "Conf", "Rule")
for r in rules[:]:
    print "%4.1f %4.1f  %s" % (r.support, r.confidence, r)

rule = rules[0]
for idx, d in enumerate(data):
    print '\nUser {0}: {1}'.format(idx, raw_data[idx])
    for r in rules:
        if r.applies_left(d) and not r.applies_right(d):
            print "%4.1f %4.1f  %s" % (r.support, r.confidence, r)

