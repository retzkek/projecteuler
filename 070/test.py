maxn = 100
ns = set()
for i in xrange(1,maxn+1):
    for j in xrange(i,maxn*maxn/i):
        print i,j
        ns.add(i*j)
for i in xrange(maxn*maxn):
    if i not in ns:
        print i
