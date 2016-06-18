# binary sarch tree in python

import os

os.system("clear")

class Node:
    def __init__(self,data):
        self.data = data
        self.lc = None
        self.rc = None


def insert(node,data):
    if node is None:
        node = Node(data)
        return node

    else:
        if data <node.data:
            node.lc = insert(node.lc,data)

        if data > node.data:
            node.rc = insert(node.rc,data)

        return node

def inOrder(node):
    if node:
        inOrder(node.lc)
        print(node.data)
        inOrder(node.rc)

def search(node,key):
    while node:
        if key < node.data:
            node = node.lc

        if key > node.data:
            node = node.rc

        if key == node.data:
            print("Found")
            return
            break;


    print("Not found")






if __name__ == '__main__':
    mytree = Node(5)
    mytree = insert(mytree,3)
    mytree = insert(mytree,1)
    mytree = insert(mytree,2)
    mytree = insert(mytree,4)
    mytree = insert(mytree,7)
    mytree = insert(mytree,6)
    mytree = insert(mytree,8)
    inOrder(mytree)
    search(mytree,6)
    search(mytree,10)
