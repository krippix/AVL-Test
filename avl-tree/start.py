import tree

nodes = [9,3,14,11,12,17]
#nodes = [3,2,4]
del_no = 9
test = tree.Tree()

print("\n************* START *************\n")

print(f"Inserting the following nodes: {nodes}")
test.insert(nodes)

print(f"Structure after inserting: ")
print(test.export())
print("")

print(f"Searching for number: {del_no}")
print(f"Found: {test.search(del_no)}\n")

print(f"Deleting number {del_no}")
test.delete(del_no)

print(f"Structure after deleting: ")
print(test.export())
print("")