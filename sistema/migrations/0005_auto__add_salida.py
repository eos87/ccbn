# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Salida'
        db.create_table('sistema_salida', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('meta', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('titulo', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('tipo_meta', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('model', self.gf('django.db.models.fields.CharField')(default='', max_length=50, blank=True)),
        ))
        db.send_create_signal('sistema', ['Salida'])

    def backwards(self, orm):
        # Deleting model 'Salida'
        db.delete_table('sistema_salida')

    models = {
        'sistema.modulo': {
            'Meta': {'object_name': 'Modulo'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'sistema.salida': {
            'Meta': {'object_name': 'Salida'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meta': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'blank': 'True'}),
            'tipo_meta': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'titulo': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'sistema.submodulo': {
            'Meta': {'object_name': 'SubModulo'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inline': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'parent_module': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sistema.Modulo']"})
        }
    }

    complete_apps = ['sistema']