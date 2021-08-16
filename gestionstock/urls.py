from django.urls import path
from . import views

urlpatterns = [
    path('', views.gestionstock, name='gestionstock'),
    path('creer/', views.creer, name='creer'),
    path('supprimer/<int:produit_id>', views.supprimer, name='supprimer'),
    path('modifier/<int:produit_id>', views.modifier, name='modifier'),
    path('submit_modification/<int:produit_id>', views.submit_modification, name='submit_modification'),
    path('recherche_par_titre', views.re_titre, name='re_titre'),
    path('recherche_par_code', views.re_code, name='re_code'),
    path('recherche_par_zone', views.re_zone, name='re_zone'),
]