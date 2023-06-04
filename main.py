#!/usr/bin/env python3

from user import User
from utils.check_files import initialisation_scores, nouveau_scores

# PROGRAMME PRINCIPAL
def main():
    scores = initialisation_scores()
    
    welcome: str = """\n + TP - D33 (PGR) - MINI CASINO"""
    tirets: str = "-"
    
    print(welcome)
    print(f" + {tirets * 100}")
    
    username = input(" + Pour commencer, veuillez saisir votre pseudonyme utilisé pour pouvoir jouer: ").upper()

    if username in scores:
        player = User(username, scores[username])
    else:
        player = User(username)
        scores[username] = player._solde
        nouveau_scores(username, player._solde)

    # Message d'accueil
    print(f"\nBienvenue {player._name}, votre solde est de {player._solde}€\n")

# INITIALISATION DU PROGRAMME PRINCIPAL
try:
    main()
except UnboundLocalError:
    scores = initialisation_scores()
    main()

# Zone de test
initialisation_scores()
