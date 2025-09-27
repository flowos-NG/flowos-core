def crear_tarea(nombre):
    return {"nombre": nombre, "completada": False}

def completar_tarea(tarea):
    tarea["completada"] = True
    return tarea
