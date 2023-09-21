from html import escape

from django.http import HttpResponse
from django.shortcuts import render, redirect

from tasks.models import Collection


# Create your views here.

def index(request):
    context = {"collections": Collection.objects.order_by("name")}
    # récuperation de toutes les collections créer on peut mettre all().
    # qui sera passer via le context
    return render(request, 'tasks/index.html', context=context)


def add_collection(request):
    # récupération de la collection depuis le formulaire
    # protection contre les attaques par injection XSS  en utilisant escape()
    collection_name = escape(request.POST.get("collection_name"))
    # création de la collection
    # verification des si l'object à été creer avec la methode get_or_create(object, created)
    collection,created = Collection.objects.get_or_create(name=collection_name)

    if not created:
        return HttpResponse("la collection existe déjà")

    return redirect("home")
