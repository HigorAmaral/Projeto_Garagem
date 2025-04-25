from django.db import models

class Cor(models.Model):
    nome = models.CharField(max_length=80)
    marca = models.ForeignKey('Marca', related_name='cores')
    categorita = models.ForeignKey('Categoria', related_name='cores')
    
    def __str__(self):
        return f"({self.id}) Marca {self.marca.title()} {self.modelo.toUpperCase()}"