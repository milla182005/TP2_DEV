# TP2_DEV
# TP2 dév : packaging et environnement de dév local

Une fois que tu sais bien manipuler Docker, tu peux :

- dév sur ton PC avec ton IDE préféré
- run ton code dans des conteneurs éphémères
- avoir des services sur lesquels reposent ton code dans des conteneurs éphémères (genre une base de données)
- n'avoir littéralement
  - AUCUN langage ni aucune lib installés sur ta machine
  - aucun service en local ni dans une VM (une base de données par exemple)

Concrètement, Docker ça te permet donc surtout de :

➜ **avoir 150k environnements de dév à ta portée**

- une commande `docker run` et PAF t'as un new langage
- dans une version spécifique
- avec des libs spécifiques
- dans des versions spécifiques

➜ **ne pas pourrir ta machine**

- dès que t'as plus besoin d'exécuter ton code...
- ...tu détruis le conteneur
- ce sera très simple d'en relancer un demain pour continuer à dév
- quand tu dév, t'as l'env qui existe, quand tu dév pas, il existe plus
- mais tu perds 0 temps dans la foulée

> 0,5 sec le temps de `docker run` my bad. Si c'est ça le coût de la manoeuvre...

➜ **t'abstraire de ton environnement à toi**

- tu crées un environnement isolé avec sa logique qui n'est pas celle de ton système hôte
- donc on s'en fout de ce qu'il y a sur ton hôte, c'est isolé
- je pense aux dévs sous Windows qui ont install' plusieurs Go de libs pour juste `aiohttp` en cours parce que Windows l'a décidé :x

➜ **partager ton environnement**

- bah ouais t'as juste à filer ton `Dockerfile` et ton `docker-compose.yml`
- et n'importe qui peut exécuter ton code dans le même environnement que toi
- n'importe qui c'est principalement :
  - d'autres dévs avec qui tu dév
  - des admins qui vont héberger ton app
  - des randoms qui trouvent ton projet github cool

➜ **pop des services éphémères**

- genre si ton app a besoin d'une db
- c'est facile d'en pop une en une seule commande dans un conteneur
- la db est dispo depuis ton poste
- et tu détruis le conteneur quand tu dév plus

![Docker was born](./img/ship_ur_machine.png)

## Sommaire

