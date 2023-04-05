class Usuario:
    def __init__(self, name, email, balance_cuenta):
        self.name = name
        self.email = email
        self.balance_cuenta = balance_cuenta
        
    def hacer_depósito(self, amount):
        self.balance_cuenta += amount
        return self

    def hacer_giro(self, amount):
        self.balance_cuenta -= amount
        return self


guido = Usuario("Guido", "Correo@correo.cl", 0)
dilan = Usuario("dilan", "Correo@correo.cl", 100)

guido.hacer_depósito(150)
dilan.hacer_depósito(150)

print("El usuario", guido.name, "Tiene en su cuenta", guido.balance_cuenta)

guido.hacer_giro(150)

print("El usuario", guido.name, "Disminuyo su saldo a", guido.balance_cuenta)
print("El usuario", dilan.name, "tiene en su cuenta", dilan.balance_cuenta)