from django.db import models
from django.db.models.enums import Choices
pilih_kualitas = (
        ('HD','hd'),
        ('SD','sd'),
        ('WEBRIP','webrip'),
    )
pilih_genre = (
    (None,''),
    ('Comedy ','comedy'),
    ('Action ','action'),
    ('Horror ','horror'),
    ('Thriller ','thriller'),
)
pilih_genre2 = (
    (None,''),
    ('| Comedy','comedy'),
    ('| Action','action'),
    ('| Horror','horror'),
    ('| Thriller','thriller'),
)


class Slider(models.Model):
    judul = models.CharField(max_length=255)
    poster = models.ImageField(upload_to='static')
    menit = models.CharField(max_length=20)
    kualitas = models.CharField(max_length=10,choices = pilih_kualitas, default='hd')
    genre1 = models.CharField(max_length=20,choices = pilih_genre, default= None,null=True)
    genre2 = models.CharField(max_length=20,choices = pilih_genre2, default= None,blank=True)
    def __str__(self):
        return "{}".format(self.judul)