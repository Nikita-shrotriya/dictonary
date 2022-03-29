a={'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
dict={}
for i in a:
    j=0
    n=[]
    while j<len(a[i]):
        if a[i][j]%2==0:
            n.append(a[i][j])
            dict[i]=n
        j+=1
print(dict)


