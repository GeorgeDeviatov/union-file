import argparse
from sys import stdin

class UF:
    def __init__(self,n):
        self.count = n
        self.id = list(range(n))

    def find(self,p):
        return self.id[p]

    def union(self,p,q):
        pID = self.find(p)
        qID = self.find(q)

        if qID != pID:
            for i in range(len(self.id)):
                if self.id[i] == pID:
                    self.id[i] = qID
            self.count-=1

    def is_connected(self,p,q):
        if self.id[p] == self.id[q]:
            return True
        return False


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='SMTH')
    parser.add_argument('view',type=str,help='Show how is a programm working?')
    
    args = parser.parse_args()

    n = int(input())
    uf = UF(n)

    for line in stdin:
        p,q = map(int,line.split())
        if uf.is_connected(p,q):
            continue
        else:
            uf.union(p,q)
        if args.view == 'y':
            print(p,q,uf.id)
        else:
            print(p,q)


    print(uf.count)
