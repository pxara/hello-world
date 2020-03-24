import sys
import pprint
import argparse

def Neighbors(p,u,v):
    for i in p:
        if i==u:
            continue
        up=(i[0] ,i[1]+1 )
        down=(i[0] ,i[1]-1 )
        right=(i[0]+1 ,i[1] )
        left=(i[0]-1 ,i[1] )
        if right==v or up==v or down==v or left==v:
            return True
    else:
         return False

def CountFixedPolyominoes(G,untried,n,p): 
    global c 
    untried=list(untried)
    while len(untried)>0:
        u=untried[0]
        p.append(u)
        untried.remove(u)
        if len(p)==n:
            c=c+1
        else:
            new_neighbors=[]
            for v in G[u]: 
                if (v not in untried) and (v not in p)  and (not Neighbors(p,u,v)):
                    new_neighbors.append(v)
            new_untried=untried+new_neighbors 
            CountFixedPolyominoes(G,new_untried,n,p)
        p.remove(u)

def PolyominoGraph(n): #[y,x] , x>=0
    polyominograph={}
    orio=n-2
    for y in range(0,n):
        polyominograph[(y,0)]=[]
    for x in range(1,n):
        for y in range(-orio,orio+1):
            polyominograph[(y,x)]=[]
        orio+=-1 
    for i in polyominograph:
        up=(i[0] ,i[1]+1 )
        down=(i[0] ,i[1]-1 )
        right=(i[0]+1 ,i[1] )
        left=(i[0]-1 ,i[1] )
        if right in polyominograph:
            polyominograph[i].append(right) 
        if up in polyominograph:
            polyominograph[i].append(up)
        if left in polyominograph:
            polyominograph[i].append(left)
        if down in polyominograph:
            polyominograph[i].append(down)
    return polyominograph 



parser=argparse.ArgumentParser()
parser.add_argument("-p","--printswitch",action="store_true")
parser.add_argument("n",type=int,help="polyomino size")
args=parser.parse_args()

G=PolyominoGraph(args.n)
untried={(0,0)}
p=[]
c=0
if args.printswitch:
    pprint.pprint(G)
CountFixedPolyominoes(G,untried,args.n,p)
print(c)
