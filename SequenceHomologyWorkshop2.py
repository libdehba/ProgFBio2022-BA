#!/usr/bin/env python3
import re
import sys
#ss_rand5_200_v_qfo_BL50.txt = sys.argv[0]
#imput = sys.argv[1]

hit_files = []
hit_list = []

for this_data in sys.argv[1:]: 

    with open (this_data , 'r') as seqhomWS:
      for line in seqhomWS:
#        line = line.rstrip()
        if line[0] == '#':
          continue
        this_data = dict(zip(fields,line.strip('\n').split('\t')))
        this_data['file'] = (
    

    else:
      line = this_data.update(line.split('\t')
#      this_data.append(field_names.join(line.split('\t')))
#      result = line.split('\t')
#      this_data.append
#      this_data = dict(zip(field_names , line.split('\t'))) 
print(line)



#Refer to solution located in gitbhub repository workshop solutions 
