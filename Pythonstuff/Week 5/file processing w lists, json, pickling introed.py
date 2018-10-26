
## Processing Lists to file
#a. Writelines method
#General syntax  -> fileObject.writelines( sequence )

# Open a file
fo = open("foo.txt", "w")
seq = ["This is 1st line\n", "This is 2nd line"]

# Write sequence of lines at the end of the file.
fo.writelines( seq )

# Close opend file
fo.close()

'''

#b. with statement (closes file automatically)
list=["\nThis is 3rd line","This is fourth line"]
with open ("foo.txt","a")as fp:
   for line in list:
       fp.write(line+"\n")

'''
'''
#c. Pickling (serializing objects as 'binary' data - in our case list sequence)
itemlist=["hello","python"]
import pickle

#write data to file (serializing)
outfile = open("foo.dat", "wb")
pickle.dump(itemlist, outfile)
outfile.close()

#read back file (deserializing)
infile = open("foo.dat", "rb")
itemlist = pickle.load(infile)
infile.close()
print(itemlist)

#read from file (binary dump) -> hexdump -C foo.dat

#d  json
#load module command: sudo pip install simplejson --upgrade

import json as simplejson
#write to file
fw = open('foo2.txt', 'w')
simplejson.dump([1,2,3,4], fw)
fw.close()

#read from file
fr = open('foo2.txt', 'r')
data=simplejson.loads(fr.read())
fr.close()
print(data)
'''
