from http import client


class Cliente:
    def __init__(self,nombre,apellido,cedula,numeroCuenta,saldo):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.numeroCuenta = numeroCuenta
        self.saldo = saldo
    def consultarSaldo(self):
        return print(self.saldo)
    def ingresar(self,extra):
        ingreso = self.saldo + extra
        return ingreso
    def retirar (self, menos):
        egreso = self.saldo - menos
        return egreso

cliente1 = Cliente("Jose", "Herrera", 1000570051, 580051, 5000)
print(cliente1.consultarSaldo())
print(cliente1.ingresar(2000))
print(cliente1.consultarSaldo())
print(cliente1.retirar(500))
print(cliente1.consultarSaldo())