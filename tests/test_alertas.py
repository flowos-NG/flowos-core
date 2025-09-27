from src.alertas.alertas import crear_alerta, enviar_alerta

def test_crear_alerta():
    a = crear_alerta("Mensaje")
    assert a["mensaje"] == "Mensaje"
    assert a["enviada"] == False

def test_enviar_alerta():
    a = crear_alerta("Mensaje")
    enviar_alerta(a)
    assert a["enviada"] == True
