# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 21:49:15 2016

@author: Nisarg
"""

import json
from pattern.en import sentiment
from pattern.en import positive




global id
id=0

f=open('Atlanta.txt')
f1=open('AtlantaF.txt','w')

 
with open('AtlantaF.txt', 'w') as f1:
    for line in open('Atlanta.txt'):
              
              items = [id,line]
              f1.write(json.dumps(items)+'\n')

                
		     
               
              id+=1

f.close()
f1.close()
