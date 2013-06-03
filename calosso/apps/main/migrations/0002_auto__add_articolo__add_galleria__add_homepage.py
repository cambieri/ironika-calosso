# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Articolo'
        db.create_table(u'main_articolo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('galleria', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Galleria'])),
            ('miniatura', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('immagine', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('titolo', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('descrizione', self.gf('django.db.models.fields.TextField')(max_length=400, blank=True)),
            ('posizione', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
        ))
        db.send_create_signal(u'main', ['Articolo'])

        # Adding model 'Galleria'
        db.create_table(u'main_galleria', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slogan', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('titolo', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('articolo_principale', self.gf('django.db.models.fields.related.OneToOneField')(blank=True, related_name='+', unique=True, null=True, to=orm['main.Articolo'])),
        ))
        db.send_create_signal(u'main', ['Galleria'])

        # Adding model 'Homepage'
        db.create_table(u'main_homepage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slogan', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('descrizione', self.gf('django.db.models.fields.CharField')(max_length=300, blank=True)),
            ('occhiello', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('galleria_principale', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['main.Galleria'], unique=True)),
        ))
        db.send_create_signal(u'main', ['Homepage'])


    def backwards(self, orm):
        
        # Deleting model 'Articolo'
        db.delete_table(u'main_articolo')

        # Deleting model 'Galleria'
        db.delete_table(u'main_galleria')

        # Deleting model 'Homepage'
        db.delete_table(u'main_homepage')


    models = {
        u'main.articolo': {
            'Meta': {'ordering': "['titolo']", 'object_name': 'Articolo'},
            'descrizione': ('django.db.models.fields.TextField', [], {'max_length': '400', 'blank': 'True'}),
            'galleria': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.Galleria']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'immagine': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'miniatura': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'posizione': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'titolo': ('django.db.models.fields.CharField', [], {'max_length': '80'})
        },
        u'main.galleria': {
            'Meta': {'ordering': "['titolo']", 'object_name': 'Galleria'},
            'articolo_principale': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "'+'", 'unique': 'True', 'null': 'True', 'to': u"orm['main.Articolo']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slogan': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'titolo': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'main.homepage': {
            'Meta': {'object_name': 'Homepage'},
            'descrizione': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'galleria_principale': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['main.Galleria']", 'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'occhiello': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'slogan': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['main']
