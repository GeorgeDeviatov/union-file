import argparse
from sys import stdin

class UF:
	def __init__(self,n):
		self.count = n
		self.id = list(range(n))

	def find(self,p):
		while p != self.id[p]:
			p = self.id[p]
		return p

	def union(self,p,q):
		pRoot = self.find(p)
		qRoot = self.find(q)

		if qRoot != pRoot:
			self.id[pRoot] = qRoot
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
	uf = UF(n)

	for line in stdin:
		p,q = map(int,line.split())
		if uf.is_connected(p,q):
			print(p,q)
			continue
		else:
			uf.union(p,q)
		if show:
			print(p,q,uf.id)
		else:
			print(p,q)


	print(uf.count)
