"""
Dynamic Connectivity lazy approach
"""

class QuickUnion:
    """docstring forQuickUnion."""
    def __init__(self,N):
        self.id = [0]*N
        for i in range(0,N):
            self.id[i] = i

    def Root(self,p):
        while(p!=self.id[p]):
            p = self.id[p]

        return p

    def find(self,p,q):
        if Root(p) == Root(q):
            return True
        else:
            return False

    def QUion(self,p,q):
        self.id[Root(p)] = Root(q)




qu = QuickUnion(5)
print(qu.find(2,2))
print(qu.find(1,1))
print(qu.find(1,2))
