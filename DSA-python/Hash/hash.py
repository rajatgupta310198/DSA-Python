import os

os.system("clear")

class hasNode:
    def __init__(self,data,key):
        self.data = data;
        self.key = key
        self.next = None


class HashTable:
    def __init__(self):
        self.htable = []
        self.max_table_size = 20

    def hsFunction(self,key):
        return key%self.max_table_size;

    def insert(self,data,key):
        
