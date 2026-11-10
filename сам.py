#ans = []
#for N in range(1,10000):
#    R = f'{N:b}'
#    if N % 8 == 0:
#        R = R + R[-2:]
#    else:
#        R = R + f'{N % 8 * 2:b}'
#    R = int(R ,2)
#    if R >= 3000:
#        ans.append(N)
#print(min(ans))
from string import printable as alph
def convert2(num, sys):
    res = ''
    while num:
        res += alph[num % sys]
        num //= sys
    return res[::-1] if res else '0'
ans = []
for N in range(1,10000):
    R = convert2(N,3)
    if N % 2 == 0:
        R = R + R[-2:]
    else:
        R = R + convert2(sum(map(int,R)), 3)
    R = int(R,3)
    if N > 9:
        ans.append([R,N])
print(min(ans))






