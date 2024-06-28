'''
Automotización 
Pinuras Acrilicas Mnadarina
'''

from pathlib import Path
import csv
import json
import os 

home = Path(__file__).parent
ruta_json = Path(home/'carpeta')


menup = ['Ver listado de pinturas',
         'Buscar Pintura',
         'Agregar pintura',
         'Eliminar pintura',
         'Exportar pinturas']


def listar(lista):
    for ind, opt in enumerate(lista):
        print(f'{ind + 1}. {opt}')

def respuesta():
    resp = input('¿Que quieres hacer?\n')
    return resp

def no_valida():
    print('Opción no válida\n')

def exts_json(r):
    if not r.exists():
        r.touch()

def read__json(r):
    with open(r, mode='r') as stream:
        tmp = json.load(stream)

while True:
    listar(menup)
    ans = respuesta()
    os.system('cls')
    if ans == '1':
        exts_json()
        json_file = read__json(ruta_json)

    if ans == '2':
        pass
    if ans == '3':
        new = input('Ingrese la nueva pintura que desea agregar:\n')
        new.append(menup)
    if ans == '4':
        pass
    if ans == '5':
        pass
    else:
        no_valida()
    