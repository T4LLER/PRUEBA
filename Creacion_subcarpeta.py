import os

#dirección = "/Users/josed/OneDrive/Escritorio/carpeta de prueba" # Dirección donde se haran las modificaciones
dirección = "\Users\josed\OneDrive\Escritorio\carpeta de prueba"
#numero = len(dirección)

cadena_ascii = [ord(a) for a in dirección]

print(cadena_ascii)

#os.chdir(dirección) #Comando donde se ingresa la direccion en donde se va a trabajar
#reconstruccion = [dirección[a] for a in range(numero-17)]#Reconstruye la dirección quitando la ultima palabra para cambiar de dirección 
#base = "".join(reconstruccion)#concatena todos los valores captados por la LISTA COMPRIMIDA
#elementos_dereccion = os.listdir() #Pone en una clase lista los elemtenos que estan en esa dirección a trabajar
#parejas = ["{}{}".format(base,elementos_dereccion[a]) for a in range(len(elementos_dereccion))]

#Lista_sub_carptetas = ["hola","como","estas"]

#print(parejas)

#for a in range(len(parejas)):
#    os.chdir(parejas[a])
#    for b in range(len(Lista_sub_carptetas)):
#        os.mkdir(Lista_sub_carptetas[b])
#        print(Lista_sub_carptetas[b])
   
#os.chdir(dirección) #Comando donde se ingresa la direccion en donde se va a trabajar
#print(os.listdir())
#direccion_local = os.getcwd() #devuelve la dirección en donde estamos

