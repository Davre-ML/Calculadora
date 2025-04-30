def pedir_y_sumar_numeros():
    """
    Pide al usuario que ingrese números separados por comas
    y devuelve la suma de esos números.
    """
    entrada = input("Ingresa los números a sumar, separados por comas: ")
    print("Ejemplo de como deberían ingresar los números")
    print("después de cada coma debe ir separado por un espacio")
    print("10, -5, 5.5, -0.5, 10")
    try:
        numeros = [float(n.strip()) for n in entrada.split(",")]
        resultado = sum(numeros)
        print(f"La suma de los números es: {resultado}")
    except ValueError:
        print("Error: Asegúrate de ingresar solo números separados por comas.")

# Ejecutar la función
pedir_y_sumar_numeros()
