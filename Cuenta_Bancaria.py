class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):
    def __init__(self, nombre, apellido, numero_cuenta, saldo=0):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo

    def __str__(self):
        return f"Cliente: {self.nombre} {self.apellido}\nCuenta {self.numero_cuenta}: {self.saldo}€"

    def Ingresar(self, cantidad):
        self.saldo += cantidad

    def Retirar(self, cantidad):

        if self.saldo >= cantidad:
            self.saldo -= cantidad
        else:
            print("Fondos insuficientes")

def Crear_Cliente():
    nombre_cliente = input("Introduzca su nombre: ")
    apellido_cliente = input("Introduzca su apellido: ")
    cuenta_cliente = input("Introduzca su cuenta: ")
    cliente = Cliente(nombre_cliente, apellido_cliente, cuenta_cliente)
    return cliente

def Iniciar():
    cliente = Crear_Cliente()
    opcion = "0"

    while opcion != "3":
        print(cliente)
        opcion = input("[1]-Ingresar dinero\n[2]-Retirar dinero\n[3]-Salir\n")

        match opcion:
            case "1":
                cantidad = int(input("Ingrese la cantidad a depositar: "))
                cliente.Ingresar(cantidad)

            case "2":
                cantidad = int(input("Ingrese la cantidad a retirar: "))
                cliente.Retirar(cantidad)

    print("Muchas gracias, vuelva pronto")

Iniciar()



