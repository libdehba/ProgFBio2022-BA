#!/usr/bin/env python

import os, sys, re



## method: seq_list_from_fastq_file(fastq_filename)
##
##  Extracts the sequence lines from a fastq file and returns a list
##  of the sequence lines
##
##  input parameters:
##
##  fastq_filename :  name of the fastq file (type: string)
##
##  returns seq_list : list of read sequences.
##                    ie.  ["GATCGCATAG", "CGATGCAG", ...]
    



def seq_list_from_fastq_file(fastq_filename):
:w
    seq_list = list()


    line_counter = 0
    with open(fastq_filename, 'r') as doc:
      for line in doc:
          line = line.rstrip()
          line_counter +=1
#The document is being read line by line. I just need to tell it to read the lines that contain the sequence which are the second line every 4 lines of file.  
          if line_counter %4 == 2:
            print(line)
            seq_list.append(line)
            print(line_counter)

    return seq_list 

#print(seq_list_from_fastq_file('reads.fq'))


def sequence_to_kmer_list(sequence, kmer_length): 
    count = 0
    kmer_list = [] 
    for nt_position in range(0 , (len(sequence)-kmer_length +1)):
 #     print(nt_position)   
      kmer_list.append(sequence[nt_position:nt_position + kmer_length])




    return kmer_list

seq_list_needed = seq_list_from_fastq_file('reads.fq')
for seq in seq_list_needed:
#  print(sequence_to_kmer_list(seq, 5))

  kmer_list2 = sequence_to_kmer_list(seq, 5)
  kmer_list_organized = kmer_list2[0:1]
  print(kmer_list_organized.sort())i
#need to add a for loop to iterate through my kmers list
#  print(kmer_list2)




 # sorted = list.sort(sequence_to_kmer_list(seq, 5))
 # print(sorted)


#print(sequence_to_kmer_list('ATGTTTACGTAGCTAGTAGATGATGA', 5))






    ## end your code

#    return seq_list



#def main():

#    progname = sys.argv[0]
    
#    usage = "\n\n\tusage: {} filename.fastq num_seqs_show\n\n\n".format(progname)
    
#    if len(sys.argv) < 3:
#        sys.stderr.write(usage)
#        sys.exit(1)

    # capture command-line arguments
#    fastq_filename = sys.argv[1]
#    num_seqs_show = int(sys.argv[2])

#    seq_list = seq_list_from_fastq_file(fastq_filename)

#    print(seq_list[0:num_seqs_show])

#    sys.exit(0)  # always good practice to indicate worked ok!



#if __name__ == '__main__':
#    main() 


#_______________________________ Brian's Answers___:
#First Challenge: same as above
#2nd channgele:see about
#3rd part: 
#combining the first 2 parts: count the kamers
#part 1 of this
