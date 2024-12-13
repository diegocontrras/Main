def base(num, base_origen, base_destino):
    def parte_entera(entero, base_destino):
        if entero == 0:
            return "0"
        digitos = [] # Almacena los dígitos de la manera entera
        while entero:
            digito = entero % base_destino # Fórmula general para conversión base decimal a base destino
            if digito >= 10:
                digitos.append(chr(ord('A') + digito - 10)) # Hace la conversión de letras para números mayores a 10
            else:
                digitos.append(str(digito)) # Si no, sólo convierte los números en cadena
            entero //= base_destino 
        return ''.join(digitos[::-1]) # Une los dígitos de manera inverso sin incluir espacio
    
    def parte_fraccion(fraccion, base_destino):
        digitos = [] # Almacena los dígitos de la manera fraccion
        while fraccion > 0 and len(digitos) < 10: # Limita la precisión a 10 dígitos
            fraccion *= base_destino
            digito = int(fraccion)
            if digito >= 10:
                digitos.append(chr(ord('A') + digito - 10)) # Hace la conversión de letras para números mayores a 10
            else:
                digitos.append(str(digito))
            fraccion -= digito
        return ''.join(digitos) # Une los dígitos sin incluir espacios ''
        
    if '.' in num: # Si hay punto decimal, se divide en parte entera y parte fraccion
        entero_str, fraccion_str = num.split('.')
    else:
        entero_str, fraccion_str = num, ""  # Aquí se ajusta para manejar números sin punto decimal

    if not es_valido_para_base(entero_str, base_origen):
        raise ValueError(f"'{entero_str}' no es un número válido en base {base_origen}.")

    if base_origen != 10: # Convierte la parte entera de bases distintas a base 10
        entero = int(entero_str, base_origen)
    else:
        entero = int(entero_str)

    # Convierte la parte fraccion a base 10
    fraccion = 0
    if fraccion_str:
        for i, digito in enumerate(fraccion_str):
            if '0' <= digito <= '9':
                valor = int(digito)
            else:
                valor = ord(digito.upper()) - ord('A') + 10 # Si el valor es una letra, busca el valor de la letra en código ASCII
            fraccion += valor * (base_origen ** -(i + 1)) # Formula general para obtener las posiciones

    resultado_entero = parte_entera(entero, base_destino)
    resultado_fraccion = parte_fraccion(fraccion, base_destino)

    if resultado_fraccion: # Unir la parte entera y la fraccion
        return f"{resultado_entero}.{resultado_fraccion}"
    else:
        return resultado_entero
    
def es_valido_para_base(num, base):
    try:
        int(num, base)
        return True
    except ValueError:
        return False

def main():
    while True:
        print("\n@@@@@@@@@@@@@@ TAREA 1 @@@@@@@@@@@@@@@@@@\n")
        print("---------- Conversión de Bases ----------")
        print("1. Convertir un número")
        print("2. Salir")
        opcion = input("\nElige una opción: ")
        
        if opcion == "1":
            num = input("Ingresa el número: ")
            if not num:
                print("Error: Debes ingresar un número válido.")
                continue
            try:
                base_origen = int(input("Ingresa la base de origen del número (ej. 2, 10, 16): "))
                base_destino = int(input("Ingresa la base destino (ej. 2, 10, 16): "))
            except ValueError:
                print("Error: Debes ingresar números válidos para las bases.")
                continue
            
            try:
                resultado = base(num, base_origen, base_destino)
                print(f"Desde base {base_origen} el número '{num}' da como resultado '{resultado}' en base {base_destino}.")
            except ValueError as e:
                print(f"Error: {e}")  # Captura y muestra el error sin romper el programa
            print("-----------------------------------------------------------------------------")
        
        elif opcion == "2":
            print("\n¡Adiós!")
            print("\n-----------------------------------------------------------------------------")
            break
        
        else:
            print("Opción no válida, por favor elige una opción del menú.")

main()
