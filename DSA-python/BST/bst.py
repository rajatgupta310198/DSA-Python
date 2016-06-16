# binary sarch tree in python

import os

os.system("clear")

class Node:
    def __init__(self,data):
        self.data = data
        self.lc = None
        self.rc = None


class BST:
    def __init__(self,data):
        self.Root = Node(data)

    def insert(self,Root,data):
        if Root is None:
            t = Node(data)
            return t;

        else:
            if data < self.Root.data:
                self.Root.lc = self.insert(self.Root.lc,data)

            if data > self.Root.data:
                self.Root.rc = self.insert(self.Root.rc,data)

            return self.Root


    def inOrder(self,Root):
        if(Root):
            inOrder(self.Root.lc)
            print(self.Root.data)
            inOrder(self.Root.rc)
