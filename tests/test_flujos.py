from src.flujos.flujos import crear_flujo, agregar_paso

def test_crear_flujo():
    f = crear_flujo("Flujo1")
    assert f["nombre"] == "Flujo1"
    assert f["pasos"] == []

def test_agregar_paso():
    f = crear_flujo("Flujo1")
    agregar_paso(f, "Paso1")
    assert f["pasos"] == ["Paso1"]
