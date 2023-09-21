from django.db import models


# Create your models here.

class Collection(models.Model):
    name = models.CharField(max_length=60)
    slug = models.SlugField()


class Task(models.Model):
    # on_delete = models.CASCADE permet supprimer les elements associé à l'attribut pere vu que c'est une clé
    # étrangères
    description = models.CharField(max_length=300)
    Collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
