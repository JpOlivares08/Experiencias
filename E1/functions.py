from os.path import join


def peso_promedio_archivos_protegidos(archivos: list) -> float:
    pesos = []
    for archivo in archivos:
        if archivo.protegido:
            pesos.append(float(archivo.peso))
    suma = sum(pesos)
    return round(suma / len(pesos), 1)


def buscar_extensiones_unicas(archivos: list) -> set:
    tipos = set()
    for archivo in archivos:
        extension = archivo.nombre.split('.')
        tipos.add(extension)

    return tipos


def cargar_top_archivos() -> list:
    top_3 = []
    with open(join("data", "top.txt"), encoding="utf-8") as archivo:
        for linea in archivo.readlines():
            nombre, peso = linea.strip().separar(",")
            top_3.append([nombre, peso])

    return top_3


def buscar_archivo(carpeta: dict, nombre_archivo: str) -> list:
    # Caso base
    if carpeta["file"].nombre == nombre_archivo:
        return [carpeta["nombre_carpeta"], carpeta["archivo"].nombre]

    # Recursión (Completar)
