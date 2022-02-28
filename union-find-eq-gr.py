import argparse
from sys import stdin
import pygame as pg

width,height = 1200,800
screen = pg.display.set_mode((width,height))
clock = pg.time.Clock()



    


class UF:
    def __init__(self,n,m):
        self.n=n
        self.m = m
        self.cost=0
        self.ol_cost = []
        self.ol_tot=[]
        self.it=0
        self.total=0
        self.count = n
        self.id = list(range(n))
        self.sz = [1 for i in range(n)]

    def find(self,p):
        while p != self.id[p]:
            self.cost += 1
            p = self.id[p]
        return p

    def union(self,p,q):
        pRoot= self.find(p)
        qRoot = self.find(q)

        if qRoot != pRoot:
            if self.sz[pRoot] < self.sz[qRoot]:
                self.id[pRoot] = qRoot
                self.sz[qRoot] += self.sz[pRoot]
            else:
                self.id[qRoot] = pRoot
                self.sz[pRoot] += self.sz[qRoot]
            self.count-=1

    def is_connected(self,p,q):
        if self.find(p) == self.find(q):
            return True
        return False


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='SMTH')
    parser.add_argument('--verbose','-v',action='count',default=0)
    
    args = parser.parse_args()
    if args.verbose == 1:
        show = True
    else:
        show = False



    n = int(input())
    m = int(input())
    uf = UF(n,m)
    a = 0
    def step(uf):
        uf.it +=1
        line = input()
        p,q = map(int,line.split())
        if uf.is_connected(p,q):
            #print(p,q)
            pass
            
        else:
            uf.union(p,q)
        if show:
            print(p,q,uf.id)
        else:
            print(p,q)
        uf.total+=uf.cost
        uf.ol_cost.append(uf.cost)
        uf.ol_tot.append(uf.total/uf.it)
        uf.cost=0
    while True:
        a+=1
        try:
            step(uf)
        except:
            pass
        o = 0
        if max(uf.ol_cost)!=0:
            h = height/max(uf.ol_cost)
        else:
            h=1
        #print(max(uf.ol_cost),height,uf.ol_cost)
        
        for cost in uf.ol_cost:
            o+=width/uf.m
            pg.draw.polygon(screen,(255,0,0),((o,height-cost*h),(o,height-cost*h+2),(o+2,height-h*cost+2),(o+2,height-h*cost)))
        o=0
        
        
        
        for tot_cost in uf.ol_tot:
            o+=width/uf.m
            pg.draw.polygon(screen,(0,255,0),((o,height-tot_cost*h),(o,height-tot_cost*h+2),(o+2,height-tot_cost*h+2),
                                              (o+2,height-tot_cost*h)))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
        
        
        
        clock.tick(30)
        pg.display.flip()
        screen.fill((0,0,0))

    print(uf.count,uf.cost,uf.total)
