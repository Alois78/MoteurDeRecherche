import os
import requests
from dotenv import load_dotenv

def recuperer_corpus():
    """Télécharge des articles depuis une API publique pour créer notre base de documents."""
    print("1. Téléchargement des données depuis l'API...")
    
    ma_cle = os.getenv("API_KEY_SECRETE")
    
    # On envoie la requête GET (sans besoin de clé API ici !)
    reponse = requests.get(url, headers=headers)

    reponse.raise_for_status() # Déclenche une erreur si le site ne répond pas
    donnees_json = reponse.json()

    documents = {}
    
    # On parcourt les articles reçus pour les ranger dans notre dictionnaire
    for article in donnees_json["posts"]:
        # On fusionne le titre et le contenu pour la recherche
        texte_complet = f"{article['title']} {article['body']}"
        documents[article["id"]] = texte_complet
        
    return documents

def creer_index_inverse(documents):
    """Crée le dictionnaire inversé (Mot -> Liste d'IDs des documents)."""
    print("2. Création de l'index inversé...")
    index = {}
    
    for doc_id, texte in documents.items():
        # Nettoyage très basique : on met en minuscules et on enlève la ponctuation simple
        texte_nettoye = texte.lower().replace(".", "").replace(",", "").replace("!", "")
        mots = texte_nettoye.split() # Transforme la phrase en liste de mots
        
        # On utilise set() pour ne garder chaque mot qu'une seule fois par document
        for mot in set(mots):
            if mot not in index:
                index[mot] = [] # Si le mot n'existe pas encore dans l'index, on crée sa liste
            index[mot].append(doc_id) # On ajoute l'ID du document à la liste de ce mot
            
    return index

def rechercher(requete, index, documents):
    """Cherche les documents qui contiennent TOUS les mots de la requête."""
    print(f"\n🔍 --- Recherche en cours pour : '{requete}' ---")
    
    # On nettoie la requête de la même manière que les documents
    mots_requete = requete.lower().split()
    
    # On récupère les listes de documents pour chaque mot
    # Si le mot n'est pas dans l'index, on renvoie un ensemble vide set()
    resultats_par_mot = [set(index.get(mot, [])) for mot in mots_requete]
    
    # Si la requête n'était pas vide, on cherche l'intersection de tous les ensembles
    if resultats_par_mot:
        documents_trouves = set.intersection(*resultats_par_mot)
    else:
        documents_trouves = set()

    # Affichage des résultats
    if not documents_trouves:
        print("❌Aucun document ne correspond à cette recherche.")
    else:
        print(f"{len(documents_trouves)} document(s) trouvé(s) :")
        for doc_id in documents_trouves:
            # On récupère les 80 premiers caractères pour faire un petit résumé
            extrait = documents[doc_id][:80] + "..." 
            print(f"   📄 [Doc n°{doc_id}] : {extrait}")

# ==========================================
# Exécution principale du programme
# ==========================================
if __name__ == "__main__":
    try:
        # Étape 1 & 2 : Préparation du moteur
        mon_corpus = recuperer_corpus()
        mon_index = creer_index_inverse(mon_corpus)
        
        print("\nLe moteur de recherche est prêt !")
        
        # Étape 3 : Tests (Attention, les textes de l'API sont en anglais)
        rechercher("english", mon_index, mon_corpus)
        rechercher("time", mon_index, mon_corpus)
        
        # Recherche avec plusieurs mots (intersection)
        rechercher("time life", mon_index, mon_corpus) 
        
        # Un mot qui n'existe sûrement pas dans le texte
        rechercher("ordinateur", mon_index, mon_corpus) 

    except requests.exceptions.RequestException as e:
        print(f"\nErreur de connexion réseau : {e}")
        print("Vérifie que le pare-feu du lycée ne bloque pas la connexion internet de Python.")
