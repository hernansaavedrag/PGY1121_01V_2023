resp ="s"
num2 =0
while resp != "n":
    numInvertido = 0
    try:
        num = int(input("Ingrese un número: "))
        num2 = num
        #palabra = input("Ingrese palabra").lower()
        #print(palabra)
        '''res = num/10
        resEntero = num//10
        res3 = 125 //10
        print(res)
        print(resEntero)
        print(res3) NO APROXIMA'''
        if num >= 103 and num <= 987:
        #if  103 <= num <= 987: 
            while num != 0 :
                numInvertido = 10*numInvertido + num%10
                num = num //10  # resultado es la parte entera

        else:
            print("el número debe ser mayor a 103 y menor a 987")
    except:
        print("Debe ingresar un número")
        #raise ValueError("Error de letras")
    finally:
        print("Si o si sale esto!!! ")
    print("El numero invertido de",num2," es: ", numInvertido)
    resp = input("desea ingresar otro número (s/n?").lower() # pasar todo a minuscula
print("FIN")