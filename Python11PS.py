#!/usr/bin/env python3

#The following is the recipe
class DNARecords(object):
  def __init__(self, sequence, gene_name, organism):
    #sequence = 'ATGCCGTGAATGCCCGGTAAAA'
    #gene_name = '5HT7'
    #organism = 'bacteria'

    self.sequence = sequence
    self.gene_name = gene_name
    self.organism = organism

  def get_AT(self):
    length = len(self.sequence)

#cooking the recipe
dna_rec_obj = DNARecords('ATGCCGTGAATGCCCGGTAAAA', '5HT7' , 'bacteria')    
#final product
print(dna_rec_obj.sequence.lower())
print(dna_rec_obj.gene_name)
print(dna_rec_obj.organism)


print(get_AT)



#________ Recreating the notes  ________
#class DNARecord(object):
#  def__init__ (self, sequence, gene_name, species_name):
#    self.sequence = sequence
#    self.gene_name = gene_name
#    self.species_name = species_name

#_______Online Example:Human Example_______

#We have a company and we want to represent employees. Each employee is a class becuase each one has diff attributes and methods like first and last name, email, and pay as well as actions they perform:

#lets create a simple employee class

#class employee:
#im leaving it empty for now but this will produce an error so choose to pass it for now
#  pass

# @2:46 so now we have a simple employee class with no attributes or methods

 


