from supplier import Supplier, supplier_info, cancel_rental_studyroom, rental_studyroom, check_available, buy_food, show_history, byke_rental, byke_available, delete_byke_rental, show_available_devices, buying_history, device_rental, new_rental_device, new_rental_book, show_catalogue, buy_book, rental_book, show_rental
from admin import generate_equipment_report, check_student_status, add_device_inventory, generate_bike_report, generate_food_report, generate_study_room_report
from user import User
from verify import UserManager
print("Nombre del estudiante: José Fernando González Ortiz")
print("Código: T00068395")

management = UserManager()


def menu():

    while True:
        print("Bienvenido a la Plataforma Universitaria de Servicios y Préstamos (PUSP)")
        print("1. Registrarse")
        print("2. Iniciar sesión como usuario")
        print("3. Iniciar sesión como administrador")
        print("4. Iniciar sesión como proveedor")
        print("5. Salir")

        choice = input("Seleccione una opción: ")
        if choice == "1":
            # Registrar un nuevo usuario
            print("\nBienvenido al menú de registro.\n")
            print("\nPor favor, ingrese los siguientes datos:\n")
            name = input("Nombre: ")
            code = input("Código de estudiante: ")
            email = input("Correo institucional: ")
            password = input("Contraseña: ")
            user = User(name, code, email, password)
            print(management.register(user))
            print("El usuario ", user.name, " de código ",
                  user.code, " ha sido registrado en el sistema")
        elif choice == "2":
            # Iniciar sesión como usuario
            print("\nInicio de sesión como usuario")
            email = input("Correo institucional: ")
            password = input("Contraseña: ")
            user = management.login(email, password)
            if user:
                while True:
                    menu_user(user)

        elif choice == "3":
            # Iniciar sesión como administrador
            print("\nInicio de sesión como administrador")
            email = input("Correo institucional: ")
            password = input("Contraseña: ")
            if email == "administrador@admin.edu.co" and password == "Admin123456":
                menu_admin()
        elif choice == "4":
            # Iniciar sesión como proveedor
            print("\nInicio de sesión como administrador")
            email = input("Correo institucional: ")
            password = input("Contraseña: ")
            if email == "proveedor@proveedor.edu.co" and password == "Proveedor123456":
                menu_supplier()
        elif choice == "5":
            print("¡Hasta luego!")
            exit()
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")
            menu()


def menu_user(user):
    virtual_library = Supplier("Libreria Virtual", 0)
    print("\nMenú de usuario")
    print("\n¡Bienvenido, ", user.name, "!\n")
    print("1. Librería Virtual")
    print("2. S.A.T.O (Sistema de Alquiler Tecnológico Online)")
    print("3. Transporte YA (Sistema de reserva de bicicletas) ")
    print("4. Alimento On-Line (Sección de compra de alimentos)")
    print("5. ESTUDIEMOS (Reservar sala de estudio)")
    print("6. Gestionar dinero digital")
    print("7. Volver al menú principal")

    option = input("Selecciona una opción:")

    if option == "1":

        print("\n--- LIBRERÍA VIRTUAL ---\n\n")
        print("1.Catálogo de libros")
        print("2.Renovar prestamo")
        print("3.Mis prestamos")
        print("4.Mi historial de compras")
        print("5.Salir al menú de usuario")
        option_2 = input("Escoge una opción: ")
        if option_2 == "1":
            show_catalogue()
            book_id = int(
                input("Selecciona un libro para ver más opciones (Ingrese el número de ID): "))
            print("1. Comprar libro")
            print("2. Alquilar libro")
            print("3. Volver al catálogo")
            book_option = int(input("Selecciona una opción: "))

            if book_option == 1:
                buy_book(virtual_library, user, book_id)
            elif book_option == 2:
                rental_book(user, book_id)
            elif book_option == 3:
                pass
            else:
                print("\nOpción inválida")
        elif option_2 == "2":
            new_rental_book()
        elif option_2 == "3":
            show_rental()
        elif option_2 == "4":
            buying_history()
        elif option_2 == "5":
            menu_user(user)

        else:
            print("\nOpción inválida")
    elif option == "2":
        print("\n--- S.A.T.O (Sistema de Alquiler Tecnológico Online) ---\n")
        print("1. Ver equipos disponibles")
        print("2. Alquilar equipo")
        print("3. Renovar alquiler")
        print("4. Volver al menú de usuario")
        option_sato = input("Selecciona una opción: ")

        if option_sato == "1":
            show_available_devices()
        elif option_sato == "2":
            device_id = int(
                input("Selecciona el id de alguno de los artículos: "))
            device_rental(user, device_id)
        elif option_sato == "3":
            device_id = int(
                input("Selecciona el id de alguno de los artículos: "))
            new_rental_device(user, device_id)
            pass
        elif option_sato == "4":
            menu_user(user)
        else:
            print("\nOpción inválida")
    elif option == "3":
        print("\n--- Transporte YA (Sistema de reserva de bicicletas) ---\n")
        print("1. Reservar bicicleta")
        print("2. Cancelar reserva de bicicleta")
        print("3. Volver al menú de usuario")
        option_byke = input("Selecciona una opción: ")

        if option_byke == "1":
            date = input("Ingrese la fecha de la reserva (YYYY-MM-DD): ")
            byke_rental(user.name, date)
        elif option_byke == "2":
            cancel_date = input(
                "Ingrese la fecha de la reserva a cancelar (YYYY-MM-DD): ")
            delete_byke_rental(cancel_date)
        elif option_byke == "3":
            menu_user(user)
        else:
            print("\nOpción inválida")
        pass
    elif option == "4":
        print("\n--- Alimento On-Line (Sección de compra de alimentos) ---\n")
        print("1. Comprar alimento")
        print("2. Consultar historial de compras de alimentos")
        print("3. Volver al menú de usuario")
        option_food = input("Selecciona una opción: ")

        if option_food == "1":
            item = input("Ingrese el nombre del alimento: ")
            precio = float(input("Ingrese el precio del alimento: "))
            buy_food(user, item, precio)
        elif option_food == "2":
            show_history(user.name)
        elif option_food == "3":
            menu_user(user)
        else:
            print("\nOpción inválida")
    elif option == "5":
        print("\n--- ESTUDIEMOS (Reservar sala de estudio) ---\n")
        print("1. Reservar sala de estudio")
        print("2. Cancelar reserva de sala de estudio")
        print("3. Volver al menú de usuario")
        option_rooms = input("Selecciona una opción: ")

        if option_rooms == "1":
            room = input("Ingrese el nombre y número de la sala a reservar: ")
            date = input("Ingrese la fecha de la reserva (YYYY-MM-DD): ")
            rental_studyroom(room, date)
        elif option_rooms == "2":
            cancel_room = input(
                "Ingrese el nombre y número de la sala a cancelar: ")
            date_cancel = input(
                "Ingrese la fecha de la reserva a cancelar (YYYY-MM-DD): ")
            cancel_rental_studyroom(cancel_room, date_cancel)
        elif option_rooms == "3":
            menu_user(user)
        else:
            print("\nOpción inválida")

    elif option == "6":
        print("--- GESTIÓN DE DINERO DIGITAL ---")
        print("1. Ver dinero disponible")
        print("2. Modificar cantidad de dinero")
        option_3 = int(input("Escoga una opción: "))
        if option_3 == 1:
            user.get_m()
            menu_user(user)
        elif option_3 == 2:
            amount = int(input("Ingrese la cantidad de dinero a depositar: "))
            user.money_admin(amount)
    elif option == "7":
        menu()
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
        menu_user(user)


