from Cliente import Cliente

cliente1 = Cliente("Jose", "Herrera", 1000570051, 580051, 5000)
print(cliente1.consultarSaldo())
print(cliente1.ingresar(2000))
print(cliente1.consultarSaldo())
print(cliente1.retirar(500))
print(cliente1.consultarSaldo())