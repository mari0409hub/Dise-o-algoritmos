# PROBLEMA 1: CAJERO AUTOMATICO - ALGORITMO GREEDY
# Estudiante: mariana gutierrez 
# Asignatura: Diseño de Algoritmos

def dispensar_billetes(monto, billetes):
    """
    Algoritmo greedy para dispensar billetes.
    
    Parametros:
    - monto: cantidad de dinero a dispensar
    - billetes: lista de denominaciones disponibles
    
    Retorna:
    - resultado: diccionario con billete y cantidad
    - restante: monto no dispensado (debe ser 0 para exito)
    """
    billetes.sort(reverse=True)
    resultado = {}
    restante = monto
    
    print(f"\n=== DISPENSANDO ${monto:,} COP ===")
    print(f"Billetes disponibles: {billetes}\n")
    
    for b in billetes:
        if restante >= b:
            cantidad = restante // b
            resultado[b] = cantidad
            restante -= cantidad * b
            print(f"  Usando {cantidad} billete(s) de ${b:,} -> Restante: ${restante:,}")
        else:
            resultado[b] = 0
    
    return resultado, restante


def mostrar_resultado(resultado, sobrante):
    """Muestra el resultado de forma legible"""
    print("\n--- RESULTADO FINAL ---")
    total_billetes = 0
    for billete, cantidad in resultado.items():
        if cantidad > 0:
            print(f"  ${billete:,}: {cantidad} billete(s)")
            total_billetes += cantidad
    print(f"Total de billetes usados: {total_billetes}")
    
    if sobrante > 0:
        print(f"ERROR: Sobrante no dispensable: ${sobrante:,}")
        print("Sugerencia: El monto debe ser multiplo de la denominacion mas pequena")
    else:
        print("EXITO: Transaccion completada - monto exacto entregado")


if __name__ == "__main__":
    # Datos del problema
    monto = 87500
    billetes = [50000, 20000, 10000, 5000, 1000]
    
    resultado, sobrante = dispensar_billetes(monto, billetes)
    mostrar_resultado(resultado, sobrante)
    
    # Caso adicional: con billete de 7000
    print("\n" + "="*50)
    print("CASO CON BILLETE DE $7,000 AGREGADO")
    print("="*50)
    
    billetes_con_7000 = [50000, 20000, 10000, 7000, 5000, 1000]
    resultado2, sobrante2 = dispensar_billetes(monto, billetes_con_7000)
    mostrar_resultado(resultado2, sobrante2)