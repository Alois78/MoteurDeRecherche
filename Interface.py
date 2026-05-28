import tkinter as tk
from tkinter import messagebox
# On importe notre fonction depuis le fichier fonctions.py
from main import occurence, longueur_piece, obtenir_top_10

def action_bouton():
    # 1. Récupération des saisies de l'utilisateur
    mot = entree_mot.get().strip()
    piece = entree_piece.get().strip()
    
    if not mot or not piece:
        messagebox.showwarning("Champs vides", "Veuillez remplir le mot ET le nom de la pièce.")
        return

    # 2. Appel de la fonction logique et gestion des erreurs
    try:
        # On utilise la fonction importée
        resultat = occurence(mot, piece)
        longueur = longueur_piece(piece)
        
        # 3. Mise à jour de l'interface graphique
        label_resultat.config(text=f"Le mot '{mot}' apparaît {resultat} fois dans {piece}.", fg="black")
        label_longueur.config(text=f"La pièce comporte {longueur} mots.", fg="black")
        
    except FileNotFoundError as err:
        # Si la fonction lève une erreur FileNotFoundError, on l'attrape ici
        messagebox.showerror("Fichier introuvable", str(err))

def action_top_10():
    piece = entree_piece.get().strip()
    
    if not piece:
        messagebox.showwarning("Champ vide", "Veuillez entrer le nom de la pièce pour le Top 10.")
        return
    try:
        # Appel de notre nouvelle fonction
        top_10 = obtenir_top_10(piece)
        
        # Formatage du texte pour l'affichage (ex: "1. king : 145 fois")
        texte_affichage = f"--- Top 10 des mots dans {piece} ---\n"
        for i, (mot, freq) in enumerate(top_10, 1):
            texte_affichage += f"{i}. {mot} : {freq} fois\n"
            
        label_resultat.config(text=texte_affichage, fg="blue")
    except FileNotFoundError as err:
        messagebox.showerror("Fichier introuvable", str(err))


# --- CRÉATION DE L'INTERFACE (TKINTER) ---
fenetre = tk.Tk()
fenetre.title("Compteur de mots - Shakespeare")
fenetre.geometry("550x500")
fenetre.config(padx=20, pady=20)

# Champ : Pièce de théâtre
label_piece = tk.Label(fenetre, text="Nom de la pièce (ex: King Lear) :", font=("Arial", 10, "bold"))
label_piece.pack(anchor="w", pady=(0, 5))
entree_piece = tk.Entry(fenetre, font=("Arial", 11), width=40)
entree_piece.pack(fill="x", pady=(0, 15))

# Bouton pour le Top 10 (placé juste après la pièce)
bouton_top10 = tk.Button(fenetre, text="Afficher le Top 10 des mots", font=("Arial", 10), bg="#2196F3", fg="white", command=action_top_10)
bouton_top10.pack(fill="x", pady=(0, 20), ipady=3)

# Séparation visuelle
barre = tk.Frame(fenetre, height=2, bg="#CCCCCC")
barre.pack(fill="x", pady=10)

# Champ : Mot à chercher
label_mot = tk.Label(fenetre, text="Mot à rechercher :", font=("Arial", 10, "bold"))
label_mot.pack(anchor="w", pady=(0, 5))
entree_mot = tk.Entry(fenetre, font=("Arial", 11), width=40)
entree_mot.pack(fill="x", pady=(0, 20))

# Bouton (qui appelle la fonction locale action_bouton)
bouton_valider = tk.Button(fenetre, text="Compter les occurrences", font=("Arial", 11, "bold"), bg="#4CAF50", fg="white", command=action_bouton)
bouton_valider.pack(fill="x", ipady=5)

# Résultat
label_resultat = tk.Label(fenetre, text="", font=("Arial", 11, "italic"), pady=20)
label_resultat.pack()
label_longueur = tk.Label(fenetre, text="", font=("Arial", 11, "italic"), pady=20)
label_longueur.pack()


fenetre.mainloop()
