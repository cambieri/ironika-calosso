from django.db import models

def get_miniatura_path(instance, filename):
    return 'img/{0}/piccole/{1}'.format(instance.galleria.titolo, filename)

def get_immagine_path(instance, filename):
    return 'img/{0}/{1}'.format(instance.galleria.titolo, filename)

class Homepage(models.Model):
    slogan = models.CharField('Slogan', max_length=50, blank=False)
    descrizione = models.CharField('Descrizione', max_length=300, blank=True)
    occhiello = models.CharField('Occhiello', max_length=50, blank=True)
    galleria_principale = models.OneToOneField('Galleria')
    class Meta:
        verbose_name = "HOMEPAGE"
        verbose_name_plural = "Gestione Homepage"
    def __unicode__(self):
        return "HOMEPAGE"

class Galleria(models.Model):
    slogan = models.CharField('Slogan', max_length=50, blank=True)
    titolo = models.CharField('Titolo', max_length=30, blank=False)
    articolo_principale = models.OneToOneField('Articolo', blank=True, null=True, related_name='+') # nessuna backwards relation
    class Meta:
        verbose_name = "GALLERIA"
        verbose_name_plural = "Gallerie"
        ordering = ['titolo']
    def __unicode__(self):
        return self.titolo

class Articolo(models.Model):
    POSIZIONE_SCELTE = (
                     (1,'Riga 1 - SX'), (2,'Riga 1 - C'), (3,'Riga 1 - DX'),
                     (4,'Riga 2 - SX'), (5,'Riga 2 - C'), (6,'Riga 2 - DX'),
                     (7,'Riga 3 - SX'), (8,'Riga 3 - C'), (9,'Riga 3 - DX'),
                     (10,'Riga 4 - SX'), (11,'Riga 4 - C'), (12,'Riga 4 - DX'),
                     (13,'Riga 5 - SX'), (14,'Riga 5 - C'), (15,'Riga 5 - DX'),
    )
    galleria = models.ForeignKey(Galleria)
    miniatura = models.ImageField('Miniatura', blank=False, upload_to=get_miniatura_path)
    immagine = models.ImageField('Immagine', blank=False, upload_to=get_immagine_path)
    titolo = models.CharField('Titolo', max_length=80, blank=False)
    descrizione = models.TextField('Descrizione', max_length=400, blank=True)
    posizione = models.PositiveSmallIntegerField('Posizione in galleria', blank=False, choices=POSIZIONE_SCELTE)
    class Meta:
        verbose_name = "ARTICOLO"
        verbose_name_plural = "Articoli"
        ordering = ['titolo']
    def __unicode__(self):
        return self.titolo
