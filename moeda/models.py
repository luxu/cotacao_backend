from django.db import models

from moeda.constantes import INITIALS, NAME


class Moeda(models.Model):
    initials = models.CharField(
        "Sigla da moeda",
        max_length=3,
        choices=INITIALS,
        null=True
    )
    name_coin = models.CharField(
        "Moeda",
        max_length=5,
        choices=NAME,
        null=True
    )
    data = models.DateField()
    value = models.CharField(
        "Valor",
        max_length=20
    )

    def __str__(self):
        return self.initials
