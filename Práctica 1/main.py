from colorama import Fore
from tkinter import filedialog
import tkinter
import sys
from producto import Producto



db = []

root = tkinter.Tk()
root.withdraw()

def lectura():
     
    file = filedialog.askopenfilename(initialdir="C:/Users/sebas/Documents/USAC/Segundo Semestre 2023/Lab LFP/Práctica 1/Archivos de Entrada",title="Elige un archivo de entrada", filetypes=(("Archivos de Datos","*.inv*"),("Todos los archivos","*.*")))
    
    with open(file, mode="r") as archivo:
        for linea in archivo:
            if "crear_producto" in linea:
                linea = linea.replace("crear_producto","")
                linea = linea.replace("\n","")
                splitted_line = linea.split(";")
                try:
                    name = splitted_line[0]
                    quantity = int(splitted_line[1])
                    price = float(splitted_line[2])
                    location = splitted_line[3]
                    newProduct = Producto(name,quantity,price,location)
                    db.append(newProduct)
                except:
                    print(Fore.RED+"EL PRODUCTO NO PUEDE SER CREADO, NO CUMPLE CON LOS REQUERIMIENTOS"+Fore.WHITE)
        archivo.close()
        root.destroy()

def movimientos():
    
    file = input(Fore.CYAN+"INGRESE LA RUTA DEL ARCHIVO"+"\n"+Fore.WHITE)
    file = file.replace("\\","/")
    file = file.replace('"',"")

    with open(file, mode="r") as archivo:
        for linea in archivo:
            if "agregar_stock" in linea:
                linea = linea.replace("agregar_stock","")
                linea = linea.replace("\n","")
                splitted_line = linea.split(";")
                name = splitted_line[0]
                quantity = int(splitted_line[1])
                location = splitted_line[2]
                for i in range(len(db)):
                    if name == (db[i].nombre):
                        if location == (db[i].ubicacion):
                            if quantity>=0:
                                db[i].cantidad=(db[i].cantidad)+quantity
                            else:
                                print(Fore.RED+"LA CANTIDAD INGRESADA ES NEGATIVA"+Fore.WHITE)
                        else:
                             print(Fore.RED+"NO EXISTE EL PRODUCTO"+Fore.YELLOW,name,Fore.RED+"EN LA",location+Fore.WHITE)

            elif "vender_producto" in linea:
                linea = linea.replace("vender_producto","")
                linea = linea.replace("\n","")
                splitted_line = linea.split(";")
                name = splitted_line[0]
                quantity = int(splitted_line[1])
                location = splitted_line[2]
                for i in range(len(db)):
                    if name == (db[i].nombre):
                        if location == (db[i].ubicacion):
                            if quantity<=(db[i].cantidad) and quantity>=0:
                                db[i].cantidad=(db[i].cantidad)-quantity
                            else:
                                print(Fore.RED+"NO EXISTE TANTO STOCK DEL PRODUCTO"+Fore.YELLOW,name,Fore.RED+"EN LA",location,"\nEL STOCK ACTUAL ES DE:",Fore.YELLOW+str(db[i].cantidad)+Fore.WHITE)
                        else:
                             print(Fore.RED+"NO EXISTE EL PRODUCTO"+Fore.YELLOW,name,Fore.RED+"EN LA",location+Fore.WHITE)
        archivo.close()

def inventario():
    print("\n"+Fore.MAGENTA+"INFORME DE INVENTARIO")
    print(Fore.WHITE+"=================================================================================================")
    print(Fore.WHITE+"|"+Fore.MAGENTA+"    Producto    "+Fore.WHITE+"|"+Fore.MAGENTA+"    Cantidad    "+Fore.WHITE+"|"+Fore.MAGENTA+"    Precio Unitario    "+Fore.WHITE+"|"+Fore.MAGENTA+"    Valor Total    "+Fore.WHITE+"|"+Fore.MAGENTA+"    Ubicacion    "+Fore.WHITE+"|")
    print(Fore.WHITE+"-------------------------------------------------------------------------------------------------\n")
    for i in range(len(db)):
        if len(db[i].nombre)>8:
            print(Fore.CYAN+"   "+db[i].nombre+"     "+"        "+str(db[i].cantidad)+"         "+"        "+str(db[i].precio)+"     "+"             "+str((db[i].precio)*(db[i].cantidad))+"   "+"          "+db[i].ubicacion+"  ")
        else:
            print(Fore.CYAN+"    "+db[i].nombre+"     "+"        "+str(db[i].cantidad)+"         "+"        "+str(db[i].precio)+"     "+"             "+str((db[i].precio)*(db[i].cantidad))+"   "+"          "+db[i].ubicacion+"  ")


def menu():
    boolean = True
    a = 1
    while boolean==True:
        print("\n"+Fore.LIGHTCYAN_EX+"-----------------------------------------------------------")
        print(Fore.LIGHTYELLOW_EX+"Practica 1 - Lab Lenguajes Formales y de Programacion")
        print(Fore.LIGHTCYAN_EX+"-----------------------------------------------------------"+"\n")
        print(Fore.GREEN+"SISTEMA DE INVENTARIO"+"\n")
        print(Fore.WHITE+"1. Cargar inventario inicial")
        print("2. Cargar instrucciones de movimientos")
        print("3. Crear informe de inventario")
        print("4. Salir"+"\n\n")
        print(Fore.GREEN+"Ingrese una opcion:"+"\n")
        try:
            a = int(input())
            if a==1:
                input("\n"+Fore.WHITE+"PRESIONE ENTER PARA ESCOGER UN ARCHIVO")
                lectura()
                input("\n"+Fore.BLACK+"PRESIONE PARA CONTINUAR AL MENU")
            elif a==2:
                input("\n"+Fore.WHITE+"PRESIONE ENTER PARA ESCOGER UN ARCHIVO")
                movimientos()
                input("\n"+Fore.BLACK+"PRESIONE PARA CONTINUAR AL MENU")
            elif a==3:
                inventario()
                input("\n"+Fore.BLACK+"PRESIONE PARA CONTINUAR AL MENU")
            elif a==4:
                boolean = False
                print(Fore.YELLOW+"GRACIAS POR USAR NUESTRO SERVICIO"+Fore.WHITE)
                sys.exit()
        except:
            print("\n"+Fore.RED+"OPCION NO VALIDA"+"\n")

menu()