from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='perfil.png')

    def __str__(self):
        return f'Perfil de {self.user.username}'

class Post(models.Model):
    titulo = models.CharField('Título del Post',max_length = 150, unique = True)
    slug = models.CharField('Slug', max_length = 150, unique = True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    timestamp = models.DateTimeField(default=timezone.now)
    content = models.TextField()
    imagen = models.ImageField(null=True,blank=True,upload_to="images/")
    publicado = models.BooleanField('Publicado',default = True)
    categoria = models.CharField('Categoria', max_length = 150)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f'{self.user.username}: {self.content}'

class Comentario(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comentario')
    content = models.TextField()

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f'{self.user.username}: {self.content}'

class Categoria(models.Model):
    nombre = models.CharField(max_length = 150)

    def __str__(self):
        return self.nombre
