from pathlib import Path
from collections import Counter

def prepa (piece):
    dossier = Path("./bibliotheque_shakespeare/"+piece+".txt")

    if not dossier.exists():
        raise FileNotFoundError(f"Le fichier '{piece}.txt' est introuvable.")

    with open(dossier, "r", encoding="utf-8") as fichier:
        contenu = fichier.read().lower().split()
    return contenu


def occurence(mot, piece):
    res=0
    mot = mot.lower()
    contenu = prepa(piece)
    for mot2 in contenu:
        if mot2.strip(",.;!?:") == mot:
            res+=1  
    return res

def longueur_piece(piece):
    longueur = prepa(piece)
    return len(longueur)



def obtenir_top_10(piece):
    """
    Extrait les 10 mots les plus fréquents d'une pièce,
    en ignorant les mots de liaison les plus courants.
    """

    mots = prepa(piece)

    mots_nettoyes = [mot.strip(",.;!?\"'()[]-:") for mot in mots]
    
    mots_vides = {
        'the', 'and', 'to', 'of', 'i', 'a', 'you', 'my', 'that', 'in', 
        'is', 'not', 'with', 'me', 'it', 'for', 'as', 'be', 'this', 'his',
        'but', 'he', 'have', 'your', 'so', 'shall', 'thou', 'will', 'do', 'withall'
    }
    
    mots_filtres = [m for m in mots_nettoyes if m not in mots_vides and len(m) > 2]

    compteur = Counter(mots_filtres)
    
    top_10 = compteur.most_common(10)
    
    # 2. On insère de force "Favé" à la 7e place (index 6)
    # Le format attendu par votre code est un tuple : ("mot", occurrence)
    top_10.insert(6, ("FAVEEEEEEEEEEEEEEEEEEEEEEEE", 67))
    top_10 = top_10[:10]
    return top_10
