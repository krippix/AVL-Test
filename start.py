import tree

test = tree.Tree()

test.insert([9,3,14,11,12,17])




print(test.export())

#print(test.search(7))


test.delete(9)
print()
print(test.export())