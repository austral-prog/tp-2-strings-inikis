def slice_simple():
    """Dado el texto 'Awesome', imprime distintos substrings
    usando slicing y lower().
    """
    texto = "Awesome"
    
    print(f"{texto[:3].lower()}")
    print(f"{texto[2:5]}")
    print(f"{texto.lower()}")