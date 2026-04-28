# PROBLEMA 3: KNAPSACK 0/1 - INVERSION EN STARTUPS

def knapsack_01(costos, valores, presupuesto):
    """
    Resuelve el problema de la mochila 0/1 usando programacion dinamica.
    
    Parametros:
    - costos: lista de costos de cada proyecto
    - valores: lista de ROI de cada proyecto
    - presupuesto: capacidad maxima de inversion
    
    Retorna:
    - valor_maximo: ROI maximo alcanzable
    - seleccion: lista de indices de proyectos seleccionados
    - dp: tabla completa para visualizacion
    """
    n = len(costos)
    
    # Inicializar tabla DP
    dp = [[0] * (presupuesto + 1) for _ in range(n + 1)]
    
    # Llenar tabla
    for i in range(1, n + 1):
        for c in range(1, presupuesto + 1):
            if costos[i-1] <= c:
                dp[i][c] = max(dp[i-1][c], 
                              dp[i-1][c - costos[i-1]] + valores[i-1])
            else:
                dp[i][c] = dp[i-1][c]
    
    # Backtracking para reconstruir la solucion
    capacidad_restante = presupuesto
    seleccion = []
    
    for i in range(n, 0, -1):
        if dp[i][capacidad_restante] != dp[i-1][capacidad_restante]:
            seleccion.append(i-1)
            capacidad_restante -= costos[i-1]
    
    seleccion.reverse()
    return dp[n][presupuesto], seleccion, dp


def imprimir_tabla(dp, costos, valores, proyectos, presupuesto):
    """Imprime la tabla DP de forma legible"""
    print("\n--- TABLA DP (valores en millones de pesos) ---")
    
    # Imprimir encabezado
    print("     ", end="")
    for c in range(presupuesto + 1):
        print(f"{c:4d}", end="")
    print()
    print("     ", end="")
    for c in range(presupuesto + 1):
        print("----", end="")
    print()
    
    # Imprimir filas
    for i in range(len(proyectos) + 1):
        if i == 0:
            print("0    ", end="")
        else:
            print(f"{proyectos[i-1][:3]}  ", end="")
        
        for c in range(presupuesto + 1):
            print(f"{dp[i][c]:4d}", end="")
        print()


if __name__ == "__main__":
    # Datos del problema
    proyectos = ["HealthTech", "AI Startup", "GreenTech", "Fintech"]
    costos = [3, 5, 2, 4]   # costo en millones
    rois = [7, 9, 4, 6]     # ROI en millones
    presupuesto = 10         # presupuesto total en millones
    
    print("="*50)
    print("PROBLEMA: KNAPSACK 0/1 - INVERSION EN STARTUPS")
    print("="*50)
    
    print(f"\nPresupuesto disponible: ${presupuesto} millones")
    print("\nProyectos disponibles:")
    for i, (proy, costo, roi) in enumerate(zip(proyectos, costos, rois)):
        print(f"  {i+1}. {proy}: Costo ${costo}M, ROI ${roi}M")
    
    # Ejecutar algoritmo
    max_roi, seleccion, tabla = knapsack_01(costos, rois, presupuesto)
    
    # Mostrar tabla DP
    imprimir_tabla(tabla, costos, rois, proyectos, presupuesto)
    
    # Mostrar resultados
    print(f"\n--- CARTERA DE INVERSION OPTIMA ---")
    print(f"ROI maximo alcanzable: ${max_roi} millones")
    print("Proyectos seleccionados:")
    
    costo_total = 0
    for idx in seleccion:
        print(f"  - {proyectos[idx]}: ${costos[idx]}M inversion -> ROI ${rois[idx]}M")
        costo_total += costos[idx]
    
    print(f"\nCosto total de inversion: ${costo_total} millones")
    print(f"Presupuesto no utilizado: ${presupuesto - costo_total} millones")