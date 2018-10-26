'''
#example throwing a KeyError
myDict = {'key1':'value1'}
x1 = myDict['key1']
x2 = myDict['key2'] 
'''
'''
#example trapping a KeyError
myDict = {'key1':'value1'}
try:
    x1 = myDict['key1']
    x2 = myDict['key2'] 
except KeyError as e:
    # Ex. check the name of the key that was missing which is 'key2'
    print ("missing key in mydict:", e)
'''
#Programming 'override' examples to avoid KeyError


default = 'Sweetie'
dog_owners = {'Tommie': 'Furry', 'Susie': 'Fluffy'}
a = dog_owners.get('Freddie Mac', default)  #set default value
print(a)

dogs = []
 
for owner in ('Tommie', 'Susie', 'Tim'):
    dogs.append(dog_owners.get(owner, default)) #use default to set key if not existing

print(dogs)
print(dog_owners)

