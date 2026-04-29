# PROBLEMA 3: KNAPSACK 0/1 - INVERSION EN STARTUPS

def knapsack_01(costos, valores, presupuesto):
    n = len(costos)
    
    # Inicializar tabla DP con ceros
    dp = [[0] * (presupuesto + 1) for _ in range(n + 1)]
    
    # Llenar la tabla
    for i in range(1, n + 1):
        for c in range(1, presupuesto + 1):
            if costos[i-1] <= c:
                dp[i][c] = max(dp[i-1][c], 
                              dp[i-1][c - costos[i-1]] + valores[i-1])
            else:
                dp[i][c] = dp[i-1][c]
    
    # Backtracking para reconstruir los proyectos seleccionados
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
    n = len(proyectos)
    
    print("\n--- TABLA DP (valores en millones) ---")
    
    # Encabezado de columnas (presupuesto c)
    print("     ", end="")
    for c in range(presupuesto + 1):
        print(f"{c:4d}", end="")
    print()
    
    # Linea separadora
    print("     ", end="")
    for _ in range(presupuesto + 1):
        print("----", end="")
    print()
    
    # Filas de la tabla
    for i in range(n + 1):
        if i == 0:
            print("0    ", end="")
        else:
            # Abreviar nombres de proyectos para que quepan
            abrev = proyectos[i-1][:3] if len(proyectos[i-1]) > 3 else proyectos[i-1]
            print(f"{abrev}  ", end="")
        
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
    print("PROBLEMA 3: KNAPSACK 0/1 - INVERSION EN STARTUPS")
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
        print(f"  - {proyectos[idx]}: inversion ${costos[idx]}M -> ROI ${rois[idx]}M")
        costo_total += costos[idx]
    
    print(f"\nInversion total: ${costo_total} millones")
    print(f"Presupuesto no utilizado: ${presupuesto - costo_total} millones")
    
    # Mostrar backtracking
    print(f"\n--- BACKTRACKING REALIZADO ---")
    print("Se recorrio la tabla desde dp[4][10] hasta dp[0][0]")
    print("comparando cada celda con la superior para determinar")
    print("si el proyecto fue tomado o no.")
