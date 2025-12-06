from django.db import models


class System(models.Model):
    name = models.CharField(max_length=255)
    version = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    maintenance_mode = models.BooleanField(default=False)
    #TODO: No futuro, criar a logica de atualização automatica a cada pr da dev para a main, ou seja a cada versão

    def __str__(self):
        return f"{self.name} (v{self.version})"
