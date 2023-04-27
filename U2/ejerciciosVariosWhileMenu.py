op = 1
while op != 4:
    print("1. Calcular número perfecto")
    print("2. Calcular número primo")
    print("3. tablas de multiplicar")
    print("4. Salir")
    op = int(input("Ingrese su opción: "))

    if op == 1 :
        num = int(input("Ingrese un número: "))
        cont = 0
        if num > 0:
            #for i in range(1,num):
            i = 1
            while i < num:
                if num %i ==0:
                    cont = cont + i
                i = i +1
            if cont == num:
                print("El número es perfecto")
            else:
                print("El número no es perfecto")
        else:
            print("El número debe ser mayor a cero")
    else:
        if op == 2:
            num = int(input("Ingrese un número: "))
            cont = 0
            if num > 0:
                #for i in range(2,num):
                i = 2
                while i < num:
                    if num %i ==0:
                        cont = cont + 1
                    i = i + 1
                if cont > 0:
                    print("El número no es primo")
                else:
                    print("El número es primo")
            else:
                print("El número debe ser mayor a cero")
        else:
            if op == 3:
                #for i in range(1,11):
                #    for j in range(1,11):
                i = 1
                while (i < 11):
                    j = 1
                    while(j < 11):
                        multi = i * j
                        print(i,"x",j,"=",multi)
                        j = j + 1
                    i = i + 1
                    print("\n")

