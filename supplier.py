from datetime import datetime, timedelta


class Supplier:
    def __init__(self, name, money):
        self.name = name
        self.money = money


# LIBRERIA VIRTUAL
# Lista de libros en el catálogo
book_catalogue = [
    {"id": 1, "title": "El principito", "autor": "Antoine de Saint-Exupéry",
        "buy_price": 15, "rental_price": 5, "available": True},
    {"id": 2, "title": "Cien años de soledad", "autor": "Gabriel García Márquez",
        "buy_price": 20, "rental_price": 8, "available": True},
    {"id": 3, "title": "Don Quijote de la Mancha", "autor": "Miguel de Cervantes",
        "buy_price": 18, "rental_price": 6, "available": True},
    {"id": 4, "title": "1984", "autor": "George Orwell",
        "buy_price": 16, "rental_price": 5, "available": True},
    {"id": 5, "title": "Orgullo y prejuicio", "autor": "Jane Austen",
        "buy_price": 14, "rental_price": 4, "available": True},
    {"id": 6, "title": "Matar a un ruiseñor", "autor": "Harper Lee",
        "buy_price": 22, "rental_price": 7, "available": True},
    {"id": 7, "title": "Crimen y castigo", "autor": "Fyodor Dostoevsky",
        "buy_price": 21, "rental_price": 8, "available": True},
    {"id": 8, "title": "Rayuela", "autor": "Julio Cortázar",
        "buy_price": 17, "rental_price": 6, "available": True},
    {"id": 9, "title": "Moby Dick", "autor": "Herman Melville",
        "buy_price": 19, "rental_price": 7, "available": True},
    {"id": 10, "title": "El gran Gatsby", "autor": "F. Scott Fitzgerald",
        "buy_price": 23, "rental_price": 9, "available": True},
    {"id": 11, "title": "La Odisea", "autor": "Homero",
        "buy_price": 20, "rental_price": 7, "available": True},
    {"id": 12, "title": "Cien años de soledad", "autor": "Gabriel García Márquez",
        "buy_price": 20, "rental_price": 8, "available": True},
    {"id": 13, "title": "Mujercitas", "autor": "Louisa May Alcott",
        "buy_price": 18, "rental_price": 6, "available": True},
    {"id": 14, "title": "Los hermanos Karamazov", "autor": "Fyodor Dostoevsky",
        "buy_price": 24, "rental_price": 9, "available": True},
    {"id": 15, "title": "Drácula", "autor": "Bram Stoker",
        "buy_price": 16, "rental_price": 5, "available": True},
    {"id": 16, "title": "El retrato de Dorian Gray", "autor": "Oscar Wilde",
        "buy_price": 22, "rental_price": 7, "available": True},
    {"id": 17, "title": "Anna Karenina", "autor": "Lev Tolstói",
        "buy_price": 21, "rental_price": 8, "available": True},
    {"id": 18, "title": "Ulises", "autor": "James Joyce",
        "buy_price": 23, "rental_price": 9, "available": True},
    {"id": 19, "title": "Las uvas de la ira", "autor": "John Steinbeck",
        "buy_price": 19, "rental_price": 7, "available": True},
    {"id": 20, "title": "Matar un ruiseñor", "autor": "Harper Lee",
        "buy_price": 22, "rental_price": 7, "available": True},
]
purchase_history = []
user_rental = {}


def buying_history(user):
    print(f"\n--- Historial de compras de {user} ---\n")
    for purchase in purchase_history:
        if purchase["user"] == user:
            print(
                f"Item: {purchase['title']} - Total: ${purchase['buy_price']}")
    if not any(purchase["user"] == user for purchase in purchase_history):
        print("No hay compras registradas para este usuario en el historial.")


def show_catalogue():
    print("\n--- Catálogo de libros ---\n")
    for book in book_catalogue:
        print(book['id'], ".", book['title'], "-", book['autor'])
    print()


def buy_book(supplier, user, book_id):
    for book in book_catalogue:
        if book['id'] == book_id:
            if user.money >= book['buy_price']:
                user.money -= book['buy_price']
                supplier.money += book['buy_price']
                purchase_history.append(
                    {"usuario": user.name, "libro": book['title'], "precio": book['buy_price']})
                print("Compra realizada con éxito")
                return
            else:
                print("No tienes suficiente dinero para comprar este libro.")
                return
    print("libro no encontrado en el catálogo.")


def new_rental_book(user, book_id):
    for book in book_catalogue:
        if book['id'] == book_id:
            if book['id'] in user_rental:
                new_available_date = input(
                    "Ingrese la nueva fecha de disponibilidad (YYYY-MM-DD): ")
                user_rental[book['id']]['rental_date'] = new_available_date
                print(
                    "libro:", book['title'], "actualizado con éxito. Puede ser recogido a partir de ", new_available_date)
                return
    print("libro no encontrado en el catálogo.")


def rental_book(user, book_id):
    for book in book_catalogue:
        if book['id'] == book_id:
            if book['available']:
                available_date = input(
                    "Ingrese la fecha de disponibilidad (YYYY-MM-DD): ")
                book['available'] = False
                user_rental[book['id']] = {
                    "title": book['title'], "rental_date": available_date}
                print(
                    "libro:", book['title'], "alquilado con éxito. Puede ser recogido a partir de ", available_date)
                return
            else:
                print("El libro no está disponible para alquilar.")
                return
    print("libro no encontrado en el catálogo.")


def show_rental():
    if user_rental:
        print("\n--- Mis préstamos ---\n")
        for book_id, info_book in user_rental.items():
            print("Título: ", info_book['title'])
            print("Fecha de alquiler: ", info_book['rental_date'])
            print()
    else:
        print("No tienes préstamos activos en este momento.")


