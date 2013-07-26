from django.db import models
from django.contrib import admin
from django.forms.models import ModelForm
from django.forms.widgets import Textarea

from models import Homepage, Galleria, Articolo, Varie
from admin_image_widget import AdminImageWidget

custom_charfield_widget = {'widget': Textarea(attrs={'cols':40, 'rows':2})}
custom_textfield_widget = {'widget': Textarea(attrs={'cols':80, 'rows':3})}
custom_image_widget = {'widget': AdminImageWidget}
widget_overrides = { 
                    models.CharField: custom_charfield_widget, 
                    models.TextField: custom_textfield_widget,
                    models.ImageField: custom_image_widget,
                    }

class ArticoloInline(admin.TabularInline):
    model = Articolo
    max_num = 18
    formfield_overrides = widget_overrides

class GalleriaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(GalleriaForm, self).__init__(*args, **kwargs)
        self.fields['articolo_principale'].queryset = Articolo.objects.filter(galleria__exact=self.instance.pk)
        self.exclude = ['homepage']
class GalleriaAdmin(admin.ModelAdmin):
    form = GalleriaForm
    fields = ['menu', 'posizione', 'articolo_principale', 'slogan', 'titolo']
    inlines = [ArticoloInline, ]
    formfield_overrides = widget_overrides
    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return ()
        return ('menu', )

class GalleriaInline(admin.TabularInline):
    model = Galleria
    form = GalleriaForm
    fields = ['posizione', 'articolo_principale', 'slogan', 'titolo']
    formfield_overrides = widget_overrides
    
class HomepageAdmin(admin.ModelAdmin):
    formfield_overrides = { models.CharField: {'widget': Textarea(attrs={'cols':60, 'rows':3})}, }
    inlines = [GalleriaInline, ]

class VarieAdmin(admin.ModelAdmin):
    formfield_overrides = { models.ImageField: custom_image_widget, }
    
admin.site.register(Homepage, HomepageAdmin)
admin.site.register(Galleria, GalleriaAdmin)
# admin.site.register(Articolo)
admin.site.register(Varie, VarieAdmin)
