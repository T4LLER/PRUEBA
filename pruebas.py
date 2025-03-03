import openpyxl as pxl
import os

libro = pxl.load_workbook('//NAS1.plastimaxsa.local/Repuestos/Maquinaria Planta/INDICE DE CARPETAS.xlsx')#Se coloca direccion del archivo el cual necesitamos los datos
hoja = libro['Hoja1']

print(hoja['A2'].value)   
os.chdir("//NAS1.plastimaxsa.local/Repuestos/Maquinaria Planta/PET")#posicionarse en la carpeta donde se generaran los cambios

#for i in range(2,13):
#    nombre_conta ='{}{}'.format('C',str(i))
#    nombre_planta ='{}{}'.format('D',str(i))
#    nombre_archivo = 'maquina_conta_{}_planta_{}'.format(hoja[nombre_conta].value,hoja[nombre_planta].value)
#    print(nombre_archivo)
#    os.mkdir(nombre_archivo)

#os.chdir("//NAS1.plastimaxsa.local/Repuestos/Maquinaria Planta/Sopladoras")
print(os.getcwd())
print(os.listdir())

#os.mkdir()