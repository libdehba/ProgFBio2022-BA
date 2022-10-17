#!/usr/bin/env python3
import re

#Question 1 From PS 8. Accidentaly stored in this problem set. It is already backed up in PS8 but keep here just in case:

#Create a function to format a string of DNA so that each line is no more than 60 nt long. Your function will:
#INPUT: a string of DNA without newlines
#OUTPUT: a string of DNA with lines no more than 60 nucleoties long


dna = 'GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCT'


dna_list = []
codon = ''
count = 0
junior_list = []
for nt in dna: 
#the following line says that im starting to build my string. so my codon includes my first nt in my dna string
    if count == 3:
#we assign the codon to the dict once it counts 3 nt (goes through the loop 3X)
#After i assign my codon to my dict, i need to clean my string and counter again 
      dna_list.append(codon.join(junior_list))
      codon =''
      count = 0
      junior_list = [] 
    else:  
      junior_list.append(nt)
      print(junior_list)      
#now i need to add the second nt to my previous line by using the count fxn. I need to do that 3 times. Then i need to tell it if it gets to 3 then you need to start a new codon
      count += 1
print(dna_list)

#print(dna_list)
    


#dna_dict.append = 'ATT'







#def dna_codons(dna):









#  codon_start = 0
#  codon_length = 3
#  codon_end = 3
#  codon_list = []
#  for nt in dna:
    



#  for nt in range(len(dna) // codon_length):
#    codon_list.append(dna[codon_start:codon_end])
#    codon_start += codon_length
#    codon_end += codon_length
#print(dna_codons)
  


#  count = 0
#for nt in dna:
#  count = 0
#  while count [0:59]:
#    print(count)
#  else:
#    print('not done') 





#c_count = dna.count('G')
#g_count = dna.count('C')
#dna_len = len(dna)
#gc_content = (c_count + g_count) / dna_len
#print(gc_content)

#  for nt in dna:
#    while 
#I want to index and slice my sequence and run it in a while loop until it reaches the end of the sequence
    

#def nt in dna:
#    gnt_count = dna.count('G')
#    tnt_count = dna.count('T')
#    totalcount = gnt_count + tnt_count
#  print(totalcount)

