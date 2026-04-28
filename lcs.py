# PROBLEMA 4: LCS - CONTROL DE VERSIONES

def lcs_completo(v1, v2):
    """
    Calcula la subsecuencia comun mas larga entre dos cadenas.
    
    Parametros:
    - v1: primera cadena
    - v2: segunda cadena
    
    Retorna:
    - longitud: tamaño de la LCS
    - subsecuencia: la subsecuencia encontrada
    - dp: tabla completa para visualizacion
    """
    m, n = len(v1), len(v2)
    
    # Inicializar tabla DP
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Llenar tabla
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if v1[i-1] == v2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    # Backtracking para reconstruir la LCS
    i, j = m, n
    caracteres_lcs = []
    
    while i > 0 and j > 0:
        if v1[i-1] == v2[j-1]:
            caracteres_lcs.append(v1[i-1])
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1
    
    subsecuencia = ''.join(reversed(caracteres_lcs))
    return dp[m][n], subsecuencia, dp


def imprimir_tabla_lcs(dp, v1, v2):
    """Imprime la tabla DP de LCS de forma legible"""
    # Imprimir encabezado con los caracteres de v2
    print("     ", end="")
    for ch in v2:
        print(f"  {ch}", end="")
    print()
    
    # Imprimir linea separadora
    print("     ", end="")
    for _ in range(len(v2)):
        print("---", end="")
    print()
    
    # Imprimir filas
    for i in range(len(v1) + 1):
        if i == 0:
            print("   ", end="")
        else:
            print(f"{v1[i-1]}  ", end="")
        
        for j in range(len(v2) + 1):
            print(f"{dp[i][j]:3d}", end=" ")
        print()


if __name__ == "__main__":
    # Datos del problema
    v1 = "DEPLOY-PROD-DB-01"
    v2 = "DEVELOP-DEBUG-01"
    
    print("="*50)
    print("PROBLEMA: LCS - CONTROL DE VERSIONES")
    print("="*50)
    
    print(f"\nVersion 1 (v1): {v1}")
    print(f"Version 2 (v2): {v2}")
    print(f"Longitud de v1: {len(v1)} caracteres")
    print(f"Longitud de v2: {len(v2)} caracteres")
    
    # Ejecutar algoritmo
    longitud, subsecuencia, tabla = lcs_completo(v1, v2)
    
    # Mostrar tabla DP
    print("\n--- TABLA DP COMPLETA ---")
    imprimir_tabla_lcs(tabla, v1, v2)
    
    # Mostrar resultados
    print(f"\n--- RESULTADOS ---")
    print(f"Longitud de la LCS: {longitud}")
    print(f"Subsecuencia comun mas larga: '{subsecuencia}'")
    
    print("\n--- INTERPRETACION EN CONTROL DE VERSIONES ---")
    print("La LCS representa las partes que permanecen iguales entre versiones.")
    print("Sistemas como Git utilizan LCS para calcular diferencias (diff)")
    print("y fusionar cambios automaticamente (merge).")