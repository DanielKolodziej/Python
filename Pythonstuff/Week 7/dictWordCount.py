sentence = input('Enter your Sentence >  ')
counts = {i:0 for i in 'aeiouAEIOU'} #create/intialize dictionary with dict comprehension

for char in sentence:
    if char in counts:
        counts[char] += 1
for k,v in counts.items():  #display dictionary items
    print (k, ":" , v)


print()

import pickle
#set dictionary to values low to high
d=dict(sorted(counts.items(), key=lambda t: t[1]))

#use with statement to open, manipulate, close out file within block!
with open('mydict.pickle', 'wb') as f:
    
    pickle.dump(d, f)

#unpickle dict object from file

with open('mydict.pickle', 'rb') as f:
    dict_contents=pickle.load(f)

#print dict contents to stdout
    
for k,v in dict_contents.items():     #display dictionary items
    print (k, ":" , v)

