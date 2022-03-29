dict={'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]}
a={}
for i,j in dict.items():
    j.clear()
    a[i]=j
print(a)    

