from django.db import models
from django.contrib.auth.models import User

class Produit(models.Model):
    titre = models.CharField(max_length=200)
    code = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    creer_par = models.ForeignKey(User, on_delete=models.CASCADE)
    date_ajout = models.DateTimeField()

    def __str__(self):
        if len(self.titre) > 10:
            return self.titre[:10] + "..."
        return self.titre

    def pub_date_pretty(self):
        return self.date_ajout.strftime('%d/%m/%Y')