from django.db import models


# Create your models here.
class Contato_Model(models.Model):
    data = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    nome = models.CharField(max_length=300)
    email = models.CharField(max_length=500)
    telefone = models.CharField(max_length=20, null=True)
    texto = models.CharField(max_length=1000, null=True)
    visto = models.BooleanField(default=False)

    objects = models.Manager()

    def __str__(self) -> str:
        return super().__str__(self.nome)
