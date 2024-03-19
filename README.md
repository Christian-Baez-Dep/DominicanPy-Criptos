import pandas as pd

# Obtener datos históricos de precios
def obtener_datos_historicos(moneda):
    url = f"https://api.coinmarketcap.com/v1/ticker/{moneda}/historical-data/?start=20150101&end=20151231"
    respuesta = requests.get(url)
    datos = respuesta.json()
    return datos

# Calcular porcentaje de cambio
def calcular_cambio(precio_inicial, precio_final):
    return (precio_final - precio_inicial) / precio_inicial * 100

# Calcular desviación estándar
def calcular_desviacion_estandar(precios):
    return np.std(precios)

# Función principal
def criptomonedas_auge_estabilidad():
    # Obtener datos de criptomonedas
    monedas = ["bitcoin", "ethereum", "litecoin", "ripple", "tether", "usd-coin", "dogecoin", "monero", "dash", "iota"]

    # Almacenar resultados
    mejor_auge = []
    mejor_estabilidad = []
    mejoras_significativas = []

    for moneda in monedas:
        # Obtener datos históricos
        datos = obtener_datos_historicos(moneda)

        # Convertir a DataFrame
        df = pd.DataFrame(datos["prices"])

        # Calcular precio inicial y final
        precio_inicial = df["close"][0]
        precio_final = df["close"][-1]

        # Calcular cambio y desviación estándar
        cambio = calcular_cambio(precio_inicial, precio_final)
        desviacion_estandar = calcular_desviacion_estandar(df["close"])

        # Agregar a la lista de mejores
        mejor_auge.append({"nombre": moneda, "cambio": cambio})
        mejor_estabilidad.append({"nombre": moneda, "desviacion_estandar": desviacion_estandar})

        # Evaluar mejoras significativas
        mejora_significativa = False
        if cambio > 100 or (df["market_cap"][-1] - df["market_cap"][0]) > 100000000:
            mejora_significativa = True
            descripcion = "Aumento del precio del " + str(round(cambio, 2)) + "%."
            if cambio > 100:
                descripcion = "Aumento de la capitalización de mercado en $" + str(round((df["market_cap"][-1] - df["market_cap"][0]) / 1000000, 2)) + " millones."

        if mejora_significativa:
            mejoras_significativas.append({"nombre": moneda, "mejora": descripcion})

    # Ordenar listas
    mejor_auge.sort(key=lambda x: x["cambio"], reverse=True)
    mejor_estabilidad.sort(key=lambda x: x["desviacion_estandar"])

    return mejor_auge, mejor_estabilidad, mejoras_significativas

# Obtener resultados
mejor_auge, mejor_estabilidad, mejoras_significativas = criptomonedas_auge_estabilidad()

# Imprimir resultados
print("*Mejor auge:*")
for moneda in mejor_auge[:10]:
    print(f"- {moneda['nombre']}: {moneda['cambio']:.2f}%")

print("\n*Mejor estabilidad:*")
for moneda in mejor_estabilidad[:10]:
    print(f"- {moneda['nombre']}: {moneda['desviacion_estandar']:.2f}")

print("\n*Mejoras significativas:*")
for moneda in mejoras_significativas:
    print(f"- {moneda['nombre']}: {moneda['mejora']}")
