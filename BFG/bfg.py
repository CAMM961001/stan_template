import os
import sys
import numpy as np
import pandas as pd

from shutil import copy
from cmdstanpy import CmdStanModel


class StanProject:
    def __init__(self, name:str):
        # Inicializar variables estáticas
        self.NAME = name
        self.CURRENT = os.path.dirname(__file__)
        self.ROOT = os.path.dirname(self.CURRENT)


    def create_stan_project(self, dir='models'):
        """
        Función para crear un proyecto de stan en un directorio
        especificado. El proyecto consta de una carpeta con una 
        plantilla de stan.

        Parámetros:
            dir: str = 'models'. El directorio en el cual se va
                a crear el proyecto stan

        Salidas:
            stan_dir: str. La ruta global del directorio del
                proyecto stan
            stan_file: str. La ruta global del archivo del
                modelo stan
        """

        # Directorio general de modelos
        if not os.path.exists(path = dir):
            os.mkdir(path = dir)
            print(f"Directorio '{dir}' creado!")

        # Ruta a directorio de modelo stan específico
        stan_dir = os.path.join(dir, self.NAME)
        stan_dir = os.path.join(self.ROOT, stan_dir)
        
        # Directorio de modelo stan específico
        if not os.path.exists(path = stan_dir):
            os.mkdir(path = stan_dir)

        # Ruta a archivo stan
        stan_file = os.path.join(stan_dir, f'{self.NAME}.stan')

        # Generar plantilla stan en caso de no existir
        if not os.path.exists(path = stan_file):        
            try:
                # Cargar plantilla stan en memoria
                template = os.path.join(self.CURRENT, '__template__.stan')

                # Crear plantilla de stan en directorio específico
                copy(template, stan_dir)

            except FileNotFoundError:
                # Excepción en caso de no existir plantilla en BFG
                print("Archivo '__template__.stan' faltante en módulo BFG!")
                sys.exit(1)

            # Renombrar plantilla con nombre de archivo stan
            template = os.path.join(stan_dir, '__template__.stan')
            os.rename(template, stan_file)

            print(f"Proyecto '{self.NAME}' creado!")

        else:
            # En caso de que exista un proyecto previo
            print(f"Ya existe un proyecto llamado '{self.NAME}'")

        return stan_dir, stan_file


if __name__ == '__main__':
    name = 'test'
    stp = StanProject(name)
    dir, name = stp.create_stan_project()
    print(dir)
    print(name)
