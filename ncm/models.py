from django.db import models

# Create your models here.
class Ncm(models.Model):
    class Meta:
        verbose_name="NCM"
        verbose_name_plural="NCM"
    codigo = models.IntegerField()
    descricao = models.CharField(max_length=500)
    uf = models.CharField(max_length=2, null=True, blank=True)    
    nacionalFederal = models.FloatField(null=True, blank=True)
    importadosFederal = models.FloatField(null=True, blank=True)
    estadual = models.FloatField(null=True, blank=True)
    municipal = models.FloatField(null=True, blank=True)
    inicio = models.DateField(null=True, blank=True)
    fim = models.DateField(null=True, blank=True)
    atualizacao = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return "Descrição: {}, UF: {}".format(self.descricao,self.uf)





