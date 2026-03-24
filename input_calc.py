def rectangle():
    """Lee base y altura de un rectángulo, calcula e imprime
    el área y el perímetro.
    """
    base = int(input())
    print(f"Base: {base}")

    altura = int(input())
    print(f"Altura: {altura}")
    
    area=int((base*altura))
    perimetro=base*2+altura*2
    print(f"Area: {area}\nPerimetro: {perimetro}")
