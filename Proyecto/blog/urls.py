from django.urls import path
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from .views import edit_post, eliminar_post, detalle_post, comentario, edit_comentario, eliminar_comentario, ver_categoria

urlpatterns = [
    path('', views.feed, name="feed"),
    path('profile/', views.profile, name ="profile"),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('register/', views.register, name ="register"),
    path('login/', LoginView.as_view(template_name='social/login.html'), name="login"),
    path('logout/', LogoutView.as_view(template_name='social/logout.html'), name="logout"),
    path('post',views.post, name="post"),
    path('edit/<content>/', edit_post, name ='edit'),
    path('eliminar/<content>', eliminar_post, name='eliminar'),
    path('<slug:slug>/',detalle_post, name='detalle_post'),
    path('comentario/<slug>',views.comentario, name="comentario"),
    path('edit_comentario/<content>/', edit_comentario, name ='edit_comentario'),
    path('eliminar_comentario/<content>', eliminar_comentario, name='eliminar_comentario'),
    path('categoria/<str:cats>/',ver_categoria, name='categoria')
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)