import json
from datetime import datetime

class Document:
    def __init__(self, titre, annee):
        self.titre = titre
        self.annee = annee

    def afficher(self):
        print(f"{self.titre} ({self.annee})")

    def est_recent(self):
        """Un document est récent s’il a moins de 5 ans."""
        return (datetime.now().year - self.annee) <= 5


class Livre(Document):
    def __init__(self, titre, annee, auteur):
        super().__init__(titre, annee)
        self.auteur = auteur

    def afficher(self):
        print(f"Livre: {self.titre} par {self.auteur} ({self.annee})")


class Magazine(Document):
    def __init__(self, titre, annee, numero):
        super().__init__(titre, annee)
        self.numero = numero

    def afficher(self):
        print(f"Magazine: {self.titre} No. {self.numero} ({self.annee})")


class Bibliotheque:
    def __init__(self):
        self.documents = []

    def ajouter(self, doc):
        self.documents.append(doc)

    def rechercher(self, titre):
        for doc in self.documents:
            if doc.titre.lower() == titre.lower():
                return doc
        return None

    def afficher_tous(self):
        for doc in self.documents:
            doc.afficher()

    def to_json(self):
        return json.dumps([doc.__dict__ for doc in self.documents], ensure_ascii=False, indent=4)


# Test
if __name__ == '__main__':
    biblio = Bibliotheque()
    biblio.ajouter(Livre("1984", 1949, "George Orwell"))
    biblio.ajouter(Magazine("Science & Vie", 2023, 456))
    biblio.ajouter(Livre("Le Petit Prince", 1943, "Antoine de Saint-Exupéry"))

    print("=== Affichage des documents ===")
    biblio.afficher_tous()

    print("\n=== Recherche ===")
    doc = biblio.rechercher("1984")
    if doc:
        doc.afficher()

    print("\n=== Vérification de la récence ===")
    for d in biblio.documents:
        print(f"{d.titre} est récent ? {d.est_recent()}")

    print("\n=== Sérialisation JSON ===")
    print(biblio.to_json())
