import random
from django.shortcuts import render
from .models import Mot



def index(request):
    mots = Mot.objects.all().order_by('mot_sar')
    return render(request, 'mots/index.html', {'mots': mots})

def galerie_view(request):
    mots = list(Mot.objects.all())  # Récupérer tous les mots
    random.shuffle(mots)  # Mélanger la liste des mots
    mots_aleatoires = mots[:3]  # Prendre les 3 premiers mots mélangés (vous pouvez ajuster ce nombre)
    return render(request, 'mots/index.html', {'mots': mots_aleatoires})
def apropos(request):
    return render(request,'mots/apropos.html', {'mots':Mot.objects.all()})


def entrainement(request):
    mot = random.choice(Mot.objects.all())
    correct = False
    if request.method == 'POST':
        reponse = request.POST.get('reponse', '').strip().lower()
        if reponse == mot.mot_fr.lower():
            correct = True
    return render(request, 'mots/entrainement.html', {'mot': mot, 'correct': correct})


def index(request):
    search_query = request.GET.get('search', '')

    if search_query:
        mots = Mot.objects.filter(mot_fr__icontains=search_query).order_by('mot_sar')
    else:
        mots = Mot.objects.all().order_by('mot_sar')

    return render(request, 'mots/index.html', {'mots': mots, 'search_query': search_query})


