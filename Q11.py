my_dict = {'a':50,'b':58,'c':56,'d':40,'e':100,'f':20}
max1=0
max2=0
max3=0
for i in my_dict:
    if my_dict[i]<max1:
        max1=my_dict[i]
        for j in my_dict:
            if my_dict[j]<max2 and my_dict[j]>max1:
                max2=my_dict[j]
                for k in my_dict:
                    if my_dict[k]<max2 and my_dict[k]>max3:
                        max3=my_dict[k]
print(max1,max2,max3)                          
