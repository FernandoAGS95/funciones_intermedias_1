matriz = [ [10, 15, 20], [3, 7, 14] ]
cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"}
]

ciudades = {
    "México": ["Ciudad de México", "Guadalajara", "Cancún"],
    "Chile": ["Santiago", "Concepción", "Viña del Mar"]
}

coordenadas = [
    {"latitud": 8.2588997, "longitud": -84.9399704}
]
#1
matriz[1][0] = 6
cantantes[0]["nombre"] = "Enrique Martin Morales"
ciudades["México"][2] = "Monterrey"
coordenadas[0]["latitud"] = 9.9355431
print(matriz)
print(cantantes)
print(ciudades)
print(coordenadas)

#2
cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]

def iterarDiccionario(diccionario):
    for i in range(len(diccionario)):
        print("nombre - " + diccionario[i]["nombre"] + ", pais - " + diccionario[i]["pais"])
iterarDiccionario(cantantes)
#3

def iterarDiccionario2(llave, lista):
    for i in range(len(lista)):
        print(lista[i][llave])

iterarDiccionario2("nombre", cantantes)
iterarDiccionario2("pais", cantantes)

#4

costa_rica = {
    "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
    "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
}

def imprimirInformacion(diccionario):
    for llave, lista in diccionario.items():
        print(f"{llave} - {len(lista)}")
        for valor in lista:
            print(valor)

imprimirInformacion(costa_rica)