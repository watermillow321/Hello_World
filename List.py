mylist = [ "Will","Millow","Willow","Nilow","Will","Mark"] # this is how you create a list

print(mylist) # this is how you print a list

print(mylist[2]) # this is how you print the 2nd string in a list

print(mylist[1:4]) # to print a range of a string

print(mylist[:4]) # to print until the 4th string

mylist[2:3] = ["Dark","Carl"]  # to change a element in a array or list
print(mylist[:4])

mylist[0:2] = ["WINTERMILLOW","WINTERMILLOW","WINTERMILLOW"] # to change a element in a array or a list
print(mylist[:4])

mylist.insert(2,"Millowmelon") # to insert a element in a list
print(mylist)

mylist.append("Karl") # to add a element at the end of the list or array
print(mylist)

Extend_example = ["Names", "Names","Names"]
mylist.extend(Extend_example) # to add or extend elements in a list or a array
print(mylist)

mylist.remove("WINTERMILLOW") # to remove an item within a list or array
print(mylist)

mylist.pop(2) # removes a specific a element in a list or array using its index
del mylist[3] # also removes a element in a list using array
print(mylist)

mylist.clear() # clears all elements in a list
print(mylist)
