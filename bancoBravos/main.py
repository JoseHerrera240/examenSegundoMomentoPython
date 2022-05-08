from Cliente import Cliente

cliente = Cliente()
opcion = 1
while(opcion != 0):
    print("Digitar 1 para ingresar un cliente")
    print("Digitar 2 Para consultar el saldo ")
    print("Digitar 3 para ingresar dinero")
    print("Digitar 4 para retirar")
    print("Digitar 0 para Terminar")
    opcion=int(input("Digita una opcion: "))
    if(opcion==0):
        break
    elif(opcion==1):
        cliente.ingresarCliente()
    elif(opcion==2):
        cliente.consultarSaldo()
    elif(opcion==3):
        cliente.ingresar()
    elif(opcion==4):
        cliente.retirar()
    else:
        print("Lo Sentimos, presentamos un error. por favor vuelve a intentarlo.")
