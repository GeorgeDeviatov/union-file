import argparse
from sys import stdin


def find(p,idd):
    return idd[p]

def union(p,q,idd):
    pID = find(p,idd)
    qID = find(q,idd)

    if qID != pID:
        for i in range(len(idd)):
            if idd[i] == pID:
                idd[i] = qID
    return idd

def is_connected(p,q,idd):
    if idd[p] == idd[q]:
        return True
    return False


if __name__ == "__main__":
    try:
        parser = argparse.ArgumentParser(description='SMTH')
        parser.add_argument('view',type=str,help='Show how is a programm working?')
    
        args = parser.parse_args()
        if args.view == 'y':
            show = True
        else:
            show = False
    except:
        show = False

    n = int(input())
    idd = list(range(n))
    count = n
    
    for line in stdin:
        p,q = map(int,line.split())
        if is_connected(p,q,idd):
            print(p,q)
            continue
        else:
            count-=1
            union(p,q,idd)
        if show:
            print(p,q,idd)
        else:
            print(p,q)


    print(count)
