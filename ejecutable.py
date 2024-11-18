from clases import Detector, Radiacion, Virus, Sanador
import random
import time

# Declaramos la función inicial.
def start():
    print("")
    print("🧬🧬 Bienvenido a Infection 🧬🧬")
    print("")
    
    ADN = crear_adn()
    
    print("\n🧬 El ADN ha sido generado exitosamente. 🧬")
    for fila in ADN:
        print(f"                {fila}")
    
    modificar_ADN(ADN)

# Declaramos una función para crear el ADN.
def crear_adn():
    while True:
        opcion_menu = input("¿Desea crear un ADN personalizado? (S/N): ").strip().upper()
        
        # En caso de que el usuario desee ingresar las bases por su cuenta.
        if opcion_menu == "S":
            print("""
    Ingresa las bases nitrogenadas deseadas:
            T — Timina
            A — Adenina
            G — Guanina
            C — Citosina
            """)
            ADN = []
            for i in range(6):
                while True:
                    fila = input(f"Ingrese 6 bases nitrogenadas para la fila {i+1}: ").strip().upper()
                    if len(fila) == 6 and all(letra in "ATGC" for letra in fila):
                        ADN.append(fila)
                        break
                    print("Ingreso inválido. Debe contener exactamente 6 bases (A, T, G, C).")
            return ADN

        # En caso de que el usuario desee ingresar las bases de forma aleatorias.
        elif opcion_menu == "N":
            return ["".join(random.choice("ATGC") for _ in range(6)) for _ in range(6)]

        else:
            print("Opción inválida. Por favor, seleccione 'S' o 'N'.")

# Declaramos la función para modificar el ADN.
def modificar_ADN(ADN):
    while True:
        print("""
¿Qué desea hacer con el ADN?
    1. 🔎 Detectar mutantes.
    2. 🦠 Crear mutaciones.
    3. 🤍 Sanar mutaciones.
    4. 🚪 Salir.
        """)
        
        try:
            opcion = int(input("Seleccione la opción deseada (1-4): ").strip())
            print("")
        except ValueError:
            print("Opción inválida. Por favor, ingrese un número entre 1 y 4.")
            continue

        if opcion == 1:
            detectar_mutantes(ADN)
        elif opcion == 2:
            ADN = crear_mutaciones(ADN)
        elif opcion == 3:
            ADN = sanar_mutantes(ADN)
        elif opcion == 4:
            print("¡Gracias por usar Infection!")
            break
        else:
            print("\nOpción inválida. Por favor, ingrese un número entre 1 y 4.")

# Declaramos una función para detectar mutaciones e invocar la clase Detector.
def detectar_mutantes(ADN):
    nombre_detector = input("Nombre del detector: ").capitalize()
    eficiencia_detector = input("Eficiencia del detector (alta, media, baja, nula): ").lower()
    
    print("")
    
    print("🔎 Buscando posibles mutaciones... 🔎")
    time.sleep(1)
    
    print("")
    
    detector = Detector(ADN, nombre_detector, eficiencia_detector)
    if detector.detectar_mutantes(ADN):
        print(f"✅ El detector {nombre_detector} ha detectado mutaciones.")
    else:
        print(f"❎ No se encontraron mutaciones con el detector {nombre_detector}.")

# Declaramos una función para generar mutaciones e invocar a las subclases Radiacion y Virus.
def crear_mutaciones(ADN):
    while True:
        print("""
¿Qué tipo de mutación desea realizar?
    1. 💀 Radiación
    2. 🦠 Virus
        """)
        try:
            tipo_mutacion = int(input("Ingrese la opción deseada (1 o 2): ").strip())
        except ValueError:
            print("Opción inválida. Ingrese 1 o 2.")
            continue

        base_nitrogenada = input("Ingrese la base nitrogenada para la mutación (T, A, G, C): ").strip().upper()
        if base_nitrogenada not in "ATGC":
            print("Base nitrogenada inválida. Intente nuevamente.")
            continue

        origen = input("Origen del mutador (laboratorio, animal, espacial, etc.): ").lower()
        agresividad = input("Agresividad del mutador (letal, alta, media, baja, nula): ").lower()

        print("")
        
        # Generación de radiacion
        if tipo_mutacion == 1:
            orientacion = input("¿Desea que la radiación se exparza horizontal o verticalmente? (H/V): ").strip().upper()
            while(True):
                try:
                    fila, columna = map(int, input("Ingrese la posición inicial (fila columna): ").split())
                    radiacion = Radiacion(base_nitrogenada, agresividad, origen, ADN)
                    ADN = radiacion.crear_mutante((fila, columna), orientacion)
                    
                    print("")
                    
                    print("\n💀 Introduciendo un poco de radiación... 💀")
                    time.sleep(1)
                    
                    print("\nEl ADN ha sido infectado correctamente. 🧬💀")
                    for fila in ADN:
                        print(f"                {fila}")
                    return ADN
                    break
                except ValueError:
                    print("Posición inválida. Asegúrese de ingresar dos números separados por un espacio.")
                except Exception as e:
                    print(f"Error al aplicar la mutación: {e}")
        
        # Generacion de virus
        elif tipo_mutacion == 2:
            while(True):
                try:
                    fila, columna = map(int, input("Ingrese la posición inicial (fila columna): ").split())
                    virus = Virus(base_nitrogenada, agresividad, origen, ADN)
                    ADN = virus.crear_mutante((fila, columna))
                    
                    print("")
                    
                    print("🦠 Introduciendo algunos virus... 🦠")
                    time.sleep(1)
                    
                    print("")
                    
                    print("\nEl ADN ha sido infectado correctamente. 🧬🦠")
                    for fila in ADN:
                        print(f"                {fila}")
                    return ADN
                    break
                except ValueError:
                    print("Posición inválida. Asegúrese de ingresar dos números separados por un espacio.")
                except Exception as e:
                    print(f"Error al aplicar la mutación: {e}")
        else:
            print("Opción de mutación inválida. Intente nuevamente.")
            
# Declaramos una función para eliminar mutaciones e invocar a la clase Sanador.
def sanar_mutantes(ADN):
    nombre_sanador = input("Nombre del sanador: ").capitalize()
    eficiencia_sanador = input(f"Eficiencia del {nombre_sanador} (alta, media, baja): ").lower()
    
    sanador = Sanador(ADN, nombre_sanador, eficiencia_sanador)
    
    print("")
    
    print("🔎 Buscando posibles mutaciones... 🔎")
    time.sleep(1)
    
    print("")
    
    detector = Detector(ADN, "Temporal", "alta")
    ADN = sanador.sanar_mutantes(detector)
    
    print("🤍 Sanando las mutaciones encontradas... 🤍")
    time.sleep(1)
    
    print("")
    
    print("¡Listo! El ADN ya no tiene mutantes 🤍 ")
    for fila in ADN:
        print(f"                {fila}")
    
    return ADN

# Inicialización del programa.
if __name__ == "__main__":
    start()