# SATO
available_devices = [
    {"id": 1, "name": "Computadora portátil",
        "type": "portátil", "available": True},
    {"id": 2, "name": "Tablet", "type": "tablet", "available": True},
    {"id": 3, "name": "Impresora", "type": "impresora", "available": True},
    # Agrega más equipos aquí según sea necesario
]


def show_available_devices():
    print("\n--- Equipos Disponibles para Alquilar ---\n")
    for device in available_devices:
        print(device['id'], ". ", device['nombre'])
    print()


def device_rental(user, device_id):
    for device in available_devices:
        if device['id'] == device_id:
            if device['disponible']:
                rental_date = input(
                    "Ingrese la fecha de alquiler (YYYY-MM-DD): ")
                user_rental[device['id']] = {
                    "name": device['name'], "rental_date": rental_date}
                print(
                    "Equipo ", device['name'], "alquilado con éxito. Estará disponible a partir de", rental_date)
                return
            else:
                print(
                    "El equipo seleccionado no está disponible para alquilar en este momento.")
                return
    print("Equipo no encontrado.")


def new_rental_device(user, device_id):
    for device in available_devices:
        if device['id'] == device_id:
            if device['id'] in user_rental:
                new_available_date = input(
                    "Ingrese la nueva fecha de disponibilidad (YYYY-MM-DD): ")
                user_rental[device['id']]['rental_date'] = new_available_date
                print(
                    "Equipo:", device['title'], "actualizado con éxito. Puede ser recogido a partir de ", new_available_date)
                return


# TRANSPORTE YA
byke_rental = {}


def byke_available(date):
    """
    Verifica la disponibilidad de bicicletas para la fecha especificada.
    """
    if date not in byke_rental:
        return True
    else:
        return False


def byke_rental(user, date):
    """
    Reserva una bicicleta para el usuario en la fecha especificada.
    """
    if byke_available(date):
        byke_rental[date] = user
        print(f"Bicicleta reservada con éxito para {date}.")
    else:
        print("Lo siento, todas las bicicletas están reservadas para esta fecha.")


def delete_byke_rental(date):
    """
    Cancela la reserva de bicicleta para la fecha especificada.
    """
    if date in byke_rental:
        del byke_rental[date]
        print(f"Reserva de bicicleta para {date} cancelada correctamente.")
    else:
        print("No hay reserva de bicicleta para esta fecha.")


# Alimento On-Line
buying_food_history = []


def buy_food(user, item, price):
    """
    Realiza una compra de alimento para el usuario.
    """
    if user.money >= price:
        user.money -= price
        buying_food_history.append(
            {"usuario": user.name, "item": item, "precio": price})
        print(
            f"Compra de {item} realizada con éxito. Saldo restante: ${user.money}")
    else:
        print("Saldo insuficiente para realizar la compra.")


def show_history(user):
    """
    Consulta el historial de compras de alimentos del usuario.
    """
    print(f"\n--- Historial de compras de alimentos de {user} ---\n")
    for purchase in buying_food_history:
        if purchase["user"] == user:
            print(f"Item: {purchase['item']} - Precio: ${purchase['precio']}")
    if not any(purchase["user"] == user for purchase in buying_food_history):
        print("No hay compras de alimentos registradas para este usuario en el historial.")


# ESTUDIEMOS
rental_study = {}


def check_available(room, date):
    """
    Verifica la disponibilidad de una sala de estudio para la fecha especificada.
    """
    if room not in rental_study:
        return True
    elif date not in rental_study[room]:
        return True
    else:
        return False


def rental_studyroom(room, date):
    """
    Reserva una sala de estudio para la fecha especificada.
    """
    if check_available(room, date):
        if room not in rental_study:
            rental_study[room] = [date]
        else:
            rental_study[room].append(date)
        print(f"Sala {room} reservada con éxito para {date}.")
    else:
        print("Lo siento, la sala de estudio ya está reservada para esta fecha.")


def cancel_rental_studyroom(room, date):
    """
    Cancela la reserva de una sala de estudio para la fecha especificada.
    """
    if room in rental_study and date in rental_study[room]:
        rental_study[room].remove(date)
        print(
            f"Reserva de la sala {room} para {date} cancelada correctamente.")
    else:
        print("No hay reserva de esta sala de estudio para esta fecha.")

#info
sales_data = {
    "LIBRERIA VIRTUAL": {"ventas": 5000, "productos_disponibles": 100},
    "S.A.T.O": {"ventas": 8000, "productos_disponibles": 150},
    "Transporte YA": {"ventas": 3000, "productos_disponibles": 80},
    "Alimento On-Line": {"ventas": 6000, "productos_disponibles": 120},
    "ESTUDIEMOS": {"ventas": 4000, "productos_disponibles": 90}
}

def supplier_info(choice):
    """
    Mostrar información del proveedor seleccionado.
    """
    supplier_name = None
    if choice == "1":
        supplier_name = "LIBRERIA VIRTUAL"
    elif choice == "2":
        supplier_name = "S.A.T.O"
    elif choice == "3":
        supplier_name = "Transporte YA"
    elif choice == "4":
        supplier_name = "Alimento On-Line"
    elif choice == "5":
        supplier_name = "ESTUDIEMOS"

    if supplier_name:
        info = sales_data[supplier_name]
        print(f"\nInformación del proveedor {supplier_name}:")
        print(f"Dinero obtenido de las ventas: ${info['ventas']}")
        print(f"Productos disponibles sin alquilar: {info['productos_disponibles']}")
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")