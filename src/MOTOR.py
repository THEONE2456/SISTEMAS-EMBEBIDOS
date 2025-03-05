welcome_message = """
    BIENVENIDO AL SISTEMA MOTOR CONTROL
    Para comenzar, debes introducir una velocidad deseada y la dirección (L para izquierda, R para derecha):
"""
print(welcome_message)

while True:
    user_input = input("Introduce una velocidad en el rango válido (0 a 255) y la dirección (L o R), o escribe STOP para detener el motor: ").strip()

    if user_input.upper() == "STOP":
        motor_info = {"velocidad": 0, "dirección": "STOP"}
        print(motor_info)
        print("El motor se ha detenido.")
        break

    try:
        parts = user_input.split()
        if len(parts) != 2:
            raise ValueError("Formato incorrecto")

        velocity, direction = parts
        velocity = int(velocity)
        direction = direction.upper()
    except ValueError:
        print("Error: Debes ingresar un valor numérico seguido de L o R (ejemplo: 100 L). Intenta de nuevo.")
        continue

    if direction not in ["L", "R"]:
        print("Error: La dirección debe ser L (izquierda) o R (derecha). Intenta de nuevo.")
        continue

    if 0 <= velocity <= 255:
        motor_info = {"velocidad": velocity, "dirección": direction}
        print(motor_info)
        if direction == "L":
            print(f"Velocidad establecida en {velocity} RPM. El motor gira hacia la izquierda.")
        elif direction == "R":
            print(f"Velocidad establecida en {velocity} RPM. El motor gira hacia la derecha.")
    else:
        print("Error: La velocidad no está en rango (0 a 255). Intenta de nuevo.")