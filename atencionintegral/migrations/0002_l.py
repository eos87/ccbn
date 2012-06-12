# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'EventoColectivo'
        db.create_table('atencionintegral_eventocolectivo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fecha', self.gf('django.db.models.fields.DateTimeField')()),
            ('lugar', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('actividad', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['atencionintegral.ActividadEvento'])),
            ('participantes', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('ninos', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('ninas', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('jovenes_hombres', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('jovenes_mujeres', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('adultos_hombres', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('adultos_mujeres', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('sensibilizacion', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('apropiacion', self.gf('django.db.models.fields.IntegerField')()),
            ('foto', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('comentarios', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('acuerdos', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
        ))
        db.send_create_signal('atencionintegral', ['EventoColectivo'])

        # Adding model 'ActividadEvento'
        db.create_table('atencionintegral_actividadevento', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('atencionintegral', ['ActividadEvento'])


    def backwards(self, orm):
        # Deleting model 'EventoColectivo'
        db.delete_table('atencionintegral_eventocolectivo')

        # Deleting model 'ActividadEvento'
        db.delete_table('atencionintegral_actividadevento')


    models = {
        'atencionintegral.actividadevento': {
            'Meta': {'object_name': 'ActividadEvento'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'atencionintegral.becaprimaria': {
            'Meta': {'object_name': 'BecaPrimaria'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'atencionintegral.becasecundaria': {
            'Meta': {'object_name': 'BecaSecundaria'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'atencionintegral.becauniversitaria': {
            'Meta': {'object_name': 'BecaUniversitaria'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'atencionintegral.eventocolectivo': {
            'Meta': {'object_name': 'EventoColectivo'},
            'actividad': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['atencionintegral.ActividadEvento']"}),
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
            'sensibilizacion': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['atencionintegral']