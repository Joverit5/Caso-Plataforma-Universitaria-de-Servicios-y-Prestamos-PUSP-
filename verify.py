class UserManager (object):
    def __init__(self):
        self.registered_users = []

    def verify_email(self, email):
        # Lógica para verificar que el correo institucional sea válido
        if "@estudiantes.edu.co" in email:
            return True
        else:
            print("Error: El correo electrónico no es institucional.")
            return False

    def verify_password(self, password):
        # Lógica para verificar que la contraseña sea válida
        if len(password) >= 8 and any(char.isdigit() for char in password):
            return True
        else:
            print(
                "Error: La contraseña debe tener al menos 8 caracteres y al menos un dígito.")
            return False

    def register(self, user):
        # Verificar que el correo institucional y la contraseña sean válidos
        if self.verify_email(user.email) and self.verify_password(user.password):
            self.registered_users.append(user)
            return "Usuario registrado correctamente"

        else:
            return "Error: Cuenta no pudo ser creada"
        # Fin de registro de usuario

    def login(self, email, password):
        for user in self.registered_users:
            if user.email == email and user.password == password:
                return user
        return None

    def manage_user_info(self, user_code):
        """
        Administrar la información del usuario.
        """
        if user_code in self.registered_users:
            user_info = self.registered_users[user_code]
            print(f"\nInformación del usuario con código {user_code}:")
            print(f"Nombre: {user_info['name']}")
            print(f"Correo electrónico: {user_info['email']}")
        else:
            print("El código de usuario ingresado no existe.")
