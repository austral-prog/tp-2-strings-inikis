def check_vowels():
    """Lee un nombre y verifica si contiene cada una de las vocales (a, e, i, o, u),
    sin distinguir mayúsculas de minúsculas.
    """
    nombre=input()
    print(f"Contiene a: {"a" in nombre or "A" in nombre}")
    print(f"Contiene e: {"e" in nombre}")
    print(f"Contiene i: {"i" in nombre or "I" in nombre}")
    print(f"Contiene o: {"o" in nombre}")
    print(f"Contiene u: {"u" in nombre}")