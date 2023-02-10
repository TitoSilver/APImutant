# APImutant

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

## Intro

Se creo este proyecto usando fastAPI y siguiendo la estructura de arquitectura hexagonal.

Este proyecto ayuda a Magneto a detectar mutantes, validando el ADN de personas. 

## Estructura del Projecto

![project_structure](docs/project_structure.png)

## Tecnologias Usadas

- Python 3.10
- FastAPI
- MongoDB

## Pre Requisitos

Asegurese de haber instalado todos los requisitos y levantado los servicios previos en la maquina de desarollo.

- [Python 3.10](https://www.python.org/downloads/)
- [GIT](https://git-scm.com/downloads)
- [MongoDB](https://www.mongodb.com/try/download/community)

## Como ejecutar

- instalar el modulo virtualenv de python
```bash
pip install virtualenv
```

- crear un enviroment con el comando:
```bash
python -m venv env
```

- acceder al env:

**_NOTE_** en Windows:
```bash
env/Script/activate
```

**_NOTE_** en Linux/Mac:
```bash
source env/bin/activate
```

- instalar dependencias de requirements.txt:
```bash
pip install -r requirements.txt
```

-correr la aplicacion en el root del repositorio:
```bash
python -m src.app
```

-se visualiza todos los endpoints a traves de:

http://localhost:8000/docs

## TEST

**_NOTE:_**  tener en cuenta si en la consola detecta el alias python, existen exepciones como:
- python
- python3
- py
- py3

**_NOTE:_** validar usando el 'alias de python' --version

```bash
python -m unittest test.unit.test_mutants
```



