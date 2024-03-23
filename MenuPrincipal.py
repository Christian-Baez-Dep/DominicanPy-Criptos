import sys
from Funcionalidades.ExtrDatos import DatosCSV 
from Funcionalidades.Filtrador import Filtrator as fl
from Funcionalidades.Preprocesador import PrepocedarorDatos as ppd
from Menu_Monedas_Importantes import Monedas_Interesantes_2015
from Menu_Medias import Menu_Mean
from Funcionalidades.MarketCrypto import Market
from Menu_Monedas_UltimoTrimestre import Monedas_Ultimotrismetre
from Menu_Medias_2015 import Menu_Mean_2015
from Menu_Grafica_Precio import Grafica_Precios
from Menu_Grafica_Capi import Grafica_Capitalizacion
from Funcionalidades.Fluctu import Fluctuador
import numpy as np
from Menu_Grafica_Fluctuaciones import Grafica_Fluctuaciones
from Menu_Grafica_Calor import Grafica_Calor
from Menu_Grafica_Dispersion import Grafica_Dispersion
class MenuPrici:
    def __init__(self) -> None:
        pass
    
    def MostrarMenu():
        salida = False
        
        while salida == False:
            bienvenida = "Bienvenido a DominicanPy"
            print("_"*40 + bienvenida + "_"*40 )
            print("|" + " " * (78 + len(bienvenida)) + "|")

            print("|" + "Que desea hacer?" + " "*86  + "|")
            print("|" + " " * (78 + len(bienvenida)) + "|")
            print("|" + "1- Ver la media de las criptomonedas en 2015" + " "*58  + "|")
            print("|" + "2- Ver las mas importantes de 2015" + " "*68  + "|")
            print("|" + "3- Ver las medias de las diferentes criptomonedas" + " "*53  + "|")
            print("|" + "4- Ver las criptomonedas que tuvieron mayor valor en el ultimo trimestre de 2015" + " "*22  + "|")
            print("|" + "5- Ver la moneda mas estable de 2015" + " "*66  + "|")
            print("|" + "6- Ver la moneda mas inestable de 2015" + " "*64  + "|")
            print("|" + "7- Grafica de las monedas 2015 (precios)" + " "*62  + "|")
            print("|" + "8- Grafica de las monedas 2015 (capitalizacion)" + " "*55  + "|")
            print("|" + "9- Grafica de las monedas (precios)" + " "*67  + "|")
            print("|" + "10- Grafica de las monedas (capitalizacion)" + " "*59  + "|")
            print("|" + "11- Grafica de las fluctuaciones de las monedas 2015 (porcentual)" + " "*37  + "|")
            print("|" + "12- Grafica de las fluctuaciones de las monedas 2015 (regular)" + " "*40  + "|")
            print("|" + "13- Grafica de correlacion de las monedas 2015 (calor)" + " "*41  + "|")
            print("|" + "14- Grafica de correlacion de las moneda (dispersion)" + " "*34  + "|")
            print("|" + "15- Grafica de correlacion de las moneda (calor)" + " "*34  + "|")

            print("|" + " " * (78 + len(bienvenida)) + "|")
            print("|" + " " * (78 + len(bienvenida)) + "|")
            print( "*"* (80 + len(bienvenida)) )
            MenuPrici.InputUser()
            print('Desea salir del sistema? si/no')
            opc = input()
            
            if opc.lower() == 'si':
                salida = True
                  
    def InputUser():
        exc = DatosCSV()
        datos = exc.extraer_archivos_csv()
        ppd.NormalizarFecha(datos)
        ppd.RellenarNulos(datos)
        ppd.CambioDeTipo(datos)
        
        datos_2015 = fl.Get_Datos_2015(datos)
        salida = False
        fluctuaciones,fluc_regu, fluctuacion_mayor, fluctuacion_menor= Fluctuador.sacar_fluctuaciones(datos_2015)
        while salida == False:
            opc = input()
            if opc == "1":
                Menu_Mean_2015.MostrarMenu(datos_2015)
                salida = True
            elif opc == "2":
                Monedas_Interesantes_2015.MostrarMenu(datos_2015)
                salida = True
            elif opc == "3":
                Menu_Mean.MostrarMenu(datos)
                salida = True
            elif opc == "4":
                newDf = Market.datos_interesantes()
                Monedas_Ultimotrismetre.MostrarMenu(newDf)
                salida = True
            elif opc == "5":
                print(fluctuacion_mayor)
                salida = True
            elif opc == "6":
                print(fluctuacion_menor)
                salida = True
            elif opc == "7":
                Grafica_Precios.MostrarGrafica(datos_2015)
                salida = True
            elif opc == "8":
                Grafica_Capitalizacion.MostrarGrafica(datos_2015)
                salida = True
            elif opc == "9":
                Grafica_Precios.MostrarGrafica(datos)
                salida = True
            elif opc == "10":
                Grafica_Capitalizacion.MostrarGrafica(datos)
                salida = True
            elif opc == "11":
                Grafica_Fluctuaciones.MostrarGrafica(datos_2015, fluctuaciones)
                salida = True
            elif opc == "12":
                Grafica_Fluctuaciones.MostrarGrafica(datos_2015, fluc_regu)
                salida = True
            elif opc == "13":
                Grafica_Calor.MostrarGrafica(datos_2015)
                salida = True
            elif opc == "14":
                Grafica_Dispersion.MostrarGraficoDispersion(datos)
                salida = True           
            elif opc == "15":
                Grafica_Calor.MostrarGrafica(datos)
                salida = True


            else:
                sys.stdout.write("\x1b[1A\x1b[2K")
                sys.stdout.flush()

MenuPrici.MostrarMenu()
print("Adios")
