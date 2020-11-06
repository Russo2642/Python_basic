thisset = {"apple", "banana", "cherry"}
print(thisset)

# You cannot access items in a set by referring to an index or a key
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)


# add()	Adds an element to the set
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

# clear()	Removes all the elements from the set
thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)


# discard()	Remove the specified item
thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)
# If the item to remove does not exist, discard() will NOT raise an error.



# pop()	Removes an element from the set
thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)
# Sets are unordered, so when using the pop() method, you will not know which item that gets removed.



# remove()	Removes the specified element
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)
# If the item to remove does not exist, remove() will raise an error.



# union()	Return a set containing the union of sets
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)


# update()	Update the set with the union of this set and others    
thisset = {"apple", "banana", "cherry"}

thisset.update(["orange", "mango", "grapes"])

print(thisset)

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)


# The del keyword will delete the set completely:

thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset)