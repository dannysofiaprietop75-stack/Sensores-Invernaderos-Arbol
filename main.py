#Estructura del Árbol
arbol = {
    "cond": "ping_activo",
    "si": {
        "cond": "variacion_mayor_30",
        "si": {
            "cond": "vecinos_cambian",
            "si": "Alerta Ambiental: Activar Riego",
            "no": "Error: Recalibrar Sensor"
        },
        "no": "Operación Normal"
    },
    "no": "Falla de Energía"
}
#Dibujar Árbol y Recorrer
def ver_arbol(nodo, pref=""):
    if isinstance(nodo, str):
        print(f"{pref}└─► [{nodo}]")
        return
    print(f"{pref}├─ ¿{nodo['cond']}?")
    ver_arbol(nodo["si"], pref + "│  (Sí) ")
    ver_arbol(nodo["no"], pref + "   (No) ")

def evaluar(nodo, sensor):
    if isinstance(nodo, str):
        print(f"\nRESULTADO: {nodo}")
        return
    resp = sensor.get(nodo["cond"], False)
    print(f" -> Evaluando [{nodo['cond']}]: {'Sí' if resp else 'No'}")
    evaluar(nodo["si"] if resp else nodo["no"], sensor)


sensor = {"ping_activo": True, "variacion_mayor_30": True, "vecinos_cambian": True}

print("=== ÁRBOL DE DECISIÓN ===")
ver_arbol(arbol)

print("\n=== RECORRIDO ===")
evaluar(arbol, sensor)