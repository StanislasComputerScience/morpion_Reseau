import socket
import threading

# Initialisation de la grille
grille = [["." for _ in range(3)] for _ in range(3)]
joueurs = []
tour = 0  # 0 ou 1

lock = threading.Lock()
jeu_termine = False

def afficher_grille():
    lignes = ["\nGRILLE :",
              "  1   2   3",
              "+---+---+---+"]
    for i, ligne in enumerate(grille):
        nom_ligne = chr(ord('A') + i)
        contenu = "| " + " | ".join(ligne) + " |"
        lignes.append(f"{nom_ligne}{contenu}")
        lignes.append("+---+---+---+")
    return "\n".join(lignes)

def verifier_victoire(symbole):
    for i in range(3):
        if all(grille[i][j] == symbole for j in range(3)) or all(grille[j][i] == symbole for j in range(3)):
            return True
    if grille[0][0] == grille[1][1] == grille[2][2] == symbole or grille[0][2] == grille[1][1] == grille[2][0] == symbole:
        return True
    return False

def match_nul():
    return all(cell != "." for row in grille for cell in row)

def envoyer_a_tous(message):
    for client, _ in joueurs:
        try:
            client.sendall(message.encode())
        except:
            continue

def gerer_client(client, joueur_id):
    global tour, jeu_termine
    symbole = "X" if joueur_id == 0 else "O"
    client.sendall(f"Votre symbole : {symbole}\n".encode())

    while not jeu_termine:
        with lock:
            if tour != joueur_id:
                continue

            client.sendall((afficher_grille() + f"\nC'est votre tour ({symbole})\nVotre coup (ex: A1) ou QUIT pour quitter : ").encode())

        try:
            coup = client.recv(1024).decode().strip().upper()
        except:
            break

        if coup == "QUIT":
            envoyer_a_tous(f"Le joueur {symbole} a quitté la partie.\n")
            jeu_termine = True
            break

        if len(coup) != 2 or coup[0] not in "ABC" or coup[1] not in "123":
            client.sendall("Entrée invalide. Format attendu : A1, B3...\n".encode())
            continue

        ligne = ord(coup[0]) - ord('A')
        colonne = int(coup[1]) - 1

        with lock:
            if grille[ligne][colonne] != ".":
                client.sendall("Cette case est déjà occupée. Réessayez.\n".encode())
                continue

            grille[ligne][colonne] = symbole

            if verifier_victoire(symbole):
                envoyer_a_tous(afficher_grille())
                envoyer_a_tous(f"\nLe joueur {symbole} a gagné !\n")
                jeu_termine = True
                break

            if match_nul():
                envoyer_a_tous(afficher_grille())
                envoyer_a_tous("\nMatch nul !\n")
                jeu_termine = True
                break

            tour = 1 - tour
            envoyer_a_tous(afficher_grille())

    client.close()

def main():
    hote = "0.0.0.0"
    port = 12345

    serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serveur.bind((hote, port))
    serveur.listen(2)

    print(f"Serveur en écoute sur {hote}:{port}...")

    while len(joueurs) < 2:
        client, _ = serveur.accept()
        joueurs.append((client, len(joueurs)))
        print(f"Joueur {len(joueurs)} connecté.")
        client.sendall("En attente d'un autre joueur...\n".encode())

    for client, i in joueurs:
        thread = threading.Thread(target=gerer_client, args=(client, i))
        thread.start()

if __name__ == "__main__":
    main()
