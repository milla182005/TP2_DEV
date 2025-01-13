import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Tentative de connexion au serveur...")
sock.connect(('10.1.1.2', 8889))

# Envoyer un message de bienvenue
sock.send('Hello'.encode())

data = sock.recv(1024)
print(f"Message reçu du serveur : {data.decode()}")

# Récupérer une string saisie par l'utilisateur
msg = input('Calcul à envoyer (ex: "3 + 3"): ')

# Encoder le message explicitement en UTF-8 pour récupérer un tableau de bytes
encoded_msg = msg.encode('utf-8')

# Calculer sa taille, en nombre d'octets
msg_len = len(encoded_msg)

# Encoder ce nombre d'octets sur une taille fixe de 4 octets
header = msg_len.to_bytes(4, byteorder='big')

# Concaténer ce header avec le message, avant d'envoyer sur le réseau
payload = header + encoded_msg

# Envoyer le payload sur le réseau
print(f"Envoi du message : {payload}")
sock.send(payload)

# Recevoir le résultat du serveur
result = sock.recv(1024)
print(f"Résultat reçu du serveur : {result.decode()}")

sock.close()