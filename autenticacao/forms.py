from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario
import re

class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)
    nome = forms.CharField(max_length=100)
    
    def clean_nome(self):
        nome = self.cleaned_data.get("nome")
        if not nome.replace(" ", "").isalpha():
            raise ValidationError("O nome deve conter apenas letras.")
        return nome

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if Usuario.objects.filter(email=email).exists():
            raise ValidationError("Este e-mail já está em uso.")
        return email

    def clean_password1(self):
        senha = self.cleaned_data.get("password1")
        if not re.search(r'[A-Z]', senha) or not re.search(r'\d', senha) or not re.search(r'\W', senha) or len(senha) < 8:
            raise ValidationError("A senha deve ter pelo menos 8 caracteres incluindo 1 letra maiúscula, 1 número e 1 caractere especial.")
        return senha

    class Meta:
        model = Usuario
        fields = ["nome", "email", "password1", "password2"]
