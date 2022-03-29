dic=[{"first":"1"},{"second": "2"},{"third": "1"},{"four": "5"},{"five":"5"},{"six":"9"},{"seven":"7"}]
a=[]
for i in dic:
    for j in i.values():
        a.append(j)
print(set(a))        
