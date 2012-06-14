# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'EventoInterno.ninos'
        db.add_column('prevencion_eventointerno', 'ninos',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'EventoInterno.ninas'
        db.add_column('prevencion_eventointerno', 'ninas',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'EventoInterno.jovenes_hombres'
        db.add_column('prevencion_eventointerno', 'jovenes_hombres',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'EventoInterno.jovenes_mujeres'
        db.add_column('prevencion_eventointerno', 'jovenes_mujeres',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'EventoInterno.adultos_hombres'
        db.add_column('prevencion_eventointerno', 'adultos_hombres',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'EventoInterno.adultos_mujeres'
        db.add_column('prevencion_eventointerno', 'adultos_mujeres',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'EventoInterno.ninos'
        db.delete_column('prevencion_eventointerno', 'ninos')

        # Deleting field 'EventoInterno.ninas'
        db.delete_column('prevencion_eventointerno', 'ninas')

        # Deleting field 'EventoInterno.jovenes_hombres'
        db.delete_column('prevencion_eventointerno', 'jovenes_hombres')

        # Deleting field 'EventoInterno.jovenes_mujeres'
        db.delete_column('prevencion_eventointerno', 'jovenes_mujeres')

        # Deleting field 'EventoInterno.adultos_hombres'
        db.delete_column('prevencion_eventointerno', 'adultos_hombres')

        # Deleting field 'EventoInterno.adultos_mujeres'
        db.delete_column('prevencion_eventointerno', 'adultos_mujeres')


    models = {
        'prevencion.eventoexterno': {
            'Meta': {'object_name': 'EventoExterno'},
            'actividad': ('django.db.models.fields.IntegerField', [], {}),
            'acuerdos': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'adultos_hombres': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'adultos_mujeres': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'comentarios': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'facilitadores': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'fecha': ('django.db.models.fields.DateTimeField', [], {}),
            'foto': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jovenes_hombres': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'jovenes_mujeres': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'lugar': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'ninas': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'ninos': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'tematica': ('django.db.models.fields.IntegerField', [], {}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'prevencion.eventointerno': {
            'Meta': {'object_name': 'EventoInterno'},
            'actividad': ('django.db.models.fields.IntegerField', [], {}),
            'acuerdos': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'adultos_hombres': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'adultos_mujeres': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'aprendizaje': ('django.db.models.fields.IntegerField', [], {}),
            'apropiacion': ('django.db.models.fields.IntegerField', [], {}),
            'comentarios': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'fecha': ('django.db.models.fields.DateTimeField', [], {}),
            'foto': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jovenes_hombres': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'jovenes_mujeres': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'lugar': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'metodologia': ('django.db.models.fields.IntegerField', [], {}),
            'ninas': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'ninos': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'participacion': ('django.db.models.fields.IntegerField', [], {}),
            'participantes': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'tematica': ('django.db.models.fields.IntegerField', [], {}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['prevencion']