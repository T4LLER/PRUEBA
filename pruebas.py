import openpyxl as pxl
import os

libro = pxl.load_workbook('//NAS1.plastimaxsa.local/Repuestos/Maquinaria Planta/INDICE DE CARPETAS.xlsx')#Se coloca direccion del archivo el cual necesitamos los datos
hoja = libro['Hoja1']#comando para abrir la hoja en donde se trabajara

print(hoja['A2'].value) #comando que permite extraer el valor contenido en la celda 
os.chdir("//NAS1.plastimaxsa.local/Repuestos/Maquinaria Planta/PET")#Comando donde se ingresa la direccion en donde se va a trabajar

for i in range(2,13):
    nombre_conta ='{}{}'.format('C',str(i))
    nombre_planta ='{}{}'.format('D',str(i))
    nombre_archivo = 'maquina_conta_{}_planta_{}'.format(hoja[nombre_conta].value,hoja[nombre_planta].value)
    print(nombre_archivo)
    os.mkdir(nombre_archivo)

print(os.getcwd())
print(os.listdir())

