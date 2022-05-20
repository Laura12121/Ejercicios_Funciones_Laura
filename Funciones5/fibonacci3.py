def fibonacci(longitud):
    fibo=[1,1]
    for i in range(2,longitud):
        valor=fibo[i-2] +fibo[i-1]
        fibo.append(valor)
    return fibo 
a=[]
if len(a)==0:
    a= fibonacci(50)
else:
    print('la lista no vacia')
print(a)
