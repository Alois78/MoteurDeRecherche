import tkinter as tk
from tkinter import filedialog, messagebox
from collections import Counter

# Fonction d'analyse
def analyser():
    chemin = filedialog.askopenfilename(
        title="Choisir un fichier texte",
        filetypes=[("Fichiers texte", "*.txt")]
    )

    if not chemin:
        return

    try:
        with open(chemin, "r", encoding="utf-8") as fichier:
            texte = fichier.read().lower()

        # Garder uniquement les lettres
        lettres = [c for c in texte if c.isalpha()]

        # Compter les occurrences
        compteur = Counter(lettres)

        # Afficher le résultat
        zone_resultat.delete("1.0", tk.END)

        for lettre, nombre in sorted(compteur.items()):
            zone_resultat.insert(tk.END, f"{lettre} : {nombre}\n")

    except Exception as e:
        messagebox.showerror("Erreur", str(e))


# Fenêtre principale
fenetre = tk.Tk()
fenetre.title("Analyse Shakespeare")
fenetre.geometry("400x500")

# Titre
label = tk.Label(
    fenetre,
    text="Occurrences des lettres",
    font=("Arial", 16)
)
label.pack(pady=10)

# Bouton
bouton = tk.Button(
    fenetre,
    text="Choisir une pièce",
    command=analyser
)
bouton.pack(pady=10)

# Zone de texte
zone_resultat = tk.Text(fenetre, width=40, height=20)
zone_resultat.pack(padx=10, pady=10)

# Boucle principale
fenetre.mainloop()
