import numpy as np
import time
import random


def timingpythonvsnumpy():
    n = 1000000
    a = [random.random() for i in range(n)]
    b = [random.random() for i in range(n)]

    s = time.time()
    c = [a[i]*b[i] for i in range(n)]
    print("Comprehension:", time.time()-s)

    s = time.time()
    c = []
    for i in range(n):
        c.append(a[i]*b[i])
    print("for loop:", time.time()-s)

    s = time.time()
    c = [0]*n
    for i in range(n):
        c[i] = a[i]*b[i]
    print("Existing List", time.time()-s)

    x = np.array(a)
    y = np.array(b)
    s = time.time()
    c = x * y
    print("Numpy Time:", time.time()-s)