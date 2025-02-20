from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegistroForm

def registrar(request):
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect("menu")  # Redireciona para a tela de Menu após o registro
    else:
        form = RegistroForm()
    return render(request, "autenticacao/registrar.html", {"form": form})

from django.contrib.auth import authenticate, login
from django.contrib import messages

def logar(request):
    if request.method == "POST":
        email = request.POST.get("email")
        senha = request.POST.get("senha")
        usuario = authenticate(request, username=email, password=senha)

        if usuario is not None:
            login(request, usuario)
            return redirect("menu")
        else:
            messages.error(request, "E-mail ou senha inválidos.")

    return render(request, "autenticacao/login.html")

from django.contrib.auth.decorators import login_required

@login_required
def menu(request):
    return render(request, "autenticacao/menu.html")

from django.contrib.auth import logout
from django.shortcuts import redirect

def deslogar(request):
    logout(request)
    return redirect("login")
