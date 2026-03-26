def string_methods():
    """Demuestra el uso de métodos de string: strip, lstrip, rstrip, upper, lower,
    title, find, replace, count, operador in, slicing con paso, reverso,
    f-strings y strings multilínea.
    """
    nombre = "   Grace Hopper   "
    frase = "Python es un gran lenguaje de programacion"
    multilinea = """Linea 1
Linea 2
Linea 3"""
    
    nombre_strip = nombre.strip()
    nombre_lstrip = nombre.lstrip()
    nombre_rstrip = nombre.rstrip()
    frase_may = frase.upper()
    frase_min = frase.lower()
    frase_tit = frase.title()
    pos_gran = frase.find("gran")
    frase_reemplazo = frase.replace("programacion", "desarrollo")
    cant_a = frase.count("a")
    python_en_frase = "Python" in frase
    java_en_frase = "Java" in frase
    frase_slice = frase[:6] #Python
    no_contiguos = frase_slice[::2]
    inverso = frase_slice[::-1]
    combinacion = f"{nombre_strip} sabe {frase_slice}"
    
    print(f"Strip: {nombre_strip}")
    print(f"Lstrip: {nombre_lstrip}")
    print(f"Rstrip: {nombre_rstrip}")
    print(f"Upper: {frase_may}")
    print(f"Lower: {frase_min}")
    print(f"Title: {frase_tit}")
    print(f"Find: {pos_gran}")
    print(f"Replace: {frase_reemplazo}")
    print(f"Count: {cant_a}")
    print(f"Contiene Python: {python_en_frase}")
    print(f"Contiene Java: {java_en_frase}")
    print(f"Slice: {frase_slice}")
    print(f"Paso: {no_contiguos}")
    print(f"Reverso: {inverso}")
    print(f"Formato: {combinacion}")
    print(multilinea)
