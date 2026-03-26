def casting():
    """Lee precio descuento y cantidad como texto y calcula el precio con descuento y el total"""
    precio=int(input("ingrese un precio: "))
    descuento=float(input("ingrese un descuento (valido con coma): "))
    cant=int(input("ingrese una cantidad: "))
    
    precio_descuento = precio - descuento
    total = precio_descuento * cant
    
    print(f"Precio: {precio}\nDescuento: {descuento}\nPrecio con descuento: {precio_descuento}\nTotal: {total}")