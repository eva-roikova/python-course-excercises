import numpy as np

a = np.zeros(10)
a[4] = 1
print("a")
print(a)

b = np.arange(10,50)
print("b")
print(b)

c = b[::-1]
print("c")
print(c)

d = np.arange(9).reshape((3,3))
print("d")
print(d)

e = np.array([1,2,0,0,4,0])
e_nonzero = np.nonzero(e)
print("e")
print(e_nonzero)

f = np.array(np.random.rand(30))
f_mean = np.mean(f)
print("f")
print(f_mean)

g = np.ones((3,3))
g[1,1] = 0
print("g")
print(g)

h = np.ones((8,8))
h[1::2, ::2] = 0
h[::2, 1::2] = 0
print("h")
print(h)

i = np.array([1,0])

j = np.arange(11)
ja = (j>2) & (j<9)
j[ja] *= -1
print("j")
print(j)

k = np.random.random(10)
k = np.sort(k)
print("k")
print(k)

l1 = np.random.randint(0,2,5)
l2 = np.random.randint(0,2,5)
equal = l1 == l2
print("l")
print(l1)
print(l2)
print(equal)

m = np.arange(10, dtype=np.int32)
#print(m)
m[:] *= m[:]
print("m")
print(m)

n1 = np.arange(9).reshape(3,3)
n2 = n1 + 1
n3 = np.dot(n1,n2)
n_diag = np.diag(n3)
print("n")
print(n3)
print(n_diag)

