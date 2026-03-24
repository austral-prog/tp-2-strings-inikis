def names():
    """Lee nombre y apellido, e imprime el nombre completo en distintos formatos:
    minúsculas, título, mayúsculas y con tabulador.
    """
    nombre=input("nombre: ")
    apellido=input("apellido: ")
    
    nombre_completo=nombre+" "+apellido
    
    print(f"{nombre_completo.lower()}\n{nombre_completo.title()}\n{nombre_completo.upper()}\n\t{nombre_completo.lower()}")
