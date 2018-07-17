import numpy as np

#generate the number of tanks
N=np.random.randint(50000)

k=np.random.randint(1,N)

#generate the tanks
tanks=np.arange(N)
#randomly order them
np.random.shuffle(tanks)
#get the first k
t=tanks[:k]
kmax=np.max(t)


print 'k = {} , kmax = {}'.format(k, kmax)

print 'kmax + kmax/k -1  = {}'.format(-1+kmax+kmax/k)
print '              N   = {}'.format(N)

