from producto import Producto
from colorama import Fore
db = []

def lectura():
    with open("Archivos de Entrada/example.inv", mode="r") as archivo:
        for linea in archivo:
            if "crear_producto" in linea:
                linea = linea.replace("crear_producto","")
                linea = linea.replace("\n","")
                splitted_line = linea.split(";")
                name = splitted_line[0]
                quantity = int(splitted_line[1])
                price = float(splitted_line[2])
                location = splitted_line[3]
                newProduct = Producto(name,quantity,price,location)
                db.append(newProduct)
        archivo.close()
        for i in range(len(db)):
            print((db[i].nombre),"con cantidad de",str(db[i].cantidad)) 

def movimientos():
    with open("Archivos de Entrada/movimientos.mov", mode="r") as archivo:
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
                            if quantity<=(db[i].cantidad):
                                db[i].cantidad=(db[i].cantidad)-quantity
                            else:
                                print(Fore.RED+"NO EXISTE TANTO STOCK DEL PRODUCTO"+Fore.YELLOW,name,Fore.RED+"EN LA",location,"\nEL STOCK ACTUAL ES DE:",Fore.YELLOW+str(db[i].cantidad)+Fore.WHITE)
                        else:
                             print(Fore.RED+"NO EXISTE EL PRODUCTO"+Fore.YELLOW,name,Fore.RED+"EN LA",location+Fore.WHITE)
        archivo.close()
        for i in range(len(db)):
                    print((db[i].nombre),"con cantidad de",str(db[i].cantidad))    

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
lectura()
movimientos()
inventario()