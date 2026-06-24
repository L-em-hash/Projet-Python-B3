import unittest
import os
import sqlite3
from src.pipeline_part1 import initialiser_bdd, effacer_bdd, stocker_donnees, calculer_aggregation_sql

class TestPartie1(unittest.TestCase):
    def setUp(self):
        initialiser_bdd()

    def test_insertion_et_aggregation(self):
        effacer_bdd()
        donnees_test = [
            {"nom": "Test1", "taille": "10KB", "etat": "OK", "longueur": 50.0},
            {"nom": "Test2", "taille": "20KB", "etat": "OK", "longueur": 150.0}
        ]
        stocker_donnees(donnees_test)
        
        moyenne = calculer_aggregation_sql()
        self.assertEqual(moyenne, 100.0)

if __name__ == "__main__":
    unittest.main()