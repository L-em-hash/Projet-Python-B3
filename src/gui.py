import tkinter as tk
from tkinter import messagebox, ttk
import os
from PIL import Image, ImageTk

# Importation des fonctions de ton pipeline Partie 2 et Partie 1
from pipeline_part2 import main as lancer_partie_2
from pipeline_part1 import (
    initialiser_bdd,
    effacer_bdd,
    telecharger_donnees_json,
    stocker_donnees,
    calculer_aggregation_sql,
    generer_graphique_bdd
)

class ApplicationProjet(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Application de Bureau - Projet Python Avancé")
        self.geometry("700x650")
        self.configure(bg="#f0f2f5")

        # Initialisation automatique de la base de données au lancement
        initialiser_bdd()

        # Référence pour l'image du graphique Tkinter afin d'éviter le garbage collector
        self.image_graphique_tk = None

        # --- CRÉATION DU MENU (Demandé dans la Partie 1) ---
        menu_bar = tk.Menu(self)
        
        menu_actions = tk.Menu(menu_bar, tearoff=0)
        menu_actions.add_command(label="Obtenir les données Internet", command=self.action_recuperer_json)
        menu_actions.add_command(label="Effacer la base de données", command=self.action_effacer_bdd)
        menu_actions.add_separator()
        menu_actions.add_command(label="Quitter", command=self.quit)
        menu_bar.add_cascade(label="Menu Actions", menu=menu_actions)
        
        menu_options = tk.Menu(menu_bar, tearoff=0)
        menu_options.add_command(label="Thème Clair (Par défaut)", command=lambda: self.changer_theme("#f0f2f5", "#ffffff", "#333333"))
        menu_options.add_command(label="Thème Sombre", command=lambda: self.changer_theme("#202124", "#303134", "#ffffff"))
        menu_bar.add_cascade(label="Options d'affichage", menu=menu_options)
        
        self.config(menu=menu_bar)

        # --- TITRE PRINCIPAL ---
        self.lbl_titre = tk.Label(
            self, 
            text="PROJET PYTHON AVANCÉ", 
            font=("Arial", 16, "bold"), 
            bg="#f0f2f5", 
            fg="#333333"
        )
        self.lbl_titre.pack(pady=10)

        
        #  BLOC PARTIE 2 : RAPPORT WORD (PRIORITAIRE)
        
        self.frame_p2 = tk.LabelFrame(
            self, 
            text=" ⚙️ Partie 2 : Génération du Rapport Word ", 
            font=("Arial", 11, "bold"),
            padx=15, 
            pady=15,
            bg="#ffffff",
            fg="#1a73e8"
        )
        self.frame_p2.pack(fill="x", padx=15, pady=10)

        self.lbl_desc_p2 = tk.Label(
            self.frame_p2, 
            text="Télécharge un livre depuis Project Gutenberg, analyse les paragraphes,\n"
                 "traite les images avec le logo et génère le document Word automatisé.",
            justify="left", bg="#ffffff", fg="#333333", font=("Arial", 9, "italic")
        )
        self.lbl_desc_p2.pack(anchor="w", pady=(0, 10))

        btn_run_p2 = ttk.Button(
            self.frame_p2, 
            text="▶ Lancer le Pipeline de la Partie 2", 
            command=self.action_partie_2
        )
        btn_run_p2.pack(fill="x", ipady=5)

        
        #  BLOC PARTIE 1 : BASE DE DONNÉES & JSON
        
        self.frame_p1 = tk.LabelFrame(
            self, 
            text=" Partie 1 : Base de Données & Données JSON ", 
            font=("Arial", 11, "bold"),
            padx=15, 
            pady=15,
            bg="#ffffff",
            fg="#202124"
        )
        self.frame_p1.pack(fill="x", padx=15, pady=10)

        # Grille de boutons de la partie 1
        self.btn_grid_p1 = tk.Frame(self.frame_p1, bg="#ffffff")
        self.btn_grid_p1.pack(fill="x", pady=5)

        btn_download_json = ttk.Button(self.btn_grid_p1, text="1. Récupérer JSON", command=self.action_recuperer_json)
        btn_download_json.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

        btn_clear_db = ttk.Button(self.btn_grid_p1, text="2. Effacer BDD", command=self.action_effacer_bdd)
        btn_clear_db.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        btn_stats_sql = ttk.Button(self.btn_grid_p1, text="3. Agrégation SQL", command=self.action_aggregation_sql)
        btn_stats_sql.grid(row=1, column=0, padx=5, pady=5, sticky="ew")

        btn_graph_sql = ttk.Button(self.btn_grid_p1, text="4. Graphique BDD", command=self.action_afficher_graphique)
        btn_graph_sql.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        self.btn_grid_p1.grid_columnconfigure(0, weight=1)
        self.btn_grid_p1.grid_columnconfigure(1, weight=1)

        # Zone dynamique pour afficher le graphique ou les résultats au milieu de la fenêtre
        self.frame_affichage = tk.Frame(self.frame_p1, bg="#ffffff")
        self.frame_affichage.pack(fill="both", expand=True, pady=10)
        
        self.lbl_affichage_contenu = tk.Label(self.frame_affichage, bg="#ffffff", fg="#333333", font=("Arial", 10))
        self.lbl_affichage_contenu.pack()

        
        #  BARRE D'ÉTAT (OPTIONNELLE - BONUS)
        
        self.status_var = tk.StringVar(value="Application prête. Prête à exécuter la Partie 2.")
        self.status_bar = tk.Label(
            self, 
            textvariable=self.status_var, 
            bd=1, 
            relief=tk.SUNKEN, 
            anchor="w",
            font=("Arial", 9),
            bg="#e8eaed",
            fg="#5f6368",
            padx=10
        )
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

    # --- ACTIONS DE LA PARTIE 2 ---
    def action_partie_2(self):
        self.status_var.set("Exécution de la Partie 2 en cours (Téléchargement et calculs)...")
        self.update_idletasks()
        try:
            lancer_partie_2()
            self.status_var.set("Rapport Word généré avec succès dans 'rapport_livre.docx' !")
            messagebox.showinfo("Succès", "Le pipeline de la Partie 2 s'est déroulé sans erreur.\nLe fichier Word a été créé !")
        except Exception as e:
            self.status_var.set("Erreur lors de l'exécution de la Partie 2.")
            messagebox.showerror("Erreur", f"Le pipeline a rencontré un problème :\n{e}")

    # --- ACTIONS DE LA PARTIE 1 ---
    def action_recuperer_json(self):
        self.status_var.set("Téléchargement des données JSON depuis Internet...")
        self.update_idletasks()
        try:
            donnees = telecharger_donnees_json()
            # stocker_donnees renvoie le nombre d'éléments présents avant insertion
            elements_pre_existants = stocker_donnees(donnees)
            
            message_info = f"{len(donnees)} éléments insérés en base de données."
            if elements_pre_existants > 0:
                message_info += f"\nNote : La base n'était pas vide ({elements_pre_existants} éléments s'y trouvaient déjà), les données ont été ajoutées à la suite."
            
            self.status_var.set("Données JSON stockées avec succès.")
            messagebox.showinfo("Téléchargement", message_info)
        except Exception as e:
            self.status_var.set("Erreur lors du téléchargement ou du stockage JSON.")
            messagebox.showerror("Erreur", f"Impossible de récupérer les données :\n{e}")

    def action_effacer_bdd(self):
        try:
            effacer_bdd()
            self.status_var.set("Base de données vidée.")
            self.lbl_affichage_contenu.config(image="", text="La base de données est vide.")
            messagebox.showinfo("Base de données", "Le contenu de la base de données a été effacé avec succès.")
        except Exception as e:
            self.status_var.set("Erreur lors du nettoyage de la BDD.")
            messagebox.showerror("Erreur", f"Action impossible :\n{e}")

    def action_aggregation_sql(self):
        try:
            moyenne = calculer_aggregation_sql()
            text_resultat = f"Moyenne de la valeur 'longueur' (Calcul SQL) : {moyenne}"
            self.lbl_affichage_contenu.config(image="", text=text_resultat)
            self.status_var.set("Agrégation SQL calculée avec succès.")
        except Exception as e:
            self.status_var.set("Erreur lors du calcul de l'agrégation SQL.")
            messagebox.showerror("Erreur", f"Erreur SQL :\n{e}")

    def action_afficher_graphique(self):
        self.status_var.set("Génération du graphique depuis la base de données...")
        try:
            chemin_image = "data/graphique_bdd.png"
            succes = generer_graphique_bdd(chemin_image)
            
            if succes and os.path.exists(chemin_image):
                img = Image.open(chemin_image)
                self.image_graphique_tk = ImageTk.PhotoImage(img)
                self.lbl_affichage_contenu.config(image=self.image_graphique_tk, text="")
                self.status_var.set("Graphique de la base de données affiché à l'écran.")
            else:
                self.lbl_affichage_contenu.config(image="", text="Aucune donnée disponible pour créer le graphique.\nVeuillez d'abord récupérer le JSON.")
                self.status_var.set("Échec : Base de données vide.")
        except Exception as e:
            self.status_var.set("Erreur lors de l'affichage du graphique.")
            messagebox.showerror("Erreur", f"Erreur de rendu graphique :\n{e}")

    # --- OPTION SUPPLÉMENTAIRE : CHANGEMENT DYNAMIQUE DE THÈME ---
    def changer_theme(self, bg_color, frame_color, fg_color):
        self.configure(bg=bg_color)
        self.lbl_titre.config(bg=bg_color, fg=fg_color)
        self.frame_p2.config(bg=frame_color, fg="#1a73e8" if bg_color != "#202124" else "#8ab4f8")
        self.lbl_desc_p2.config(bg=frame_color, fg=fg_color)
        self.frame_p1.config(bg=frame_color, fg=fg_color)
        self.btn_grid_p1.config(bg=frame_color)
        self.frame_affichage.config(bg=frame_color)
        self.lbl_affichage_contenu.config(bg=frame_color, fg=fg_color)
        self.status_var.set("Thème mis à jour.")

if __name__ == "__main__":
    app = ApplicationProjet()
    app.mainloop()