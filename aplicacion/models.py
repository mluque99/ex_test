from django.db import models

class Paciente(models.Model):
    # category = models.ForeignKey(Category, on_delete=models.CASCADE)
    nombreP = models.CharField(max_length=128)
    # url = models.URLField()
    # views = models.IntegerField(default=0)

    def __str__(self):
        return self.nombreP

class Medico(models.Model):
    nombreM = models.CharField(max_length=128)

    def __str__(self):
        return self.nombreM

class Receta(models.Model):
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)

    def __str__(self):
        return self.medico.nombreM + "-" + self.paciente.nombreP
