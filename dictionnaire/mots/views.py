
import random
from django.shortcuts import render
from .models import Mot

def index(request):
    mots = Mot.objects.all().order_by('mot_sar')
    return render(request, 'mots/index.html', {'mots': mots})

def entrainement(request):
    mot = random.choice(Mot.objects.all())
    correct = False
    if request.method == 'POST':
        reponse = request.POST.get('reponse', '').strip().lower()
        if reponse == mot.mot_fr.lower():
            correct = True
    return render(request, 'mots/entrainement.html', {'mot': mot, 'correct': correct})