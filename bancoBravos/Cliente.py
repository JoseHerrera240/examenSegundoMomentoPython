from http import client


class Cliente:
    def __init__(self):
        self.nombre = None
        self.apellido = None
        self.cedula = None
        self.numeroCuenta = None
        self.saldo = None
    def consultarSaldo(self):
        return print(f"Saldo:  {self.saldo}")
    def ingresar(self):
        extra = int(input("Ingrese el dinero a ingresar: "))
        ingreso = self.saldo + extra
        return print(f"Ingresate:  {extra}")
    def retirar (self):
        menos = int(input("Ingrese el dinero a retirar: "))
        egreso = self.saldo - menos
        return print(f"Retiraste: {menos}")
    def ingresarCliente(self):
      self.nombre = input("Ingrese su nombre: ")
      self.apellido = input("Ingrese su apellido: ")
      self.cedula = int(input("Ingrese la cedula: "))
      self.numeroCuenta = int(input("Ingrese el numero de cuenta: "))
      self.saldo = int(input("Ingrese su saldo: "))  

