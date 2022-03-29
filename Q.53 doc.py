dic=[[1, 'Jean Castro', 'V'], [2, 'Lula Powell', 'V'], [3, 'Brian Howell', 'VI'], [4, 'Lynne Foster', 'VI'], [5, 'Zachary Simon', 'VII']]
a={}
i=0
while i<len(dic):
    j=0
    c=0
    list=[]
    while j<len(dic[i]):
        if j==0:
        	c=dic[i][j]
        else:
        	list.append(dic[i][j])
        j+=1
    a[c]=list
    i+=1
print(a)

