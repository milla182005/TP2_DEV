import socket
import os

# Récupérer la valeur de la variable d'environnement CALC_PORT
port = os.getenv('CALC_PORT', '8889')

print(f"coucou port {port}")

# Vérifier que c'est un entier
try:
    port = int(port)
except ValueError:
    raise ValueError("La variable d'environnement CALC_PORT doit être un entier.")

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('0.0.0.0', port))
sock.listen(1)

print(f"En attente de connexion sur le port {port}...")
try:
    client, client_addr = sock.accept()
    print(f"Connexion établie avec {client_addr}")
except Exception as e:
    print(f"Erreur lors de l'acceptation de la connexion : {e}")
    sock.close()
    exit(1)

while True:
    try:
        header = client.recv(4)
    
        if not header:
            print("Connexion fermée par le client.")
            break

        print(f"Header reçu : {header}")
        msg_len = int.from_bytes(header, byteorder='big')
        print(f"Lecture des {msg_len} prochains octets")

        chunks = []
        bytes_received = 0
        while bytes_received < msg_len:
            chunk = client.recv(min(msg_len - bytes_received, 1024))
            if not chunk:
                raise RuntimeError('Invalid chunk received bro')
            chunks.append(chunk)
            bytes_received += len(chunk)

        message_received = b"".join(chunks).decode('utf-8')
        print(f"Données reçues du client : {message_received}")

        try:
            res = eval(message_received)
            print(f"res is {res}")
            client.send(str(res).encode())
        except Exception as e:
            client.send(f"Erreur: {str(e)}".encode())
    except Exception as e:
        print(f"Erreur lors de la réception des données : {e}")
        break

client.close()
sock.close()