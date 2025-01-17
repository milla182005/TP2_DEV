import socket
import sys

def send_message(message, host='localhost', port=8889):
    try:
        # Create a socket object
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect to the server
        client_socket.connect((host, port))

        # Encode the message and get its length
        message_encoded = message.encode('utf-8')
        message_length = len(message_encoded)

        # Send the length of the message as a 4-byte header
        client_socket.sendall(message_length.to_bytes(4, byteorder='big'))

        # Send the actual message
        client_socket.sendall(message_encoded)

        # Receive the response from the server
        response = client_socket.recv(1024)
        print(f"Réponse du serveur: {response.decode('utf-8')}")

    except Exception as e:
        print(f"Une erreur s'est produite lors de la communication avec le serveur: {e}")
    finally:
        # Close the socket
        client_socket.close()

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python client.py <message>")
        sys.exit(1)

    message = sys.argv[1]
    send_message(message)