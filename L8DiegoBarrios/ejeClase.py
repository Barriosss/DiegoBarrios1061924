for i in range(2, 11):
    print("Tabla del",i, ":")
    for x in range(1,11):
        print(i,"x",x,"=", i*x)       
    print()


print("ejercicio 2")
n = int(input("Ingrese un número: "))
n1 = int(input("Ingrese otro número: "))

totalprimos = 0

for i in range(n, n1 + 1):
    if i > 1:
        es_primo = True
        for x in range(2, i):
            if i % x == 0:
                es_primo = False
                break
        if es_primo:
            totalprimos += 1
            print(i, "es un número primo")

print("Entre", n, "y", n1, "hay", totalprimos, "números primos")