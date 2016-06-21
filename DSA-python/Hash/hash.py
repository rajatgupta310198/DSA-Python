import os

os.system("clear")

class hashNode:
    def __init__(self,data,key):
        self.data = data;
        self.key = key
        self.next = None


class HashTable:
    def __init__(self):
        self.max_table_size = 20
        self.hashtable = []*self.max_table_size
        for i in range(0,self.max_table_size):
            self.hashtable.append(None)

    def hsFunction(self,key):
        return key%self.max_table_size;

    def insert(self,data,key):
         hskey = self.hsFunction(key)
         t = hashNode(data,key)
         p = self.hashtable[hskey]
         if p is None:
             p = t;
             self.hashtable[hskey] = p;


    def querry(self,key):
        hashKey = self.hsFunction(key)
        if(self.hashtable[hashKey] is None):
            print("No data ")

        else:
            t = self.hashtable[hashKey]
            while t:
                print(t.key,':',t.data)
                t=t.next;


if __name__ == '__main__':
    my = HashTable()
    my.insert(1,2)
    my.querry(2)
