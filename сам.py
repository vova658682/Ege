#ans = []
#for N in range(1,10000):
#    R = f'{N:b}'
#    if N % 3 == 0:
#        R =  R + R[-3:]
#    else:
#        R = R + f'{N % 3 * 3:b}'
#    R = int(R,2)
#    if R > 76:
#        ans.append(N)
#print(min(ans))
#ans = []
#for N in range(1, 10000):
#    R = f'{N:b}'
#    if N % 2 == 0:
#        R = R +'10'
#    else:
#        R = '1' + R + '01'
#    R = int(R,2)
#    if R > 516:
#        ans.append(N)
#print(min(ans))
ans = []
for N in range(1,10000):
    R = f'{N:b}'
    if sum(map(int,R)) % 2 == 0:
        R = R + '0'
        R = '10' + R[2:]
    else:
        R = '1'+ R
        R = '11' + R[2:]
    R = int(R,2)
    if R >= 16:
        ans.append(N)
print(min(ans))



