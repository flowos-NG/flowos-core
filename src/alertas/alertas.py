def crear_alerta(mensaje):
    return {"mensaje": mensaje, "enviada": False}

def enviar_alerta(alerta):
    alerta["enviada"] = True
    print(f"Enviando alerta: {alerta['mensaje']}")