- [TP2 dév : packaging et environnement de dév local](#tp2-dév--packaging-et-environnement-de-dév-local)
  - [Sommaire](#sommaire)
- [I. Packaging](#i-packaging)
  - [1. Calculatrice](#1-calculatrice)
  - [2. Chat room](#2-chat-room)
  - [3. Ur own](#3-ur-own)
  - [4. Un ptit mot](#4-un-ptit-mot)

# I. Packaging

## 1. Calculatrice

➜ **Créez un dépôt git dédié au code de votre calculatrice**

- on parle du [TP4](https://gitlab.com/it4lik/b2-network-2024/-/blob/main/tp/dev/4/3_compute/README.md) ou [TP5](https://gitlab.com/it4lik/b2-network-2024/-/blob/main/tp/dev/5/calc.md) de réseau (si t'as fait l'opti calculatrice)
- vous y mettez :
  - votre serveur calculatrice (un fichier `.py`)
  - le client (un fichier `.py`)
- dans le rendu pour ce TP, vous indiquerez juste le lien vers votre dépôt calculatrice

➜ **Packager dans une image Docker l'application de calculatrice réseau**

- packaging du serveur, **pas le client**
- créer un `Dockerfile` qui permet de build une image qui contient votre calculatrice
  - `FROM` ce que vous voulez
  - il faut qu'il y ait Python
  - les librairies s'il y a des libs pour votre calculatrice
  - un `ENTRYPOINT` qui lance automatiquement la calculatrices

➜ **Environnement : adapter le code**

- on doit pouvoir choisir sur quel port écoute la calculatrice au lancement du conteneur
  -  on peut définir la variable d'environnement `CALC_PORT` pour le conteneur
  -  par exemple `CALC_PORT=8888`
- votre code doit donc :
  - récupérer la valeur de la variable d'environnement `CALC_PORT` si elle existe
  - vous devez vérifier que c'est un entier
  - écouter sur ce port là
- ainsi, on peut choisir le port d'écoute comme ça avec `docker run` :

```bash
$ docker run -e CALC_PORT=6767 -d calc
```

➜ **Adapter le `Dockerfile`**

- définir la variable d'environnement `CALC_PORT` à sa valeur par défaut directement dans le `Dockerfile`
- comme ça, y'a une valeur par défaut !

➜ **Ecrire un `docker-compose.yml`**

- créer un `docker-compose.yml` qui permet de lancer votre image calculatrice
- il build automatiquement le `Dockerfile` pour lancer la calculatrice
  - on peut faire ça en ajoutant une clause `build:` dans le `docker-compose.yml`

➜ **Logs : adapter le code si besoin**

- tous les logs de la calculatrice DOIVENT sortir en sortie standard
  - genre si tu le lances à la main ton code, ça print les logs dans le terminal
- en effet, il est courant qu'un conteneur génère tous ses logs en sortie standard
- parce qu'en fait, on peut consulter tout ce qu'a print le conteneur dans son terminal avec la commande `docker logs`

```bash
docker logs <ID_or_name>
```

🌞 **Le lien vers ton dépôt**

- dans le compte-rendu, le lien vers le dépôt git de ta calculatrice, et c'est tout
- il doit donc contenir :
  - le code serveur
  - le code client
  - un `Dockerfile`
  - un `docker-compose.yml`
  - un `README.md`
    - il donne un exemple de commande build
    - il donne un exemple de commande pour up le `docker-compose.yml`
    - il explique qu'on peut modifier le port d'écoute en modifiant une variable d'environnement

## 2. Chat room

![Cat Whale](./img/cat_whale.png)

➜ Idem, tu crées un dépôt git dédié pour ça

- tu peux aussi te reservir de ton dépôt git déjà existant pour la chat room (normalement)

🌞 **Packager l'application de chat room**

- uniquement le lien du dépôt git dans le compte-rendu
- pareil : on package le serveur (pas le client)
- `Dockerfile` et `docker-compose.yml` à ajouter
- code à adapter :
  - logs en sortie standard
  - variable d'environnement `CHAT_PORT` pour le port d'écoute
  - variable d'environnement `MAX_USERS` pour limiter le nombre de users dans chaque room (ou la room s'il y en a qu'une)
- encore un `README.md` propre qui montre comment build et comment run (en démontrant l'utilisation des variables d'environnement)

## 3. Ur own

T'es un dév, donc tu dév nan ? Sur du code non ? :d

🌞 **Packager une application à vous**

- que vous avez dév en cours, ou en perso
- dans l'idéal, un truc où y'a au moins deux conteneurs, que ce soit rigolo, mais np sinon
- ajoutez une gestion de variable d'environnement pareil ce serait cool et sûrement utile ?
- écrivez un `Dockerfile` qui porte l'environnement de votre application
- écrivez un `docker-compose.yml` qui lance les bails
- écrivez un `README.md` qui donne la commande pour lancer les bails
- (ré)utilisez un dépôt git dédié
  - je veux pouvoir juste le clone, et suivre le `README.md` qui m'indique la commande `docker compose`

## 4. Un ptit mot

➜ **J'espère que ces cours vous ont apporté du recul sur la relation client/serveur**

- deux programmes distincts, chacun a son rôle
  - le serveur
    - est le gardien de la logique, le maître du jeu, garant du respect des règles
    - c'est votre bébé vous le maîtrisez
    - opti et sécu en tête
  - le client c'est... le client
    - faut juste qu'il soit joooooli
    - garder à l'esprit que n'importe qui peut le modifier ou l'adapter
    - ou carrément dév son propre client
- y'a même des milieux comme le web, où les gars qui dév les serveurs (Apache, NGINX, etc) c'est pas DU TOUT les mêmes qui dévs les clients (navigateurs Web, `curl`, librairie `requests` en Python, etc)
