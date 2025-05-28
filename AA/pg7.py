def min_edge(e,v,vt):
    min=999
    for i in range (len(e)):
        x=e[i][0]
        y=e[i][1]
        w=e[i][2]
        if (x in v and y in vt) or (x in vt and y in v):
            if w< min:
                min=w
                pos=i
    return pos         

def prims(e,v):
    et=[]
    vt=[]
    vert=v.pop(0)
    vt.append(vert)
    n=len(v)
    for i in range (n):
        pos=min_edge(e,v,vt)
        x=e[pos][0]
        y=e[pos][1]
        b=e[pos]
        et.append(b)
        del b
        if x in vt:
            vt.append(y)
            v.remove(y)
        else:
            vt.append(x)
            v.remove(x)
    return et
# Driver code
edge = [['a', 'b', 5], ['b', 'd', 6], ['c', 'd', 4],
        ['a', 'c', 7], ['a', 'e', 2], ['b', 'e', 3],
        ['d', 'e', 5], ['c', 'e', 4]]
vert = ['a', 'b', 'c', 'd', 'e']

mst = prims(edge, vert)
print("Minimum Spanning Tree (MST):", mst)#
