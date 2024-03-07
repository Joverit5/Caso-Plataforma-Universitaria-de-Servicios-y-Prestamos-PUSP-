
class User(object):
    def __init__(self, name, code, email, password, money=0):
        self.name = name
        self.code = code
        self.email = email
        self.password = password
        self.money = money

    def admin_money(self):
        self.money

    def get_n(self):
        return self.name

    def get_c(self):
        return self.code

    def get_e(self):
        return self.email

    def get_p(self):
        return self.password

    def get_m(self):
        return self.money
    
    def money_admin(self, amount):
        """
        Gestiona la cantidad de dinero del usuario.
        Si cantidad es positiva, se añade al dinero actual del usuario.
        Si cantidad es negativa, se resta del dinero actual del usuario si hay suficiente.
        """
        if amount >= 0:
            self.money += amount
            print("Se han añadido ", amount,
                  "  pesos. Nuevo saldo: ", self.money)
        else:
            if self.money >= abs(amount):
                self.money -= abs(amount)
                print(
                    "Se han restado ",amount, " pesos. Nuevo saldo: ", self.money)
            else:
                print("No tienes suficiente dinero para realizar esta operación.")
