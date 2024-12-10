# a list is a ordered collection of items /stores multiple values in a single variable 
items = ['toyotta','honda','nissans','randrover','mazda']
# accessing the items 
print(items)
# list items are accessd by index and they start from 0
print(items[1])
# print numbers 1 to 3
print(items[1:4])
# prints items 2 and above
print(items[2:]) 
# print 2 and below
print(items[:3])
# list are mutable can be updated

items.append("canter")
print(items)

items.insert(1,"volkwargon")
print(items)

items.remove("mazda")
print(items)



