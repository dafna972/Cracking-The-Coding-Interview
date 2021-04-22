from MinimalTree import MinimalTree

def ValidateBST(root):
    value = root.value
    leftTree = root.left_child
    rightTree = root.right_child
    if leftTree != None and leftTree.max() >= value:
        return False
    if rightTree != None and rightTree.min() <= value:
        return False
    if (leftTree == None or ValidateBST(leftTree)) and (rightTree == None or ValidateBST(rightTree)):
        return True
    else:
        return False

tree = MinimalTree([1,2,3,4,5,6,7],7)
print(tree)
print(ValidateBST(tree))
tree = MinimalTree([1,3,2,4,5,6,7],7)
print(tree)
print(ValidateBST(tree))