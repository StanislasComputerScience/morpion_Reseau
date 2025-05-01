# Morpion en Réseau

Un jeu de **Morpion** (ou Tic-Tac-Toe) en réseau, permettant à deux joueurs de s'affronter sur une grille 3x3 via une connexion TCP. Chaque joueur peut choisir son symbole (X ou O) et jouer tour à tour sur un serveur.

## 🛠️ Fonctionnalités

- Jeu en temps réel pour deux joueurs.
- Serveur TCP gérant les connexions et la synchronisation du jeu.
- Interface en ligne de commande avec affichage de la grille après chaque coup.
- Détection de victoire ou de match nul.(A venir ...)

## 🚀 Prérequis

Avant de commencer, assurez-vous que vous avez installé les dépendances suivantes :

- **Python 3** 

## 🧑‍💻 Installation

1. Clonez le dépôt sur votre machine locale :
    ```bash
    git clone https://github.com/StanislasComputerScience/morpion_Reseau.git
    ```

2. Allez dans le répertoire du projet :
    ```bash
    cd morpion_reseau
    ```

3. Exécutez le serveur :
    ```bash
    python3 serveur.py
    ```

4. Exécutez le client :
    ```bash
    python3 client.py
    ```

5. Suivez les instructions dans le terminal pour jouer au jeu !

## 🎮 Comment jouer

1. Le premier joueur (X) démarre la partie en se connectant au serveur.
2. Le deuxième joueur (O) rejoint en entrant l'adresse IP du serveur.
3. Les joueurs jouent à tour de rôle en indiquant leur coup sous la forme `A1`, `B2`, etc.
4. Le jeu se termine lorsqu'un joueur gagne ou si la grille est remplie (match nul).

## 🤖 Fonctionnalités à venir

- Amélioration de l'interface graphique.
- Mode de jeu contre l'ordinateur.
- Historique des scores et des parties.

## 📄 Licence

Ce projet est sous licence MIT - voir le fichier [LICENSE](LICENSE) pour plus de détails.

## 📞 Contact

Si vous avez des questions ou des suggestions, n'hésitez pas à ouvrir une issue sur ce dépôt ou à me contacter à [remilabonne@yahoo].

