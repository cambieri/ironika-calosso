# -*- coding: utf-8 -*-

from django.db import models

### GESTIONE CARICAMENTO E CANCELLAZIONE IMMAGINI ARTICOLI (inizio) ###
import os
from django.core.files.storage import FileSystemStorage
from django.conf import settings
class OverwriteFileStorage(FileSystemStorage):   
    def get_available_name(self, name):
        if self.exists(name):
            os.remove(os.path.join(settings.MEDIA_ROOT, name))
        return name
def get_miniatura_path(instance, filename):
    return 'img/{0}/piccole/{1}'.format(instance.galleria.pk, filename)
def get_immagine_path(instance, filename):
    return 'img/{0}/{1}'.format(instance.galleria.pk, filename)
from django.db.models.fields.files import FieldFile
from django.db.models.signals import pre_delete
def file_cleanup(sender, instance, *args, **kwargs):
    '''
        Deletes the file(s) associated with a model instance. The model
        is not saved after deletion of the file(s) since this is meant
        to be used with the pre_delete signal.
        Se vuote, cancella anche la directory contenitore e la sua parent.
    '''
    for field_name, _ in list(instance.__dict__.iteritems()):
        field = getattr(instance, field_name)
        if issubclass(field.__class__, FieldFile) and field.name:
            dir_path = os.path.join(settings.MEDIA_ROOT, os.path.dirname(field.name))
            field.delete(save=False)
            if os.path.isdir(dir_path) and not os.listdir(dir_path):
                parent_dir_path = os.path.dirname(dir_path)
                os.rmdir(dir_path)
                if os.path.isdir(parent_dir_path) and not os.listdir(parent_dir_path):
                    os.rmdir(parent_dir_path)
### GESTIONE CARICAMENTO E CANCELLAZIONE IMMAGINI ARTICOLI (fine) ###

class Homepage(models.Model):
    slogan = models.CharField('Slogan', max_length=50, blank=False)
    descrizione = models.CharField('Descrizione', max_length=300, blank=True)
    occhiello = models.CharField('Occhiello', max_length=50, blank=True)
    immagine = models.ImageField('Immagine', blank=False, upload_to='img/home', storage=OverwriteFileStorage())
#     galleria_principale = models.OneToOneField('Galleria')
    class Meta:
        verbose_name = "HOMEPAGE"
        verbose_name_plural = "Homepage"
    def __unicode__(self):
        return u"Gestione HOMEPAGE"

class Galleria(models.Model):
    POSIZIONE_SCELTE = (
                     (0,'Disabilitato'),
                     (1,'Galleria Principale'),
                     (2,'Riga 1 - SX'), (3,'Riga 1 - C'), (4,'Riga 1 - DX'),
                     (5,'Riga 2 - SX'), (6,'Riga 2 - C'), (7,'Riga 2 - DX'),
    )
    homepage = models.ForeignKey(Homepage, default=1, editable=False)
    menu = models.CharField('Voce di menù', max_length=50, blank=False)
    slogan = models.CharField('Slogan', max_length=50, blank=True)
    titolo = models.CharField('Titolo', max_length=30, blank=False)
    articolo_principale = models.OneToOneField('Articolo', on_delete=models.SET_NULL, blank=True, null=True, related_name='+') # nessuna backwards relation
    posizione = models.PositiveSmallIntegerField('Posizione in homepage', blank=False, default=0, choices=POSIZIONE_SCELTE)
    class Meta:
        verbose_name = "GALLERIA"
        verbose_name_plural = "Gallerie"
        ordering = ['pk']
    def __unicode__(self):
        return u'{0} - {1}'.format(self.posizione, self.menu)

class Articolo(models.Model):
    POSIZIONE_SCELTE = (
                     (0,'Disabilitato'),
                     (1,'Riga 1 - SX'), (2,'Riga 1 - C'), (3,'Riga 1 - DX'),
                     (4,'Riga 2 - SX'), (5,'Riga 2 - C'), (6,'Riga 2 - DX'),
                     (7,'Riga 3 - SX'), (8,'Riga 3 - C'), (9,'Riga 3 - DX'),
                     (10,'Riga 4 - SX'), (11,'Riga 4 - C'), (12,'Riga 4 - DX'),
                     (13,'Riga 5 - SX'), (14,'Riga 5 - C'), (15,'Riga 5 - DX'),
                     (16,'Riga 6 - SX'), (17,'Riga 6 - C'), (18,'Riga 6 - DX'),
    )
    galleria = models.ForeignKey(Galleria)
    miniatura = models.ImageField('Miniatura', blank=False, upload_to=get_miniatura_path, storage=OverwriteFileStorage())
    immagine = models.ImageField('Immagine', blank=False, upload_to=get_immagine_path, storage=OverwriteFileStorage())
    titolo = models.CharField('Titolo', max_length=80, blank=False)
    descrizione = models.TextField('Descrizione', max_length=400, blank=True)
    posizione = models.PositiveSmallIntegerField('Posizione in galleria', blank=False, default=0, choices=POSIZIONE_SCELTE)
    class Meta:
        verbose_name = "ARTICOLO"
        verbose_name_plural = "Articoli"
        ordering = ['posizione']
    def __unicode__(self):
        return u'{0} - {1}'.format(self.posizione, self.titolo)

pre_delete.connect(file_cleanup, sender=Articolo)

