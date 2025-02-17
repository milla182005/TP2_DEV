# Serveur de Calculatrice 

## Description 

Ce projet contient un serveur de calculatrice simple et un client. Le serveur écoute les connexions entrantes, reçoit des expressions mathématiques, les évalue et renvoie le résultat. Le client envoie des expressions mathématiques au serveur et affiche le résultat.

## Prérequis

- Docker
- Doker Compose
- python 

## Configuration

### Construction de l'image Docker

Pour construire l'image Docker pour le serveur de calculatrice, naviguez vers le répertoire du projet et exécutez :

```sh
docker-compose build

```

  Exécuter le conteneur Docker

Pour exécuter le conteneur Docker pour le serveur de calculatrice, utilisez :

```sh
docker-compose up

```

Par défaut, le serveur écoute sur le port 8889. Vous pouvez spécifier un port différent en définissant la variable d'environnement CALC_PORT :

```sh
CALC_PORT=6767 docker-compose up

```

Exécuter le client

Pour exécuter le client et envoyer un message au serveur, utilisez la commande suivante :

```sh
python client.py "2 + 2"

```


## En résumé 

Commandes d'exemple

Construire l'image Docker

```sh
docker-compose build

```

Exécuter le conteneur Docker

```sh
docker-compose up

```

Exécuter le client

```sh
python client.py "2 + 2"

```

Spécifier un port différent

```sh
CALC_PORT=6767 docker-compose up

python client.py "2 + 2" localhost 6767

```

