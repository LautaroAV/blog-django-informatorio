from django.db.models.fields import SlugField
from django.shortcuts import get_object_or_404, render, redirect
from .models import *
from .forms import ComentarioForm, PostForm, UserRegisterForm
from django.contrib import messages
from django.contrib.auth.models import User


def feed(request):
    posts = Post.objects.all()
    context = {'posts':posts}

    return render(request, 'social/feed.html', context)

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'El usuario {username} ha sido creado correctamente')
            return redirect('feed')
    else:
        form = UserRegisterForm()


    context = { 'form': form}
    return render(request, 'social/register.html', context)

def post(request):
    current_user = get_object_or_404(User, pk=request.user.pk)
    if request.method == "POST":
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
            messages.success(request, 'Publicación creada')
            return redirect('feed')
    else:
        form = PostForm()
    return render(request, 'social/post.html', {'form': form})

def profile(request, username=None):
    current_user = request.user
    if username and username != current_user.username:
        user = User.objects.get(username=username)
        posts = user.posts.all()
    else:
        posts = current_user.posts.all()
        user = current_user
    return render(request, 'social/profile.html', {'user':user, 'posts':posts})

def edit_post(request,content):
    post = get_object_or_404(Post,content=content)
    
    contexto = {
        'form':PostForm(instance=post)
    }
    
    if request.method=='POST':
        formulario = PostForm(data=request.POST, instance=post)
        if formulario.is_valid():
            formulario.save()
            return redirect('feed')
        contexto['form'] = formulario

    return render(request,'social/edit.html', contexto)

def eliminar_post(request,content):
    post = get_object_or_404(Post,content=content)
    post.delete()
    return redirect('feed')

def detalle_post(request,slug):
    post = get_object_or_404(Post,slug=slug)
    post = Post.objects.get(
        slug = slug
    )
    
    contexto = {'detalle_post':post,           
            }

    return render(request,'social/detalle_post.html',contexto)

def comentario(request,slug):
    post = get_object_or_404(Post, slug=slug)
    current_user = get_object_or_404(User, pk=request.user.pk)
    if request.method == "POST":
        form = ComentarioForm(request.POST)
        if form.is_valid():
            com = form.save(commit=False)
            com.user = current_user
            com.post = post
            com.save()
            messages.success(request, 'Comentario publicado')
            return redirect('feed')
    else:
        form = ComentarioForm()
        return render(request, 'social/comentario.html', {'form': form})

def edit_comentario(request,content):
    comentario = get_object_or_404(Comentario,content=content)
    
    contexto = {
        'form':ComentarioForm(instance=comentario)
    }
    
    if request.method=='POST':
        formulario = ComentarioForm(data=request.POST, instance=comentario)
        if formulario.is_valid():
            formulario.save()
            return redirect('feed')
        contexto['form'] = formulario

    return render(request,'social/edit.html', contexto)

def eliminar_comentario(request,content):
    comentario = get_object_or_404(Comentario,content=content)
    comentario.delete()
    return redirect('feed')