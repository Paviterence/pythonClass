thisset = {"apple", "banana", "cherry"}
print(thisset)
print(type(thisset))
print("+=+="*10)
try:
    print(thisset[10])
except TypeError:
    print("'set' object is not subscriptable")
print("+=+="*10)
# A set is a collection which is unordered, unchangeable*, and unindexed
# Note: the set list is unordered, meaning: the items will appear in a random order.
#duplicate values are removed
thisset1 = {"apple", "banana", "cherry", "apple"}
print(thisset1)
print("+=+="*10)
thisset2= set(("apple", "banana", "cherry"))
print(thisset2)
thisset2.add("hello")
print(thisset2)
thisset2.remove("banana")#discard(),clear(),pop(),del
print(thisset2)
thisset2.discard("cherry")
print(thisset2)
print("+=+="*10)
# Once a set is created, you cannot change its items, but you can remove items and add new items.
