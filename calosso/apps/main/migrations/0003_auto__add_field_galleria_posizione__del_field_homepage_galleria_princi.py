# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Galleria.posizione'
        db.add_column(u'main_galleria', 'posizione', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0), keep_default=False)

        # Deleting field 'Homepage.galleria_principale'
        db.delete_column(u'main_homepage', 'galleria_principale_id')


    def backwards(self, orm):
        
        # Deleting field 'Galleria.posizione'
        db.delete_column(u'main_galleria', 'posizione')

        # Adding field 'Homepage.galleria_principale'
        db.add_column(u'main_homepage', 'galleria_principale', self.gf('django.db.models.fields.related.OneToOneField')(default=1, to=orm['main.Galleria'], unique=True), keep_default=False)


    models = {
        u'main.articolo': {
            'Meta': {'ordering': "['titolo']", 'object_name': 'Articolo'},
            'descrizione': ('django.db.models.fields.TextField', [], {'max_length': '400', 'blank': 'True'}),
            'galleria': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.Galleria']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'immagine': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'miniatura': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'posizione': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'titolo': ('django.db.models.fields.CharField', [], {'max_length': '80'})
        },
        u'main.galleria': {
            'Meta': {'ordering': "['pk']", 'object_name': 'Galleria'},
            'articolo_principale': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "'+'", 'unique': 'True', 'null': 'True', 'to': u"orm['main.Articolo']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'posizione': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'slogan': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'titolo': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'main.homepage': {
            'Meta': {'object_name': 'Homepage'},
            'descrizione': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'occhiello': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'slogan': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['main']
