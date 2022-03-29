dict=[('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
a={}
for i in dict:
    for j in i:
        if i==j:
            j=j+1
            a.append(j)
            
print(a)            



