def names():
    """Lee nombre y apellido, e imprime el nombre completo en distintos formatos:
    minúsculas, título, mayúsculas y con tabulador.
    """
    pass
    name=input()
    surname=input()
    completeName=name+" "+surname
    print(completeName.lower())
    print(completeName.title())
    print(completeName.upper())
    print("\t"+completeName.lower())