def create_dictionary(first_name, last_name, age, height, weight, birth_place, birthday, blood_type, curp, rfc):     
    user_info = {         
        "firstname": first_name,         
        "lastname": last_name,         
        "age": age,         
        "height": height,         
        "weight": weight,         
        "birth_place": birth_place,         
        "birthday": birthday,         
        "blood_type": blood_type,         
        "curp": curp,  # Asegúrate de pasar el valor como string
        "rfc": rfc     
    }     
    return user_info  

print("Ejecutando script...")  # Verificar que el script corre  

# Ejemplo de uso con tus datos corregidos
diccionario_Leonardo = create_dictionary(
    "Leonardo", "Lores", 20, 1.74, 94, "Ciudad Victoria", 
    "2 de noviembre", "O+", "RELL041102HTSSRNA8", "NO_CUENTO_CON_UNO_DE_MOMENTO"
)

print(diccionario_Leonardo)  # Verificar salida