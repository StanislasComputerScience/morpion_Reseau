import socket
import threading

def recevoir_messages(sock):
    while True:
        try:
            message = sock.recv(4096).decode()
            if not message:
                print("Déconnecté du serveur.")
                break
            print(message)
        except:
            print("Erreur de réception.")
            break

def main():
    hote = input("Adresse IP du serveur : ")
    port = 12345

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((hote, port))
    print("Connecté au serveur.\n")

    # Thread pour recevoir les messages du serveur
    thread_reception = threading.Thread(target=recevoir_messages, args=(client,))
    thread_reception.daemon = True
    thread_reception.start()

    while True:
        try:
            coup = input()
            if coup.upper() == "QUIT":
                client.sendall("QUIT".encode())
                break
            client.sendall(coup.encode())
        except KeyboardInterrupt:
            print("\nDéconnexion...")
            client.sendall("QUIT".encode())
            break
        except:
            print("Erreur de communication.")
            break

    client.close()

if __name__ == "__main__":
    main()
