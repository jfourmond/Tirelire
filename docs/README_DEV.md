# Tirelire

| [<img alt="FOURMOND Jérôme" src="https://avatars2.githubusercontent.com/u/15089371" width="100">](https://github.com/jfourmond) |
|:-------------------------------------------------------------------------------------------------------------------------------:|
|                                           [@jfourmond](https://github.com/jfourmond)                                            |
|                                             Dernière modification   : *17/12/2022*                                              |
|                                                           **v0.0.1**                                                            |

L'application **Tirelire** a été réalisée dans le cadre d'une évaluation technique. L'énonce ne sera pas partagée
dans ce répertoire.

L'idée ici est de simuler l'utilisation d'une tirelire. 

A utilisateur unique, les options d'administration, de création d'utilisateur ou de connexion ont été omises.

## Cloner le projet

- `git clone git@github.com:jfourmond/Tirelire.git`

## Prérequis

- Python 3.10
- Postgresql

### Ubuntu

1. Création de l'environnement virtuel python :
    - `python -m venv env`
2. Activation de l'environnement :
    - `source env/bin/activate`
3. Installation des paquets python :
    - `pip install -r requirements.txt`

### Base de données

### Database - Postgresql

Exécution de la base de données via Docker :
   - `docker compose -f docker-compose.yml up`

## Exécution

Vous souhaitez développer ? Travailler en local ? Spécifier la variable d'environnement DJANGO_SETTINGS_MODULE avec 
les options locales :
   - `export DJANGO_SETTINGS_MODULE=piggy_bank.settings_local`

### Migration 

> `python manage.py migrate`

### App - Django

> `python manage.py runserver`
