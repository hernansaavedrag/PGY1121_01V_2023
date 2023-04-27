i = 1
contCeros = 0
suma = 0
while (i < 6):
    print(i)
    try:
        num = int(input("Ingrese número: "))
        if num > 0 :
            contCeros = contCeros + 1

        if num%2 == 0 :
            suma = suma + num

        i = i + 1
    except:
        print("Error, debe ingresar un número")

print("la cantidad de numeros mayores a cero es: ",contCeros)
print("La suma de los números de pares es: ",suma)


