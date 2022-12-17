# Tirelire

| [<img alt="FOURMOND Jérôme" src="https://avatars2.githubusercontent.com/u/15089371" width="100">](https://github.com/jfourmond) |
|:-------------------------------------------------------------------------------------------------------------------------------:|
|                                           [@jfourmond](https://github.com/jfourmond)                                            |
|                                             Dernière modification   : *17/12/2022*                                              |
|                                                           **v0.0.1**                                                            |

L'application **Tirelire** a été réalisée dans le cadre d'une évaluation technique. L'énoncé ne sera pas partagé
dans ce répertoire.

L'idée ici est de simuler l'utilisation d'une tirelire. 

À utilisateur unique, les options d'administration, de création d'utilisateur ou de connexion ont été omises.

## Cloner le projet

- `git clone git@github.com:jfourmond/Tirelire.git`

## Prérequis

- Python 3.10
- Postgresql

## Installation

Pour le déploiement passer au titre suivant.

Pour le développement local, consulter le document [README_DEV.md](./docs/README_DEV.md)

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

### Utilisation

L'API dispose de cinq endpoints :

1. [GET] http://127.0.0.1:8000/ : retourne des informations sur la tirelire actuelle

**OUTPUT**

```json
{
    "id": 2,
    "broken": false,
    "added": "2022-12-17T22:36:02.223838Z",
    "updated": "2022-12-17T22:36:02.223867Z"
}
```

2. [POST] http://127.0.0.1:8000/save/ : épargne des pièces ou des billets, les ajoute à la tirelire

**INPUT**

```json
{
    "amount": 50,
    "type": "bank_note"
}
```

**OUTPUT**

```json
{
    "type": "bank_note",
    "amount": 50
}
```

3. [GET] http://127.0.0.1:8000/shake/ : indique la valeur du contenant de la tirelire

**OUTPUT**

```json
{
    "value": 50
}
```

4. [POST] http://127.0.0.1:8000/break/ : casse le contenu de la tirelire et retourne son contenu

**OUTPUT**

```json
[
    {
        "id": 1,
        "type": "bank_note",
        "amount": 50,
        "added": "2022-12-17T22:44:11.060025Z"
    }
]
```

5. [POST] http://127.0.0.1:8000/repare/ : répare la tirelire / en créer une nouvelle

**OUTPUT**

```json
{
    "id": 3,
    "broken": false,
    "added": "2022-12-17T22:46:20.554819Z",
    "updated": "2022-12-17T22:46:20.554835Z"
}
```