from re import M
a=['S001', 'S002', 'S003', 'S004']
b=['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saimchards']
c=[85, 98, 89, 92]
d=[]
for i in a:
    e={}
    for j in b:
        f={}
        for k in c:
            f[j]=k
            e[i]=f
            d.append(e)
            c.remove(k)
            break
        b.remove(j)
        break
print(d)             

    