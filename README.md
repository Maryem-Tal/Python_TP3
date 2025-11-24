# TP2 — Encapsulation et Composition en Python

Ce projet regroupe deux exercices pratiques illustrant les principes fondamentaux de la programmation orientée objet en Python : **l'encapsulation** et **la composition**.

---

## 🧩 Objectifs pédagogiques

- Appliquer les principes d'encapsulation : attributs protégés et privés, propriétés, validation des données.
- Mettre en œuvre la composition entre classes : relation de type « a un » ou « utilise ».
- Structurer un projet Python avec des fichiers séparés pour les classes et les tests.
- Préparer un code clair, réutilisable et prêt pour une présentation académique ou un portfolio.

---

## 📁 Structure du projet
Python_TP2/ ├── EX1_banque.py # Classe CompteBancaire avec encapsulation ├── EX1_main.py # Programme principal pour EX1 ├── EX2.py # Classes CompteBancaire et Client (composition) ├── EX2_test.py # Programme principal pour EX2 └── pycache/ # Dossier généré automatiquement par Python

---

## 🧪 EX1 — Encapsulation

### Classe : `CompteBancaire`
- Attributs :
  - `_titulaire` (protégé)
  - `__solde` (privé)
- Méthodes :
  - `deposer(montant)`
  - `retirer(montant)`
  - `solde` (propriété en lecture seule)
  - `__str__()` pour affichage

### Exemple d’utilisation (`EX1_main.py`)
```python
from EX1_banque import CompteBancaire

compte = CompteBancaire("Ali", 1000)
compte.deposer(200)
compte.retirer(150)
print(compte)
print("Solde accessible (lecture) :", compte.solde)

try:
    compte.solde = 500  # Provoque une erreur
except AttributeError as e:
    print("Erreur :", e)
EX2 — Composition
Classes :
CompteBancaire : gère le solde et les opérations

Client : possède un compte bancaire

Exemple d’utilisation (EX2_test.py)
from EX2 import Client

cli = Client("Yassir")
cli.compte.deposer(300)
cli.compte.retirer(50)
cli.afficher()
👩‍💻Auteur
Maryem Talbi Étudiante en informatique appliquée — spécialité cybersécurité Université Cadi Ayyad, Marrakech
