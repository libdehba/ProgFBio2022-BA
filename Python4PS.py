#!/usr/bin/env python3
print('begin')
favorites = ['read' , 'write' , 'lift' , 'hike' , 'tv']
print(favorites)
print(favorites[2])
favorites[2] = 'song'
print(favorites) 
print(favorites)
copy_favorites=favorites
copy_favorites.append('sleep')
print(favorites)
copy_favorites.insert(0 , 'run')
print(favorites)
copy_favorites.insert(1 , 'eat')
print(favorites)
copy_favorites.pop(0)
print(favorites)
copy_favorites.pop(5)
print(favorites)
copy_favorites.pop(3)
print(favorites)
stringtoaddtolist = ' ,jog ,'
x = stringtoaddtolist.join(copy_favorites)
print(x)

taxa = 'sapiens' , 'erectus' , 'neanderthalesis'
print(taxa)
print(taxa[1])
print(type(taxa))
species = taxa
print(species)
print(species[1])
print(type(species))
print(sorted(species))
print(len(species))

my_list = ['a', 'bb', 'ccc']
list_copy = my_list
print(my_list)
list_copy.append('new element')
print(my_list)

my_list2 = ['a', 'bb', 'ccc']
list_copy2 = my_list2.copy()
print(my_list2)
list_copy2.append('new element2')
print(my_list2)

count = 1
while count < 100:
	print("count:" , count)
	count+=1
print('done')


factorial = 1
count = 1
while count <= 2:
	count = count + 1
	factorial = factorial * count
print(factorial)
print(len(str(factorial)))


loop2 = [101,2,15,22,95,33,2,27,72,15,52]
for num in loop2:  
  if num%2 == 0:
    print(num, end=' ')
print('')

x = 0
y = 0
loop = [101,2,15,22,95,33,2,27,72,15,52]
for num in loop:
  if num % 2  == 0:
    x = x + num
  else:
    y = y + num
print(y)
print(x)


print(list(range(0, 100)))

for num in range(0, 101):
  print(num)


num2 = []
for x in range(0,101):
  if 'a' in num2:
    num2.append(a)
print(num2)

#question 10???

#11:
data = ['ATGCCCGGCCCGGC' , 'GCGTGCTAGCAATACGATAAACCGG' , 'ATATATATCGAT' , 'ATGGGCCC']
data_length = len(data)
print(data)
#print (dataint)
#for gene in data:
#  print (len.data)
#  print(gene)




