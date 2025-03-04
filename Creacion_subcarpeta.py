import os

dirección = r"\\NAS1.plastimaxsa.local\Repuestos\Maquinaria Planta\Maquinas auxiliares\Hornos" # Dirección donde se haran las modificaciones
dirección = dirección.replace("\\", "/")#Remplaza los caracteres para que se puedan leer
os.chdir(dirección) #Comando donde se ingresa la direccion en donde se va a trabajar
Lista_carpetas = os.listdir()#Se gurada en nombre de los archivos que estan en la dirección seleccionada
Lista_direcciones = [f"{dirección}{"/"}{Lista_carpetas[a]}" for a in range(len(Lista_carpetas))]#Crea lista con las direcciones a utilizar para creación de carmpetas
print(Lista_direcciones)
Lista_sub_carptetas = ["Planos","Fotografias"]#Ingresar nombre de carpetas a crear en subcarpetas

for a in range(len(Lista_direcciones)):
    os.chdir(Lista_direcciones[a])
    for b in range(len(Lista_sub_carptetas)):
        os.mkdir(Lista_sub_carptetas[b])
        print(Lista_sub_carptetas[b])
   
#direccion_local = os.getcwd() #devuelve la dirección en donde estamos

