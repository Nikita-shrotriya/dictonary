dict={1: ['Jean Castro'], 2: ['Lula Powell'], 3: ['Brian Howell'], 4: ['Lynne Foster'], 5: ['Zachary Simon']}
a=[]
b={}
for i in dict:
    for j in dict[i]:
        b[i]=j
a.append(b)
print(a)