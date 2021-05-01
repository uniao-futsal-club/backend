import random
from django.db import models


def user_directory_path(instance, filename):
    HASH = random.getrandbits(100)
    return f'{HASH}-{filename}'


class Asset(models.Model):
    file = models.FileField(
        upload_to=user_directory_path, blank=False, null=False)
    created_at = models.DateTimeField('Data de Entrada', auto_now_add=True)

    class Meta:
        verbose_name = "Arquivo"
        verbose_name_plural = "Arquivos"
