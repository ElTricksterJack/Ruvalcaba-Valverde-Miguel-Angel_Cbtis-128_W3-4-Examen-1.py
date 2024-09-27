print(" ")
print("Nombre: Ruvalcaba Valverde Miguel Angel")
print("-------Sacar area y perimetro de un triangulo--------")
print("1.Area --- 2.Perimetro")
A1 = int(input("Elije: "))#primero permitamos la entrada de este valor para desidir cual quieres
match A1:#con el match el switch de c++ pero de python y permite haser multiples simples de manera rapida
#(Decho es de mis comandos favoritos, decho tengo una lista con match que le allado cosas casi todos los dias)
    case 1:#primera opcion
        print("--Area--")
        N1 = int(input("altura 1 o b: "))#capturar o definir valores
        N2 = int(input("base 2 o a: "))
        print("Area:",N2,"X",N1)#esta es la formula para comparar
        print(N2*N1)#se muestra el resultado en pantalla  
    case 2:
        print("--Perimetro--")
        N1 = int(input("base 1 o b: "))#capturar o definir valores
        N2 = int(input("base 2 o a: "))
        print("Perimetro:","2(",N1,"+",N2,")")#esta es la formula para comparar
        print(N1+N2)#se muestra el resultado en pantalla     
    case _:
        print("X_X-ERROR-ERROR-ERROR-X_X")#mensaje de error
