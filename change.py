def change():
    """Lee un gasto y el dinero recibido, calcula el vuelto
    y lo separa en pesos (parte entera) y centavos.
    """
    pass
    gasto=float(input("Ingresar Gasto:"))
    dinero_recibido=int(input("Ingresar dinero recibido"))
    vuelto=dinero_recibido-gasto
    entero=int(vuelto)
    centavos=(vuelto-entero)*100
    print("Ingresar gasto:")
    print(gasto)
    print("Dinero recibido")
    print(dinero_recibido)
    print("\nVuelto\n")
    print("Pesos:")
    print(entero)
    print("Centavos:")
    print((round(centavos)))

#change()