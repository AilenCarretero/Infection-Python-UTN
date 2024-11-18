import random

# Declaramos la clase Detector la cual se encargará de detectar mutaciones en el ADN.
class Detector:
    # Declaración del método init y los atributos.
    def __init__(self, ADN, nombre, eficiencia):
        self.ADN = ADN
        self.nombre = nombre
        self.eficiencia = eficiencia

    # Declaramos el método para comprobar si hay mutantes en al ADN creado.
    def detectar_mutantes(self, ADN):
        return (self.detectar_horizontal(ADN) or 
                self.detectar_vertical(ADN) or 
                self.detectar_diagonal(ADN))

    # Método para buscar en orientación horizontal.
    def detectar_horizontal(self, ADN):
        return any(self._tiene_secuencia_repetida(fila) for fila in ADN)

    # Método para buscar en orientación vertical.
    def detectar_vertical(self, ADN):
        for columna in range(len(ADN[0])):
            secuencia = ''.join(fila[columna] for fila in ADN)
            if self._tiene_secuencia_repetida(secuencia):
                return True
        return False

    # Método para buscar en orientación diagonal.
    def detectar_diagonal(self, ADN):
        n = len(ADN)
        
        # Diagonal principal.
        for i in range(n - 3):
            diag1 = ''.join(ADN[i + j][j] for j in range(n - i))
            diag2 = ''.join(ADN[j][i + j] for j in range(n - i))
            if self._tiene_secuencia_repetida(diag1) or self._tiene_secuencia_repetida(diag2):
                return True

        # Diagonal secundaria.
        for i in range(3, n):
            diag1 = ''.join(ADN[i - j][j] for j in range(i + 1))
            diag2 = ''.join(ADN[n - 1 - j][i - j] for j in range(i + 1))
            if self._tiene_secuencia_repetida(diag1) or self._tiene_secuencia_repetida(diag2):
                return True

        return False

    # Método para comprobar si se repite la secuencia.
    def _tiene_secuencia_repetida(self, secuencia):
        return any(secuencia[i] == secuencia[i + 1] == secuencia[i + 2] == secuencia[i + 3]
                   for i in range(len(secuencia) - 3))

# Declaramos la clase Mutador la cual se encargará de generar mutaciones en el ADN.
class Mutador:
    
    # Declaración del método init y los atributos.
    def __init__(self, base_nitrogenada, agresividad, origen, ADN):
        self.base_nitrogenada = base_nitrogenada
        self.agresividad = agresividad
        self.origen = origen
        self.ADN = ADN

    # Declaramos el método para la creación de los mutantes.
    def crear_mutante(self):
        pass

# Declaramos la subclase Radiación de la clase Detector la cuál se encargará de generar mutaciones verticales y horizontales en el ADN.
class Radiacion(Mutador):
    
    # Declaración del método init y los atributos.    
    def __init__(self, base_nitrogenada, agresividad, origen, ADN):
        super().__init__(base_nitrogenada, agresividad, origen, ADN)
        
    # Generamos el método para crear mutantes verticales y horizontales.
    def crear_mutante(self, posicion, orientacion):
        fila, columna = posicion
        
        try:
            if orientacion == "H":
                self.ADN[fila] = (self.ADN[fila][:columna] +
                                  self.base_nitrogenada * 4 +
                                  self.ADN[fila][columna + 4:])
            elif orientacion == "V":
                for i in range(4):
                    self.ADN[fila + i] = (self.ADN[fila + i][:columna] +
                                          self.base_nitrogenada +
                                          self.ADN[fila + i][columna + 1:])
            else:
                raise ValueError("Orientación inválida")
        except IndexError:
            print("Posición fuera de los límites")
        return self.ADN

# Declaramos la subclase Virus de la clase Detector la cuál se encargará de generar mutaciones diagonales en el ADN.
class Virus(Mutador):
    
    # Declaración del método init y los atributos.    
    def __init__(self, base_nitrogenada, agresividad, origen, ADN):
        super().__init__(base_nitrogenada, agresividad, origen, ADN)
        
    # Generamos el método para crear mutantes diagonales.
    def crear_mutante(self, posicion):
        fila, columna = posicion
        
        try:
            for i in range(4):
                self.ADN[fila + i] = (self.ADN[fila + i][:columna + i] +
                                      self.base_nitrogenada +
                                      self.ADN[fila + i][columna + i + 1:])
        except IndexError:
            print("Posición fuera de los límites")
        return self.ADN

# Declaramos la clase Sanador la cual se encargará de eliminar mutaciones en el ADN.
class Sanador:
    
    # Declaración del método init y los atributos.   
    def __init__(self, ADN, nombre, eficiencia):
        self.ADN = ADN
        self.nombre = nombre
        self.eficiencia = eficiencia

    # Declaramos el métoso para eliminar mutantes.
    def sanar_mutantes(self, detector):
        if detector.detectar_mutantes(self.ADN):
            print("Se encontraron mutaciones. Generando nuevo ADN...")
            return self.generar_adn_nuevo()
        return self.ADN
    
    # Declaramos un método para generar un ADN.
    def generar_adn_nuevo(self, tamanio=6):
        ADN_nuevo = ["".join(random.choice("ATGC") for _ in range(tamanio)) for _ in range(tamanio)]
        return ADN_nuevo
