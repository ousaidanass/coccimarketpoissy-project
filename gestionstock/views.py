from django.shortcuts import render, redirect, get_object_or_404
from .models import Produit
from django.utils import timezone
from django.contrib.auth.decorators import login_required


@login_required(login_url='/accounts/login')
def gestionstock(request):
    produits = Produit.objects
    return render(request, 'gestionstock.html', {'produits': produits})


@login_required(login_url='/accounts/login')
def creer(request):
    if request.method == 'POST':
        if request.POST['titre'] and request.POST['code'] and request.POST['zone']:
            produit = Produit()
            produit.titre = request.POST['titre']
            produit.code = request.POST['code']
            produit.zone = request.POST['zone']
            produit.date_ajout = timezone.datetime.now()
            produit.creer_par = request.user
            produit.save()
            return redirect('/produit/')
        else:
            return render(request, 'creer.html', {'error': 'Remplissez tous les champs'})
    else:
        return render(request, 'creer.html')


@login_required(login_url='/accounts/login')
def supprimer(request, produit_id):
    if request.method == 'POST':
            produit = get_object_or_404(Produit, pk=produit_id)
            produit.delete()
            return redirect('/produit/')

@login_required(login_url='/accounts/login')
def modifier(request, produit_id):
    if request.method == 'POST':
            produit = get_object_or_404(Produit, pk=produit_id)
            return render(request, 'modifier.html', {'produit': produit})

@login_required(login_url='/accounts/login')
def submit_modification(request, produit_id):
    if request.method == 'POST':
            produits = Produit.objects
            produit = get_object_or_404(Produit, pk=produit_id)
            produit.titre = request.POST["titre"]
            produit.code = request.POST["code"]
            produit.zone = request.POST["zone"]
            produit.save()
            return render(request, 'gestionstock.html', {'produits': produits})


@login_required(login_url='/accounts/login')
def re_titre(request):
    if request.method == 'POST':
        dict_rechercher = {'produits_re': []}
        produits = Produit.objects.all()
        titre_rechercher = request.POST['re_par_titre']
        for re_mot in titre_rechercher.split():
            for produit in produits.iterator():
                for ti_mot in produit.titre.split():
                    if re_mot == ti_mot:
                        dict_rechercher['produits_re'].append(produit)
        return render(request, 'gestionstock.html', dict_rechercher)

@login_required(login_url='/accounts/login')
def re_code(request):
    if request.method == 'POST':
        dict_rechercher = {'produits_re': []}
        code_rechercher = request.POST['re_par_code']
        produits = Produit.objects.all()
        for produit in produits.iterator():
            if code_rechercher == produit.code:
                dict_rechercher['produits_re'].append(produit)
        return render(request, 'gestionstock.html', dict_rechercher)

@login_required(login_url='/accounts/login')
def re_zone(request):
    if request.method == 'POST':
        dict_rechercher = {'produits_re': []}
        produits = Produit.objects.all()
        zone_rechercher = request.POST['zone']
        for produit in produits.iterator():
            if zone_rechercher == produit.zone:
                dict_rechercher['produits_re'].append(produit)
        return render(request, 'gestionstock.html', dict_rechercher)