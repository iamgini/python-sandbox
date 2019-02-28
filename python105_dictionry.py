#import os
#clear screen
#os.system('clear')  # on linux / os x
#print("\n")
mydict = {'Apple':10.05,'Grapes':12.50,'Orange':'No Stock'}
print("Dictionary : ", mydict)
print("One item from Dictionary : ", mydict['Apple'])
ndict = {'veg':123,'k2':[10,20,30],'k3':{'insidekey':[100,200,"hello"]}}
ens192={'intvalues':["name-ens192","10.154.158.146",'20','30']}
print("\nens192 : ", ens192)
print("\nens192 value: ", ens192['intvalues'][0])
print("\nDictionary : ", ndict)
print("\nValue 1 from Dictionary : ", ndict['k2'])
print("\nValue 2 inside from Dictionary : ", ndict['k3']['insidekey'])
print("\nVVVVValue 2 and process it : ", ndict['k3']['insidekey'][2].upper())
ndict['k4'] = "New Key Value"
print("\nDictionary : ", ndict)
print("\nDisplay only keys : ", ndict.keys())
print("\nDisplay only values : ", ndict.values())
ndict["ams"]={'RGS':['x','y','z']}
print("'\n",ndict['ams']['RGS'])
#a=sorted(ndict.items(),key=lambda)
a=sorted(ndict, key=ndict.get)