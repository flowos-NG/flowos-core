def crear_flujo(nombre):
    return {"nombre": nombre, "pasos": []}

def agregar_paso(flujo, paso):
    flujo["pasos"].append(paso)
    return flujo
