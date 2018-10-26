#dictionary sorting example- sort by a ranking (by key or value)

myDict={'Jack':5,'Bill':14,'Kat':3,'Jess':33,'Alex':4}
myDict2={'Jack':5,'Bill':14,'Kat':3,'Jess':33,'Alex':4}

def sortByKey():    
    sortedByKeyDict=sorted(myDict.items(),key=lambda t: t[0])
    print (sortedByKeyDict)    #note array order is displayed

def sortByValue():    
    sortedByValueDict=sorted(myDict.items(),key=lambda t: t[1])
    print (sortedByValueDict)  #note array order is displayed

sortByKey();

sortByValue();


