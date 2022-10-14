#!/usr/bin/env python3

#Q1:
faves = { 'book' : 'Jitterbug Perfume' , 'song' : 'Tom Petty-I wont back down' , 'tree' : 'Cedar' }
print(faves['book'])

fave_thing = 'book'
print(faves[fave_thing])

#Q4
fave_thing2 = 'tree'
print(faves['tree'])

#Q5
faves = { 'book' : 'Jitterbug Perfume' , 'song' : 'Tom Petty-I wont back down' , 'tree' : 'Cedar' }
faves['fav_thing'] = "organism"
print(faves)
faves['trialkey'] = "test Try"
print(faves)


#Q6
faves = { 'book' : 'Jitterbug Perfume' , 'song' : 'Tom Petty-I wont back down' , 'tree' : 'Cedar' }
access = input('your key')
if access in faves:
 print(faves[access])
 print('exist')
else:
 print('doesnt exist')

#Q7
faves = { 'book' : 'Jitterbug Perfume' , 'song' : 'Tom Petty-I wont back down' , 'tree' : 'Cedar' }
faves['fave_thing'] = "bacteria"
print(faves)

#Q8



  
