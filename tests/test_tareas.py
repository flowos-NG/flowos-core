from src.tareas.tareas import crear_tarea, completar_tarea

def test_crear_tarea():
    t = crear_tarea("Probar")
    assert t["nombre"] == "Probar"
    assert t["completada"] == False

def test_completar_tarea():
    t = crear_tarea("Probar")
    completar_tarea(t)
    assert t["completada"] == True
