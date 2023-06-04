def espace():
    """Permet de simplement créer un espace"""
    return print()

def bienvenue():
    """Création d'un message d'accueil"""
    welcome: str = """ + TP - D33 (PGR) - MINI CASINO"""
    return print(welcome)

def séparateur(symbole: str = "-", nombre: int = 100):
    """fonction permettant de générer des symboles (tirets) pour séparer du contenu

    Args:
        symbole (str, optional): Le symbole utilisé. Par défaut "-".
        nombre (int, optional): La quantité de symbole répété. Par défaut 100.

    Returns:
        _type_: Retourne une chaîne de caractères.
    """
    symbole: str = symbole.strip()
    nombre: int = int(nombre)
    return print(f" + {symbole * nombre}")


# Gestion des scores (score.txt) - partie 1/2
def initialisation_scores(file_name="score.txt"):
    """Création d'une première méthode pour initialiser le fichier score.txt

    Args:
        file_name (str, optional): Nom du fichier par défaut score.txt

    Returns:
        dict: {username: score}
    """
    scores = {}
    try:
        with open(file_name, "r") as file:
            for line in file.readlines():
                username, score = line.strip().split(";")
                scores[username] = int(score)
    except FileNotFoundError:
        # Le fichier n'existe pas...
        # Création de celui-ci avec des valeurs par défaut:
        #   GRESSIER;999
        #   GUILLON;777
        default_content_file = "GRESSIER;999\nGUILLON;777\n"
        with open(file_name, "w") as file:
            file.write(default_content_file)
            scores = {
                "GRESSIER": 999,
                "GUILLON": 777
            }
    return scores

# Gestion des scores (score.txt) - partie 2/2
def nouveau_scores(username: str, score: int, file_name="score.txt"):
    """Création d'une seconde méthode pour ajouter à la suite un nouveau score.

    Args:
        username (str): Le nom de l'utilisateur
        score (int): Le score de l'utilisateur
        file_name (str, optional): Nom du fichier par défaut score.txt
    """
    # Chargement des scores existants
    scores = initialisation_scores(file_name)
    scores[username] = score

    with open(file_name, "w") as file:
        for username, score in scores.items():
            file.write(f"{username.upper()};{score}\n")
