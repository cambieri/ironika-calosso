# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Varie'
        db.create_table(u'main_varie', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('immagine_chi_siamo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('testo_chi_siamo', self.gf('django.db.models.fields.TextField')()),
            ('testo_contatti', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'main', ['Varie'])


    def backwards(self, orm):
        
        # Deleting model 'Varie'
        db.delete_table(u'main_varie')


    models = {
        u'main.articolo': {
            'Meta': {'ordering': "['posizione', 'pk']", 'object_name': 'Articolo'},
            'descrizione': ('django.db.models.fields.TextField', [], {'max_length': '400', 'blank': 'True'}),
            'galleria': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.Galleria']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'immagine': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'miniatura': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'posizione': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'titolo': ('django.db.models.fields.CharField', [], {'max_length': '80'})
        },
        u'main.galleria': {
            'Meta': {'ordering': "['posizione', 'pk']", 'object_name': 'Galleria'},
            'articolo_principale': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "'+'", 'unique': 'True', 'null': 'True', 'to': u"orm['main.Articolo']"}),
            'homepage': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['main.Homepage']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'menu': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'posizione': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'slogan': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'titolo': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'main.homepage': {
            'Meta': {'object_name': 'Homepage'},
            'descrizione': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'immagine': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'occhiello': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'slogan': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'main.varie': {
            'Meta': {'object_name': 'Varie'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'immagine_chi_siamo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'testo_chi_siamo': ('django.db.models.fields.TextField', [], {}),
            'testo_contatti': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['main']
