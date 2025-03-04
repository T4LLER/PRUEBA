def cambiar_ruta(ruta):
    return ruta.replace("\\", "/")

ruta_original = r"\Users\josed\OneDrive\Escritorio\carpeta de prueba"
ruta_modificada = cambiar_ruta(ruta_original)

print("Ruta modificada:", ruta_modificada)
