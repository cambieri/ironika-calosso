from django.template import loader
import sys
from django import http
from django.template.context import Context
from django.shortcuts import render, get_object_or_404

from models import Galleria
from calosso.apps.main.models import Homepage

def nondefault_500_error(request, template_name='500nondefault.html'):
    """
    500 error handler for debug.

    Templates: `500.html`
    Context: sys.exc_info() results
     """
    t = loader.get_template(template_name) # You need to create a 500.html template.
    ltype,lvalue,ltraceback = sys.exc_info()
    sys.exc_clear() #for fun, and to point out I only -think- this hasn't happened at 
                    #this point in the process already
    return http.HttpResponseServerError(t.render(Context({'type':ltype,'value':lvalue,'traceback':ltraceback})))

def index(request):
    homepage = Homepage.objects.all()[:1].get()
    try:
        principale = Galleria.objects.get(posizione__exact = 1);
    except:
        principale = Galleria()
    try:
        gallerie = Galleria.objects.filter(posizione__gt = 1).order_by('posizione');
    except:
        gallerie = Galleria()
    args = {
            'sezione': '',
            'homepage': homepage,
            'principale': principale,
            'gallerie': gallerie,
            }
    return render(request, 'index.html', args)
    
def gallery(request, gallery_id):
    galleria = get_object_or_404(Galleria, pk = gallery_id)
    try:
        principale = galleria.articolo_principale.posizione
    except:
        principale = 0
    args = {'sezione': galleria.menu, 'galleria': galleria, 'principale': principale}
    return render(request, 'gallery.html', args)
