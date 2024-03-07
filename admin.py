from datetime import datetime
from supplier import available_devices, user_rental, byke_rental, buying_food_history, rental_study


class Admin(object):
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def get_e(self):
        return self.email

    def get_p(self):
        return self.password


def calculate_rental_duration(device_id):
    """
    Calcula la duración del alquiler para un dispositivo específico.
    """
    if device_id in user_rental:
        rental_date = user_rental[device_id]['rental_date']
        current_date = datetime.now().date()
        rental_duration = (
            current_date - datetime.strptime(rental_date, "%Y-%m-%d").date()).days
        return rental_duration
    else:
        return 0


def calculate_average_rental_duration(equipment_type):
    """
    Calcula la duración promedio de los alquileres para un tipo de equipo específico.
    """
    total_duration = sum([calculate_rental_duration(device['id'])
                         for device in available_devices if device['type'] == equipment_type])
    total_rentals = sum(
        [1 for device in available_devices if device['type'] == equipment_type])
    if total_rentals > 0:
        return total_duration / total_rentals
    else:
        return 0


def generate_equipment_report():
    """
    Genera un informe sobre el uso de equipos tecnológicos.
    """
    total_rentals = len(user_rental)  # Total de alquileres realizados
    # Tipos de equipos disponibles
    equipment_types = set([device['type'] for device in available_devices])

    print("Informe de Uso de Equipos Tecnológicos")
    print("======================================")
    print(f"Total de alquileres realizados: {total_rentals}")

    for equipment_type in equipment_types:
        rentals_of_type = sum(
            [1 for device in available_devices if device['type'] == equipment_type])
        average_duration = calculate_average_rental_duration(equipment_type)
        print(f"\nTipo de Equipo: {equipment_type}")
        print(f"Número de alquileres: {rentals_of_type}")
        print(f"Duración promedio del alquiler: {average_duration} días")


def generate_bike_report():
    """
    Genera un informe sobre el uso de bicicletas.
    """
    total_reservations = len(byke_rental)
    print("Informe de Uso de Bicicletas")
    print("============================")
    print(f"Total de reservas de bicicletas: {total_reservations}")


def generate_food_report():
    """
    Genera un informe sobre las compras de alimentos.
    """
    total_purchases = len(buying_food_history)
    total_spent = sum([purchase['precio'] for purchase in buying_food_history])
    print("Informe de Compras de Alimentos")
    print("===============================")
    print(f"Total de compras de alimentos: {total_purchases}")
    print(f"Gasto total en alimentos: ${total_spent}")


def generate_study_room_report():
    """
    Genera un informe sobre el uso de las salas de estudio.
    """
    total_reservations = sum([len(dates) for dates in rental_study.values()])
    print("Informe de Uso de Salas de Estudio")
    print("==================================")
    print(f"Total de reservas de salas de estudio: {total_reservations}")


# Diccionario para almacenar la información de los dispositivos disponibles
available_devices = {}


def add_device_inventory(device_id, device_type, brand, model, specs, condition):
    """
    Agrega un dispositivo al inventario.
    """
    available_devices[device_id] = {
        'type': device_type,
        'brand': brand,
        'model': model,
        'specs': specs,
        'condition': condition,
        'availability': True  # Se establece como disponible por defecto
    }


def check_student_status(student_id):
    """
    Verifica el estado de un estudiante en términos de morosidad o devolución tardía.
    """
    for device_id, rental_info in user_rental.items():
        if rental_info['student_id'] == student_id:
            rental_duration = calculate_rental_duration(device_id)
            if rental_duration > 7:
                print(
                    f"El estudiante {student_id} tiene una devolución tardía para el dispositivo con ID {device_id}.")
            else:
                print(
                    f"El estudiante {student_id} está al día con el dispositivo con ID {device_id}.")
            return
    print(
        f"No se encontraron registros de alquiler para el estudiante {student_id}.")
