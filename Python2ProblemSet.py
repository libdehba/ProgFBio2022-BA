#!/usr/bin/env python3
import sys
TestVariable = 'GTACCTTGATTTCGTATTCTGAGAGGCTGCTGCTTAGCGGTAGCCCCTTGGTTTCCGTGGCAACGGAAAA'
if 'WWW' in TestVariable:
  print('found in seq')
else:
  print('seq not found') 

# Just leaving a space for the next problem. Problem 3
TestNum = 1857
if TestNum < 0:
  print('Negative')
if TestNum > 0:
  print('positive')

# Another example that includes a mixed variable, ie, a number and a letter
MixedVariable = '5HT7'
if '5' in MixedVariable:
  print('found') 
else:
  print('Not found')


#Problem 4-8 (nested test)
TestNum = int (sys.argv[1])
print (TestNum)
if TestNum < 0:
  print('Negative')
elif TestNum > 0:
  print('Positive')
else:
  print('equal to 0')
  if TestNum < 50:
   print('less than 50') 
  if TestNum % 2 ==0: 
   print('it is an even number and smaller than 50')
  else:
   print('it is larger than 50')
   if TestNum / 3 ==111:
    print('it is divisible by 3')  



# Problem 9

