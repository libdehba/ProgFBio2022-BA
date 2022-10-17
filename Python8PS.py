#!/usr/bin/env python3
import re


#With this file type we were provided (the fasta file), the first line with > will be read and one and the sequence itself is the other line. Need to create a dictionaty to include this file. within this dict I need to open another dictionary and identify the key as the gene ID (first line info) and the sequence as my value. Now my sequence(value) has 4 different characters, so I have to create another dictionary to specifify those indiivudl nt so now my key is nucleotides and my value is the the individual nucleotide (ATGC). and now because I want to count how many As Ts Cs and Gs are in each line, i have to use +=1 after I call onto my sub dict. Remeber that to call the dict you type the outer dict first in bractets like [dict1] then the inner dict  [dict1][innerdict] then keep going until you hit the deepest dict you have [dict1][innerdict][deeperdict][deepestdict]... You can then call onto individual elements of that dict and execute things to it like counting as we did in this example. 

#This is another example from Shasta of a simpler dict within a dict within a dict. The name of the dict is myFoods. Within that, we have 2 keys which are breakfasts and lunches. Each of those opens another dict includes sweet,savory,and delicious. Those are also keys for another sub dict. 
#myFoods
#{'breakfasts': {'sweet': 'pancakes', 'savory': 'toast', 'delicious': 'bagel'}, 'lunches': {'sweet': 'fruit salad', 'savory': 'sandwich', 'delicious': 'soup'}}
#>>> myFoods['breakfasts']
#i{'sweet': 'pancakes', 'savory': 'toast', 'delicious': 'bagel'}
#>>> myFoods['breakfast']['sweet']
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#KeyError: 'breakfast'
#>>> myFoods['breakfasts']['sweet']
#'pancakes'
#>>> myFoods['breakfasts']['sweet'] = 'cereal'
#>>> myFoods['breakfasts']['sweet']
#'cereal'
 #______________________________________________________________________________________
seqs = {}
nucleotide = ''
with open ('../Python_08.fasta','r') as prob1:
  count = 0
  for line in prob1:
    line = line.rstrip()
    if re.search('>',line):
      if line not in seqs:
#IN THE FOLLOWING LINE, I WANT TO TELL PYTHON THAT WHAT IS COMING IS THE KEY OF THE DICT AND IF IT IS NOT IN THE DICT ALREADY TO ADD IT. IT WILL RECOGNIZE IT BY THE > SPECIFIED IN PREVIOUS CODE
        gene_id = line    
        seqs[gene_id] = {}
    else:
      nucleotides = line
      seqs[gene_id] = {'A' : 0 , 'T' : 0 , 'G' : 0 , 'C' : 0} 
      for nt in nucleotides:
#So now, I want to count the number of ind. nucleotides per line
         if nt == 'A': 
           (seqs[gene_id]['A']) +=1
         if nt == 'T':
           (seqs[gene_id]['T']) +=1
         if nt == 'G':
           (seqs[gene_id]['G']) +=1
         if nt == 'C':
           (seqs[gene_id]['C']) +=1

print(seqs[gene_id]['A'])
print(seqs[gene_id]['T'])
print(seqs[gene_id]['G'])
print(seqs[gene_id]['C'])


#_____________
#Q2:I accidentaly used the input data from problem 1 in PS 10. Redo this this problem with the correct input data 

dna = 'GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGC    TCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTC    AGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGA    TGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACA    CCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCT'
  
  
dna_list = []
codon = '' 
count = 0
junior_list = []
for nt in dna: 
#the following line says that im starting to build my string. so my codon includes my first nt in my dna string
   if count == 3:
#we assign the codon to the dict once it counts 3 nt (goes through the loop 3X)
#After i assign my codon to my dict, i need to clean my string and counter again 
#The join function is to covert a list to a string. In here I am appending my big list by adding my now joined nt(stored in junior list) in my 'empty' string named codon. Then I want to reset the codon count to to an empty string, my count to 0, and my list to empty in order to populate it again.
      dna_list.append(codon.join(junior_list))
      codon =''
      count = 0
      junior_list = []
#My junior list adds my ind.nucleotides
   else:  
      junior_list.append(nt)
      print(junior_list)      
#now i need to add the second nt to my previous line by using the count fxn. I need to do that 3 times. Then i ne    ed to tell it if it gets to 3 then you need to start a new codon
      count += 1
print(dna_list)
  
      
      
#______________________
#PS 8 Q2: 

codons = {}
#codons is a dict of a list
nts = {}
#a dict of dict

with open ('../Python_08.fasta','r') as prob2:
  for line in prob2:
    line = line.rstrip()
    if re.search ('>', line):
        gene_id = line
        nts[gene_id] = {'A' : 0 , 'T' : 0 , 'C' : 0 , 'G' : 0}
        codons[gene_id] = {} 
#the above creates lists inside another dict
        codons[gene_id]['Frame1'] = []
        codons[gene_id]['Frame2'] = []
        codons[gene_id]['Frame3'] = []
#Thus far, ive opened a dict and inside that dict I want to call gene-id my key with my value being the sequence.But i need to do further work on the sequence to break it into codons. If my line has > in the file, I assigned it to the key of the dict and placed it in my outer dict. 
    else: 
        nucleotides = line
        for nt in nucleotides:
          nts[gene_id][nt] +=1     
        codons[gene_id]['Frame1'].append(re.findall(r'...', nucleotides)) 
        codons[gene_id]['Frame2'].append(re.findall(r'...', nucleotides[1:])) 
        codons[gene_id]['Frame3'].append(re.findall(r'...', nucleotides[2:])) 
#          if count2 == 3:
#            codon_list.append(codon.join(codon_list)) 
#            codon = ''
#            codon_list = []
#          else:
#            codon_list.append(nt)
#            print(codon_list)
#            count2 +=1 
print(codons)
print(nts)



#            if nt == 'A':
#              (seqs[gene_id]['A']) +=1
#            if nt == 'T':
#              (seqs[gene_id]['T']) +=1
#            if nt == 'C':
#              (seqs[gene_id]['C']) +=1
#            if nt == 'G':
#              (seqs[gene_id]['G']) +=1
              


#at this point ive just assigned my dictionary and key. Next is to tell it to read in codons
#        for nt in nucleotides:
#          if count == 3:
            
#print(seq[gene_id]['A']





#nt = {'A' , 'T' , 'G' , 'C'} (these are what the keys inside the most internal dict)
# {'A' : 5 , 'T' : 6 , 'C' : 90 , 'G' : 6} 







#     else:
#       seqs[gene_id] = 
    
#    count += 1
#    print(line)
#    seqid1 = line.split(' ', maxsplit=1)
#    seqid2 = seqid1[0]
#print(seqid1)


#      [seqName , tA , code3] = line.split('\t') 
#      if code1 is not in seqs
#        seqs[code1] = {} 
#      if code2 is not in seqs
#        seqs[code1][code2] = {}
#      if code3 is not in seqs
#        seqs[code1][code2][code3] = 0 
  
#    seqs = line.split()
#    seqID = seqs[0]
#    seqseq = seqs [1]
#    print(seqID)
#   else:
#    remainderID = line
#    seqs[ID] = [remainderID]
#print(seqs)
    


#    else:
#     print(seq)


#     if line
#     key = line
  

