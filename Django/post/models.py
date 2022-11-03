from tabnanny import verbose
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class post(models.Model):
    title = models.CharField(max_length = 120, verbose_name = 'Başlık')
    content = models.TextField(verbose_name = 'İçerik')
    publishing_date = models.DateField(verbose_name = 'Yayımlama Tarihi')

    def __str__(self):
        return self.title