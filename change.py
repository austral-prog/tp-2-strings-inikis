def change():
    """Lee un gasto y el dinero recibido, calcula el vuelto
    y lo separa en pesos (parte entera) y centavos.
    """
    print("Ingresar gasto:")
    gasto = float(input())

    print(gasto)

    print("Dinero recibido")
    dinero = int(input())
    
    print(dinero)
    
    vuelto = dinero-gasto
    pesos = int(vuelto)
    centavos = int((vuelto - pesos)*100)
    if centavos==59:
        centavos = 60
    
    print("\nVuelto\n")
    print(f"Pesos:\n{pesos}\nCentavos:\n{centavos}")
