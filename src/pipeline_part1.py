import sqlite3
import requests
import os
import matplotlib.pyplot as plt

DB_PATH = "data/projet.db"

def initialiser_bdd():
    """Crée la table SQLite si elle n'existe pas encore."""
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS donnees_internet (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT,
            taille TEXT,
            etat TEXT,
            longueur REAL
        )
    ''')
    conn.commit()
    conn.close()

def effacer_bdd():
    """Vide la table de la base de données."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM donnees_internet")
    conn.commit()
    conn.close()

def telecharger_donnees_json():
    """
    Télécharge des données JSON depuis Internet.
    Ici, on utilise une URL de test ou une simulation d'API publique contenant les attributs requis.
    """
    # Exemple d'URL mock ou API de test. 
    # Pour l'exemple, nous simulons le retour d'une API web (Format JSON attendu)
    # Dans ton projet, tu peux remplacer par une vraie URL d'API publique.
    url_mock = "https://jsonplaceholder.typicode.com/todos" 
    
    try:
        r = requests.get(url_mock, timeout=15)
        r.raise_for_status()
        
        # Simulation/Adaptation des objets JSON aux critères demandés (taille, nom, état, longueur)
        donnees_brutes = r.json()
        donnees_traitees = []
        
        for idx, item in enumerate(donnees_brutes[:15]): # On prend les 15 premiers éléments
            donnees_traitees.append({
                "nom": f"Fichier_{item['id']}",
                "taille": f"{ (item['id'] * 12) % 100 } KB",
                "etat": "Complété" if item['completed'] else "En cours",
                "longueur": float(len(item['title']) * 2)
            })
        return donnees_traitees
    except Exception as e:
        print(f"Erreur de téléchargement JSON : {e}")
        raise

def stocker_donnees(donnees):
    """
    Stocke les données dans SQLite.
    Gère la question de l'énoncé : 'Que feriez-vous si la base de données n'est pas vide ?'
    -> Solution adoptée : On alerte l'utilisateur ou on vide avant d'insérer, ou on ajoute à la suite.
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Vérification si la base est vide
    cursor.execute("SELECT COUNT(*) FROM donnees_internet")
    count = cursor.fetchone()[0]
    
    # Si elle n'est pas vide, on peut décider d'ajouter (Append) ou de lever une règle.
    # Ici, on insère les nouvelles données à la suite
    for d in donnees:
        cursor.execute('''
            INSERT INTO donnees_internet (nom, taille, etat, longueur)
            VALUES (?, ?, ?, ?)
        ''', (d['nom'], d['taille'], d['etat'], d['longueur']))
        
    conn.commit()
    conn.close()
    return count  # Renvoie le nombre d'éléments pré-existants pour l'affichage

def calculer_aggregation_sql():
    """Calcule la moyenne de la valeur 'longueur' en utilisant une requête SQL."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT AVG(longueur) FROM donnees_internet")
    resultat = cursor.fetchone()[0]
    conn.close()
    return round(resultat, 2) if resultat is not None else 0

def generer_graphique_bdd(chemin_sortie="data/graphique_bdd.png"):
    """Récupère les données de la BDD et génère un graphique Matplotlib."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT nom, longueur FROM donnees_internet LIMIT 10")
    lignes = cursor.fetchall()
    conn.close()
    
    if not lignes:
        return False
        
    noms = [l[0] for l in lignes]
    longueurs = [l[1] for l in lignes]
    
    plt.figure(figsize=(6, 3))
    plt.barh(noms, longueurs, color="#202124")
    plt.title("Longueur par élément (Données BDD)")
    plt.xlabel("Longueur")
    plt.tight_layout()
    plt.savefig(chemin_sortie)
    plt.close()
    return True