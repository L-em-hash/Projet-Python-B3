import unittest

from src.pipeline_part2 import (
    compter_mots_paragraphes,
    statistiques,
    extraire_metadonnees,
    extraire_premier_chapitre
)


class TestProjetPythonAvance(unittest.TestCase):

    def test_extraire_metadonnees(self):
        texte = """
Title: Mon Livre
Author: Victor Hugo

Contenu...
"""
        titre, auteur = extraire_metadonnees(texte)

        self.assertEqual(titre, "Mon Livre")
        self.assertEqual(auteur, "Victor Hugo")

    def test_compter_mots_paragraphes(self):
        chapitre = """
Bonjour tout le monde.

Voici un second paragraphe avec davantage de mots.

Petit paragraphe.
"""

        nb_mots, paragraphes = compter_mots_paragraphes(chapitre)

        self.assertEqual(len(paragraphes), 3)
        self.assertEqual(len(nb_mots), 3)

    def test_statistiques(self):
        paragraphes = [
            "bonjour " * 10,
            "test " * 20,
            "python " * 30
        ]

        nb_mots = [10, 20, 30]

        stats = statistiques(nb_mots, paragraphes)

        self.assertEqual(stats["nb_paragraphes"], 3)
        self.assertEqual(stats["total_mots"], 60)
        self.assertEqual(stats["min_mots"], 10)
        self.assertEqual(stats["max_mots"], 30)
        self.assertEqual(stats["moy_mots"], 20.0)

    def test_extraire_premier_chapitre(self):
        texte = """
Title: Test
Author: Auteur

CHAPTER I

Ceci est le premier chapitre.

CHAPTER II

Ceci est le deuxième chapitre.
"""

        chapitre = extraire_premier_chapitre(texte)

        self.assertIn("premier chapitre", chapitre)
        self.assertNotIn("deuxième chapitre", chapitre)


if __name__ == "__main__":
    unittest.main(verbosity=2)