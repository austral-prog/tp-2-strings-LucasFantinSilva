def casting():
    """Lee precio, descuento y cantidad como texto y calcula el precio con descuento y el total."""
    pass
    precio= int(input("precio"))
    descuento=float(input("descuento"))
    cant=int(input("cantidad"))
    individual=float(precio-descuento)
    total=float(individual*cant)
    print(f"Precio: {precio}")
    print(f"Descuento: {descuento}")
    print(f"Precio con descuento: {individual}")
    print(f"Total: {total}")




