dict={1:["nikki"],2:["rani"],3:["aayu"],4:["himmi"]}
a=[]
b={}
for i in dict:
    for j in dict[i]:
        b[i]=j
a.append(b)
print(a) 