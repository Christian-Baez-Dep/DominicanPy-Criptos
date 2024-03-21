import sys
from Funcionalidades.ExtrDatos import DatosCSV 
from Funcionalidades.Filtrador import Filtrator as fl
from Funcionalidades.Preprocesador import PrepocedarorDatos as ppd
from Menu_Medias import Menu_Mean_2015
from Menu_Monedas_Importantes import Monedas_Interesantes_2015
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
            print("|" + "1- Ver la media de las criptomonedas en 2015" + " "*66  + "|")
            print("|" + "2- Ver las mas importantes de 2015" + " "*68  + "|")
            print("|" + "3- Ver las monedas que estan por encima de la media" + " "*51  + "|")
            print("|" + "4- Ver las medias de las diferentes criptomonedas" + " "*53  + "|")
            print("|" + "5- Ver las criptomonedas que tuvieron mayor valor en el ultimo trimestre de 2015" + " "*22  + "|")
            print("|" + "6- Ver la moneda mas estable de 2015" + " "*66  + "|")
            print("|" + "7- Ver la moneda mas inestable de 2015" + " "*64  + "|")
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
        

        while salida == False:
            opc = input()
            if opc == "1":
                Menu_Mean_2015.MostrarMenu(datos_2015)
                salida = True
            elif opc == "2":
                Monedas_Interesantes_2015.MostrarMenu(datos_2015)
                salida = True

            elif opc == "3":
                print(3)
                salida = True
            elif opc == "4":
                print(4)
                salida = True

            elif opc == "5":
                print(5)
                salida = True
            elif opc == "6":
                print(6)
                salida = True

            elif opc == "7":
                print(7)
                salida = True

            else:
                sys.stdout.write("\x1b[1A\x1b[2K")
                sys.stdout.flush()
        
        

MenuPrici.MostrarMenu()
print("Adios")
