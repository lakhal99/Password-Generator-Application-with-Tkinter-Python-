import tkinter as tk
from tkinter import ttk, messagebox
import random
import string
import tkinter.font as tkFont  # Importation pour changer la police

# Fonction pour générer un mot de passe
def generer_mot_de_passe():
    try:
        longueur = int(entry_longueur.get())
        caracteres = string.ascii_lowercase  # Lettres minuscules par défaut

        if var_majuscules.get():
            caracteres += string.ascii_uppercase
        if var_chiffres.get():
            caracteres += string.digits
        if var_speciaux.get():
            caracteres += string.punctuation

        if longueur < 1:
            raise ValueError("Longueur invalide")

        mot_de_passe = ''.join(random.choice(caracteres) for _ in range(longueur))

        # Mise à jour de la liste avec le mot de passe généré
        index = liste_mots_de_passe.size() + 1  # Numéro à afficher
        liste_mots_de_passe.insert(tk.END, f"{index}. {mot_de_passe}")

        # Ajouter le mot de passe à l'historique
        historique_index = historique_mots_de_passe.size() + 1
        historique_mots_de_passe.insert(tk.END, f"{historique_index}. {mot_de_passe}")

    except ValueError:
        messagebox.showerror("Erreur", "Veuillez entrer une longueur valide.")

# Fonction pour effacer l'historique
def effacer_historique():
    # Effacer uniquement l'historique des mots de passe
    historique_mots_de_passe.delete(0, tk.END)
    messagebox.showinfo("Info", "Historique effacé.")

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Générateur de mots de passe")
fenetre.geometry("600x450")
fenetre.resizable(False, False)

# Configuration de la police en gras
bold_font = tkFont.Font(family="Helvetica", size=10, weight="bold")

# Configuration des mots de passe
cadre_config = tk.LabelFrame(fenetre, text="Configuration du mot de passe", padx=10, pady=10, font=bold_font)
cadre_config.place(x=20, y=20, width=300, height=150)

# Longueur du mot de passe
tk.Label(cadre_config, text="Longueur du mot de passe :").grid(row=0, column=0, sticky="w", pady=10)
entry_longueur = tk.Entry(cadre_config, width=10)
entry_longueur.grid(row=0, column=1, pady=5)

# Complexité
tk.Label(cadre_config, text="Complexité :").grid(row=1, column=0, sticky="w")
combo_complexite = ttk.Combobox(cadre_config, values=["Faible", "Moyenne", "Élevée"], state="readonly", width=12)
combo_complexite.grid(row=1, column=1, pady=5)
combo_complexite.set("Faible")

# Options
cadre_options = tk.LabelFrame(fenetre, text="Options :", font=bold_font)
cadre_options.place(x=20, y=200, width=300, height=100)

var_majuscules = tk.BooleanVar()
var_chiffres = tk.BooleanVar()
var_speciaux = tk.BooleanVar()

tk.Checkbutton(cadre_options, text="Inclure des majuscules", variable=var_majuscules).pack(anchor="w")
tk.Checkbutton(cadre_options, text="Inclure des chiffres", variable=var_chiffres).pack(anchor="w")
tk.Checkbutton(cadre_options, text="Inclure des caractères spéciaux", variable=var_speciaux).pack(anchor="w")

# Bouton "Générer"
bouton_generer = tk.Button(fenetre, text="Générer", width=20, command=generer_mot_de_passe)
bouton_generer.place(x=100, y=300)

# Mots de passe générés
tk.Label(fenetre, text="Mots de passe générés", font=bold_font).place(x=350, y=20)  # Décalé à droite
liste_mots_de_passe = tk.Listbox(fenetre, height=6, width=25)
liste_mots_de_passe.place(x=350, y=50)  # Décalé à droite

# Historique des mots de passe
tk.Label(fenetre, text="Historique des mots de passe", font=bold_font).place(x=350, y=200)  # Décalé à droite
historique_frame = tk.Frame(fenetre)
historique_frame.place(x=350, y=230)  # Décalé à droite

scrollbar = tk.Scrollbar(historique_frame)
scrollbar.pack(side="right", fill="y")

historique_mots_de_passe = tk.Listbox(historique_frame, height=5, width=30, yscrollcommand=scrollbar.set)
historique_mots_de_passe.pack(side="left")
scrollbar.config(command=historique_mots_de_passe.yview)

# Bouton "Effacer l'historique"
bouton_effacer = tk.Button(fenetre, text="Effacer l'historique", command=effacer_historique)
bouton_effacer.place(x=370, y=330)

# Conseils
tk.Label(fenetre, text="Conseils :", font=bold_font).place(x=20, y=360)
conseils_frame = tk.Frame(fenetre)
conseils_frame.place(x=20, y=380, width=560, height=60)

conseils_listbox = tk.Listbox(conseils_frame, height=3, width=72)
conseils_listbox.pack(side="left", fill="both")

# Ajout des conseils
conseils = [
    "- Utilisez des mots de passe longs.",
    "- Combinez lettres, chiffres et symboles.",
    "- Ne réutilisez pas vos mots de passe."
]
for conseil in conseils:
    conseils_listbox.insert(tk.END, conseil)

# Lancement de l'application Tkinter
fenetre.mainloop()
