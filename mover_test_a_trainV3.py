
import os
import random
import shutil

directorio = "Dataset-32000"

dir_train = f"{directorio}/TRAINING"
dir_val = f"{directorio}/VALIDATION"
dir_test = f"{directorio}/TESTING"

lista_razas = os.listdir(dir_train)

# Ejecutar solo para crear las clases en 'validation' y 'testing'
# for raza in lista_razas:
#     os.mkdir(f'{dir_val}/{raza}')
#     os.mkdir(f'{dir_test}/{raza}')

#--------------------------------MOVER TODAS LAS FOTOS DE TESTING Y VALIDATION A TRAINING--------------------------------#
for raza in lista_razas:
    nombres_fotos_test = os.listdir(f'{dir_test}/{raza}')
    nombres_fotos_val = os.listdir(f'{dir_val}/{raza}')
    for foto_a_mover in nombres_fotos_test:
        shutil.move(src=f'{dir_test}/{raza}/{foto_a_mover}', dst=f'{dir_train}/{raza}')
    os.rmdir(f'{dir_test}/{raza}')
    for foto_a_mover in nombres_fotos_val:
        shutil.move(src=f'{dir_val}/{raza}/{foto_a_mover}', dst=f'{dir_train}/{raza}')
    os.rmdir(f'{dir_val}/{raza}')

print('TODO MOVIDO A TRAINING')
#--------------------------------MOVER TODAS LAS FOTOS DE TESTING Y VALIDATION A TRAINING--------------------------------#

#--------------------------------MOVER 10% FOTOS A TESTING Y 20% A VALIDATION--------------------------------#
for raza in lista_razas:
    os.mkdir(f'{dir_val}/{raza}')
    os.mkdir(f'{dir_test}/{raza}')
    nombres_fotos = os.listdir(f'{dir_train}/{raza}')
    cantidad_fotos_raza = len(nombres_fotos)

    diezmo = int(cantidad_fotos_raza * 0.1)
    diezmoX2 = int(cantidad_fotos_raza * 0.2)

    for i in range(diezmoX2): # para validación
        nombre_a_mover = nombres_fotos.pop(random.randrange(len(nombres_fotos))) 
        shutil.move(f'{dir_train}/{raza}/{nombre_a_mover}', f'{dir_val}/{raza}')
    for i in range(diezmo): # para test
        nombre_a_mover = nombres_fotos.pop(random.randrange(len(nombres_fotos))) 
        shutil.move(f'{dir_train}/{raza}/{nombre_a_mover}', f'{dir_test}/{raza}')

print('TODO MOVIDO A VALIDATION y TESTING')
#--------------------------------MOVER 10% FOTOS A TESTING Y 20% A VALIDATION--------------------------------#

