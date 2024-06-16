from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .forms import Contato_Form
from .models import Contato_Model


# Create your views here.
def home_page(request):
    context = {
        "title": "Home",
        "content": "Infinix Soluções Financeiras",
    }
    
    return render(request, "home/home_page.html", context)


def about_page(request):
    context = {"title": "Um pouco sobre nos", "content": "Nosso compromisso"}
    return render(request, "home/view.html", context)


def contact_page(request):
    contact_form = Contato_Form(request.POST or None)
    context = {
        "title": "Contato",
        "content": "Deixe sua sugestão ou critica",
        "form": contact_form,
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
        mesg = Contato_Model.objects.create(
            nome=contact_form.cleaned_data.get("nome_completo"),
            telefone = contact_form.cleaned_data.get("telefone"),
            email = contact_form.cleaned_data.get("email"),
            texto = contact_form.cleaned_data.get("mensagem "),
        )
        mesg.save()
        context = {
            "title": "Contato",
            "content": "Mensagem enviada com sucesso, logo entratremos em contato",
            
        }
        return render(request, "home/view.html", context)
          

    return render(request, "home/view.html", context)

