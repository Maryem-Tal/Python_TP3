from abc import ABC, abstractmethod

class Paiement(ABC):
    def __init__(self, montant: float):
        if montant <= 0:
            raise ValueError("Le montant doit être positif")
        self._montant = montant

    @abstractmethod
    def payer(self):
        pass

class CarteBancaire(Paiement):
    def __init__(self, montant, numero, cvv):
        super().__init__(montant)
        self.numero = numero
        self.cvv = cvv

    def payer(self):
        return f"Paiement de {self._montant:.2f}€ par Carte Bancaire (numéro {self.numero[-4:]}) validé."

class PayPal(Paiement):
    def __init__(self, montant, email, token):
        super().__init__(montant)
        self.email = email
        self.token = token

    def payer(self):
        return f"Paiement de {self._montant:.2f}€ via PayPal ({self.email}) validé."

class Crypto(Paiement):
    def __init__(self, montant, wallet_id, reseau):
        super().__init__(montant)
        self.wallet_id = wallet_id
        self.reseau = reseau

    def payer(self):
        return f"Paiement de {self._montant:.2f}€ en crypto ({self.reseau}, wallet {self.wallet_id[:6]}...) validé."

def traiter_paiements(liste):
    for p in liste:
        print(p.payer())

if __name__ == "__main__":
    paiements = [
        CarteBancaire(100, "1234567890123456", "123"),
        CarteBancaire(50, "9876543210987654", "456"),
        PayPal(75, "user@example.com", "tok123"),
        PayPal(120, "client@test.com", "tok456"),
        Crypto(200, "walletABCDEF123456", "BTC"),
        Crypto(300, "walletXYZ987654321", "ETH")
    ]
    traiter_paiements(paiements)
