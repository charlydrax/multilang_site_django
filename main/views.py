from django.shortcuts import render
from django.utils.translation import gettext as _
#Tout charactere ou chaîne de charactère qui doit être traduit passera dans un gettext
# Create your views here.

def home(request):
    var = _("Welcome")
    return render(request, 'index.html', {'var': var})

"""
Etapes de translations
1 Définire les variables à traduires
commande: python manage.py makemessages -l laLangue
2 Donner leurs équivalences dans la langue à traduire
3 Compiler : python manage.py compilemessages
"""