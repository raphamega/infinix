from django import forms
from django.core.exceptions import ValidationError
from .models import Contato_Model


class Contato_Form(forms.Form):
    nome_completo = forms.CharField(
        error_messages={"required": "Obrigatório o preenchimento do nome"},
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Seu nome completo"}
        ),
    )
    telefone = forms.CharField(
        label="Celular",
        max_length=30,
        error_messages={"required": "É obrigatório o preenchimento do campo mensagem!"},
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "data-mask": "(00) 0 0000-0000",
                "class": "form-control",
                "placeholder": "Digite apenas Numeros",
            }
        ),
    )
    
    email = forms.EmailField(
        error_messages={"invalid": "Digite um email válido!"},
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "Digite seu email"}
        ),
    )
    mensagem = forms.CharField(
        error_messages={"required": "É obrigatório o preenchimento do campo mensagem!"},
        widget=forms.Textarea(
            attrs={"class": "form-control", "placeholder": "Digite sua mensagem"}
        ),
    )

    class Meta:
        model = Contato_Model
        fields = [
            "nome",
            "telefone",
            "email",
            "mensagem",
        ]
