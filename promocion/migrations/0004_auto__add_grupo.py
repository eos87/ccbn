# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Grupo'
        db.create_table('promocion_grupo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('semestre', self.gf('django.db.models.fields.IntegerField')()),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('submodulo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sistema.SubModulo'])),
        ))
        db.send_create_signal('promocion', ['Grupo'])


    def backwards(self, orm):
        # Deleting model 'Grupo'
        db.delete_table('promocion_grupo')


    models = {
        'promocion.coro': {
            'Meta': {'object_name': 'Coro'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'semestre': ('django.db.models.fields.IntegerField', [], {}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'promocion.danza': {
            'Meta': {'object_name': 'Danza'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'semestre': ('django.db.models.fields.IntegerField', [], {}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'promocion.eventocolectivo': {
            'Meta': {'object_name': 'EventoColectivo'},
            'actividad': ('django.db.models.fields.IntegerField', [], {}),
            'acuerdos': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'adultos_hombres': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'adultos_mujeres': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'apropiacion': ('django.db.models.fields.IntegerField', [], {}),
            'comentarios': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'fecha': ('django.db.models.fields.DateTimeField', [], {}),
            'foto': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jovenes_hombres': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'jovenes_mujeres': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'lugar': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'ninas': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'ninos': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'participantes': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sensibilizacion': ('django.db.models.fields.IntegerField', [], {}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'promocion.grupo': {
            'Meta': {'object_name': 'Grupo'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'semestre': ('django.db.models.fields.IntegerField', [], {}),
            'submodulo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sistema.SubModulo']"}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'promocion.musica': {
            'Meta': {'object_name': 'Musica'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'semestre': ('django.db.models.fields.IntegerField', [], {}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'promocion.pintura': {
            'Meta': {'object_name': 'Pintura'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'semestre': ('django.db.models.fields.IntegerField', [], {}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'promocion.teatro': {
            'Meta': {'object_name': 'Teatro'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'semestre': ('django.db.models.fields.IntegerField', [], {}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'sistema.modulo': {
            'Meta': {'object_name': 'Modulo'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
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

    complete_apps = ['promocion']