from math import log2,ceil
for L in range(1,10000):
    N = 10 + 26 + 8164
    i = ceil(log2(N))
    I = ceil(L * i/8)
    if I * 835 > 156 * 1024:
        print(L)






