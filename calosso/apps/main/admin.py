from django.db import models
from django.contrib import admin
from django.forms.models import ModelForm
from django.forms.widgets import Textarea

from models import Homepage, Galleria, Articolo
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
    formfield_overrides = widget_overrides

class GalleriaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(GalleriaForm, self).__init__(*args, **kwargs)
        self.fields['articolo_principale'].queryset = Articolo.objects.filter(galleria__exact=self.instance.pk)
class GalleriaAdmin(admin.ModelAdmin):
    form = GalleriaForm
    inlines = [ArticoloInline, ]
    formfield_overrides = widget_overrides

class GalleriaInline(admin.TabularInline):
    model = Galleria
    formfield_overrides = widget_overrides
    
class HomepageAdmin(admin.ModelAdmin):
    formfield_overrides = widget_overrides
    inlines = [GalleriaInline, ]

admin.site.register(Homepage, HomepageAdmin)
admin.site.register(Galleria, GalleriaAdmin)
# admin.site.register(Articolo)
