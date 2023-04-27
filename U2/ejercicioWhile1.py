flag = True
#while True:
while flag == True:
    i = 1
    suma = 0
    while ( i <6):
        print(i)
        num = int(input("Ingrese un número: "))
        if num > 0:
            suma = suma + num
            i = i + 1
        else:
            print("El número debe ser mayor a cero!")
    print("La suma de los numeros es: ",suma)
    print("deseas ingresar nuevamente? (s/n)")
    resp = input()
    if resp == "n":
        #break
        flag = False
