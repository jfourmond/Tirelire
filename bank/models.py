from django.db import models


class MoneyType(models.TextChoices):
    COIN = "coin"
    BANK_NOTE = "bank_note"


class Bank(models.Model):
    """
    Modèle représentant une "tirelire"
    La base de données contiendra le statut de la tirelire. Seule une tirelire intacte peut être utilisée.
        - broken : valeur booléenne indiquant si une tirelire est cassée et inutilisable, ou intact
        - added : date d'ajout
        - updated : date de mise à jour
    """
    broken = models.BooleanField(default=False, blank=False, null=False)
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "bank"
        ordering = ["added"]


class BankContent(models.Model):
    """
    Modèle représentant le contenu d'une "tirelire"
        - bank_id : identifiant de la tirelire
        - type : type de l'élément ajouté à la "tirelire", billet (bank_note) ou pièce (coin)
        - added : date d'ajout
    """

    bank = models.ForeignKey(Bank, related_name="content", on_delete=models.CASCADE, null=False, blank=False)
    type = models.CharField(choices=MoneyType.choices, max_length=9, null=False, blank=False)
    amount = models.PositiveIntegerField()
    added = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "content"
        ordering = ["added"]
        