t = 0
nt = 2
n0 = 10
r = 4
c = 0
while c < 10:
    t += 0.5
    nt = n0*(r**t)
    c +=1
    print(f'{t} --- {nt}')
