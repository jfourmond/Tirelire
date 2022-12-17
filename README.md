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

## Installation

Pour le déploiement passer au titre suivant.

Pour le développement local, consulter le document [README_DEV.md]

À la racine du projet, après clonage :

### Déploiement


1. Construire les images docker :
    - `docker compose build`
2. Créer les containers et les dépendances :
    - `docker compose up`

Le `docker-compose.yml` construit et lance trois containers :
   1. `tirelire-db` lance le container de base de données sous Postgresql, vide
   2. `tirelire-migrate` effectue la création des tables et la ou les migrations nécessaires
   3. `tirelire` lance le container django

Aucun `nginx` n'est utilisé ici.
