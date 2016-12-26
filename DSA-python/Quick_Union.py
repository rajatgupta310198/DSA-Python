"""
Dynamic Connectivity lazy approach
"""

class QuickUnion:
    """docstring forQuickUnion."""
    def __init__(self,N):
        self.id = [0]*N
        self.connectedCount = 0;
        for i in range(0,N):
            self.id[i] = i

    def Root(self,p):
        while(p!=self.id[p]):
            p = self.id[p]

        return p

    def find(self,p,q):
        if self.Root(p) == self.Root(q):
            return True
        else:
            return False

    def QUion(self,p,q):
        self.connectedCount +=1
        self.id[self.Root(p)] = self.Root(q)
        return True

    def list(self):
        for i in self.id:
            print(i, ' ')

    def count(self):
        return self.connectedCount



def main():
    qu = QuickUnion(5)
    qu.list()
    print(qu.QUion(1,2))
    print(qu.find(1,2))
    print(qu.find(3,1))
    print(qu.QUion(1,3))
    print(qu.count())
    print(qu.Root(1))


if __name__ == '__main__':
    main()
 
