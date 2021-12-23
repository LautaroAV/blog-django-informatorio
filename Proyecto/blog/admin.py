from django.contrib import admin
from .models import Post, profile,Comentario, Categoria


# Register your models here.
admin.site.register(profile)
admin.site.register(Post)
admin.site.register(Comentario)
admin.site.register(Categoria)
