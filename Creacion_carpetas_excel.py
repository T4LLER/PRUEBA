import openpyxl as pxl
import os

libro = pxl.load_workbook('//NAS1.plastimaxsa.local/Repuestos/Maquinaria Planta/INDICE DE CARPETAS.xlsx')#Se coloca direccion del archivo el cual necesitamos los datos
hoja = libro['Hoja1']#comando para abrir la hoja en donde se trabajara

print(hoja['A2'].value) #comando que permite extraer el valor contenido en la celda 
os.chdir("//NAS1.plastimaxsa.local/Repuestos/Maquinaria Planta/Maquinas auxiliares/Etiquetadora")#Comando donde se ingresa la direccion en donde se va a trabajar

for i in range(2,11):
    nombre_conta ='{}{}'.format('B',str(i))
    nombre_planta ='{}{}'.format('D',str(i))
    #nombre_archivo = 'maquina_conta_{}_planta_{}'.format(hoja[nombre_conta].value,hoja[nombre_planta].value)
    nombre_archivo = 'maquina_{}'.format(hoja[nombre_conta].value)
    print(nombre_archivo)

    os.mkdir(nombre_archivo)

print(os.getcwd())
print(os.listdir())

