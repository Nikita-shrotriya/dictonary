dict1 =  {'Alex': ['subj1', 'subj2', 'subj3'],'David': ['subj1','subj2']}
a=[]
count=0
for i in dict1:
    a.append (dict1[i])
    for j in a:
        count=count+len(a)
print(count)