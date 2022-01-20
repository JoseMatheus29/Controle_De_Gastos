from django.db import models

class Categorias(models.Model):
    nome = models.CharField(max_length=100)
    datacriacao = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.nome

class Transacao(models.Model):
    data = models.DateField()
    descricao = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    categoria = models.ForeignKey(Categorias, on_delete = models.CASCADE)
    observacoes = models.CharField(max_length=200, null=True, blank=True)
    class Meta:
        verbose_name_plural = 'Trasações' 

    def __str__(self):
        return self.descricao