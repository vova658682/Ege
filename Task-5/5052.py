ans = []
for n in range(1,10000):
    R = f'{n:b}'
    if n % 2 == 0:
        R = '11' + '11'
    else:
        R = '1' + R + '00'
    R = int(R,2)
    if R <=113:
        ans.append(R)


print(max(ans))
