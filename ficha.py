def ficha():
    """Ejercicio integrador. Lee nombre, email y 3 notas, y genera una ficha
    de alumno aplicando: strip, title, lower, upper, int, len, find, slicing,
    reverse, replace, count, in, f-strings, strings multilínea y operaciones matemáticas.
    """
    # Ejercicio integrador: Generador de Ficha de Alumno
    #
    # Leer mediante input:
    #   1. Nombre completo (puede tener espacios extra y mayúsculas mezcladas)
    #   2. Email (puede tener mayúsculas)
    #   3. Tres notas (como texto, hay que convertirlas)
    #
    # Generar una ficha que incluya:
    #   - Encabezado decorativo usando un string multilínea con "="
    #   - Nombre limpio: sin espacios extra y con formato título
    #   - Email en minúsculas
    #   - Cantidad de caracteres del nombre
    #   - Iniciales: usar find para encontrar el espacio e indexar las letras
    #   - Usuario: apellido.nombre en minúsculas
    #   - Verificar si el email contiene @ 
    #   - Extraer el dominio del email
    #   - Nombre con guion bajo en vez de espacio
    #   - Contar las 'a' en el nombre
    #   - Código secreto: nombre invertido en mayúsculas
    #   - Las 3 notas, su suma, promedio y promedio entero
    #   - Cierre decorativo usando repetición de string ("=" * 24)
    
    nombre_completo=input("ingrese su nombre: ")
    email=input("ingrese su email: ")
    nota1=int(input("ingrese nota 1: "))
    nota2=int(input("ingrese nota 2: "))
    nota3=int(input("ingrese nota 3: "))
    
    nombre_limpio=nombre_completo.strip().lower().title()
    email_minusculas=email.lower()
    cant_nombre=len(nombre_limpio)
    espacio_nombre=nombre_limpio.find(" ")
    iniciales=nombre_limpio[0]+nombre_limpio[espacio_nombre+1]
    usuario=(nombre_limpio[espacio_nombre+1:]+"."+nombre_limpio[:espacio_nombre]).lower()
    email_valido="@" in email
    dominio_email=email[email.find("@")+1:].lower()
    nombre_guion=nombre_limpio.replace(" ", "_")
    cant_a=nombre_limpio.count("a")
    codigo=nombre_limpio[::-1].upper()
    suma_notas=nota1+nota2+nota3
    promedio=suma_notas/3
    promedio_entero=suma_notas//3
    
    print("========================\n    FICHA DEL ALUMNO\n========================")
    print(f"Nombre: {nombre_limpio}")
    print(f"Email: {email_minusculas}")
    print(f"Caracteres en nombre: {cant_nombre}")
    print(f"Iniciales: {iniciales}")
    print(f"Usuario: {usuario}")
    print(f"Email valido: {email_valido}")
    print(f"Dominio: {dominio_email}")
    print(f"Nombre para archivo: {nombre_guion}")
    print(f"Cantidad de a: {cant_a}")
    print(f"Codigo secreto: {codigo}")
    print(f"Nota 1: {nota1}")
    print(f"Nota 2: {nota2}")
    print(f"Nota 3: {nota3}")
    print(f"Suma: {suma_notas}")
    print(f"Promedio: {promedio}")
    print(f"Promedio entero: {promedio_entero}")
    print("="*24)