def menu_admin():
    print("\nMenú de administrador")
    print("\n¡Bienvenido, Administrador!\n")
    print("1. Sistema 'REPORTES' ")
    print("2. Gestionar alquileres")
    print("3. Administrar información de usuario")
    print("4. Volver al menú principal")

    choice = input("Seleccione una opción: ")

    if choice == "1":
        print("\nOpciones de Reportes:")
        print("1. Reporte de uso de equipos tecnológicos")
        print("2. Reporte de uso de bicicletas")
        print("3. Reporte de compras de alimentos")
        print("4. Reporte de uso de salas de estudio")
        report_choice = input("Seleccione el tipo de reporte: ")

        if report_choice == "1":
            generate_equipment_report()
        elif report_choice == "2":
            generate_bike_report()
        elif report_choice == "3":
            generate_food_report()
        elif report_choice == "4":
            generate_study_room_report()
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")
            menu_admin()
    elif choice == "2":
        print("1. Verificar estado de estudiante")
        print("2. Agregar dispositivo al inventario")
        print("3. Volver al menú de administrador")
        choice_2 = int(input("Escoge una opción: "))
        if choice_2 == 1:
            check_student_status()
        elif choice_2 == 2:
            device_id = input("Ingrese el id del dispositivo nuevo: ")
            device_type = input("Ingrese el tipo de dispositivo: ")
            brand = input("Ingrese la marca del dispositivo: ")
            model = input("Ingrese el modelo del dispositivo: ")
            specs = input("Ingrese las especificaciones del dispositivo: ")
            condition = input("Ingrese las condiciones del dispositivo: ")
            add_device_inventory(device_id, device_type,
                                 brand, model, specs, condition)
    elif choice == "3":
        user_code = input("Ingresa la id del usuario: ")
        management.manage_user_info(user_code)
    elif choice == "4":
        menu()
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
        menu_admin()


def menu_supplier():
    print("\nMenú de proveedor")
    print("\n¡Bienvenido al sistema de proveedores!\n")
    print("1. Información Librería Virtual")
    print("2. Información S.A.T.O ")
    print("3. Información Transporte YA")
    print("4. Información Alimento On-Line")
    print("5. Información ESTUDIEMOS")
    print("6. Volver al menú principal")

    choice = input("Seleccione una opción: ")

    if choice in ["1", "2", "3", "4", "5"]:
        supplier_info(choice)
    elif choice == "6":
        menu()
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
        menu_supplier()


if __name__ == "__main__":
    menu()
