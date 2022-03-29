from platform import java_ver


dict={'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}
for i,j in dict.items():
    if i>6:
        dict[j]=i
print(dict)       


