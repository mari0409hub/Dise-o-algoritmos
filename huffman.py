# PROBLEMA 2: COMPRESION DE LOGS - ALGORITMO HUFFMAN

import heapq

class NodoHuffman:
    """Nodo del arbol de Huffman"""
    def __init__(self, frecuencia, caracter=None, izquierdo=None, derecho=None):
        self.frecuencia = frecuencia
        self.caracter = caracter
        self.izquierdo = izquierdo
        self.derecho = derecho
    
    def __lt__(self, otro):
        return self.frecuencia < otro.frecuencia


def construir_arbol_huffman(frecuencias):
    """
    realizo el arbol de Huffman a partir de un diccionario de frecuencias.
    
    Parametros:
    - frecuencias: diccionario {simbolo: frecuencia}
    
    Retorna:
    - raiz del arbol de Huffman
    """
    heap = [NodoHuffman(freq, char) for char, freq in frecuencias.items()]
    heapq.heapify(heap)
    
    print("Construccion del arbol de Huffman:")
    paso = 1
    
    while len(heap) > 1:
        izquierdo = heapq.heappop(heap)
        derecho = heapq.heappop(heap)
        nuevo_nodo = NodoHuffman(izquierdo.frecuencia + derecho.frecuencia, 
                                  None, izquierdo, derecho)
        heapq.heappush(heap, nuevo_nodo)
        print(f"  Paso {paso}: Fusion {izquierdo.frecuencia} + {derecho.frecuencia} = {nuevo_nodo.frecuencia}")
        paso += 1
    
    return heap[0]


def generar_codigos(nodo, codigo_actual="", tabla_codigos=None):
    """
    esto Genera los codigos binarios recorriendo el arbol de Huffman.
    
    Parametros:
    - nodo: nodo actual del arbol
    - codigo_actual: codigo acumulado hasta el momento
    - tabla_codigos: diccionario para almacenar los codigos
    
    Retorna:
    - diccionario {simbolo: codigo}
    """
    if tabla_codigos is None:
        tabla_codigos = {}
    
    if nodo.caracter is not None:
        tabla_codigos[nodo.caracter] = codigo_actual
        return tabla_codigos
    
    generar_codigos(nodo.izquierdo, codigo_actual + "0", tabla_codigos)
    generar_codigos(nodo.derecho, codigo_actual + "1", tabla_codigos)
    return tabla_codigos


if __name__ == "__main__":
    # Datos del problema - frecuencias de palabras en el log
    frecuencias = {
        "ERROR": 45,
        "INFO": 120,
        "WARN": 30,
        "DEBUG": 80,
        "TRACE": 15
    }
    
    print("="*50)
    print("PROBLEMA: COMPRESION DE LOGS - HUFFMAN")
    print("="*50)
    
    print("\nFrecuencias originales:")
    for palabra, freq in frecuencias.items():
        print(f"  {palabra}: {freq}")
    
    # Construir arbol y generar codigos
    arbol = construir_arbol_huffman(frecuencias)
    codigos = generar_codigos(arbol)
    
    print("\n--- CODIGOS HUFFMAN ---")
    for palabra, codigo in codigos.items():
        print(f"  {palabra}: {codigo} (longitud: {len(codigo)} bits)")
    
    # Calculo de bits sin compresion
    total_palabras = sum(frecuencias.values())
    bits_sin_compresion = total_palabras * 3  # 2^3 = 8 >= 5 simbolos
    
    # Calculo de bits con compresion
    bits_con_compresion = 0
    for palabra, freq in frecuencias.items():
        bits_con_compresion += freq * len(codigos[palabra])
    
    # Porcentaje de ahorro
    ahorro = (bits_sin_compresion - bits_con_compresion) / bits_sin_compresion * 100
    
    print("\n--- ESTADISTICAS DE COMPRESION ---")
    print(f"Total de palabras: {total_palabras}")
    print(f"Bits sin compresion (codigo fijo de 3 bits): {bits_sin_compresion}")
    print(f"Bits con compresion Huffman: {bits_con_compresion}")
    print(f"Ahorro: {ahorro:.2f}%")