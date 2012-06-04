# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Musica'
        db.create_table('promocion_musica', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('semestre', self.gf('django.db.models.fields.IntegerField')()),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('promocion', ['Musica'])

        # Adding model 'Teatro'
        db.create_table('promocion_teatro', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('semestre', self.gf('django.db.models.fields.IntegerField')()),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('promocion', ['Teatro'])

        # Adding model 'Danza'
        db.create_table('promocion_danza', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('semestre', self.gf('django.db.models.fields.IntegerField')()),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('promocion', ['Danza'])

        # Adding model 'Coro'
        db.create_table('promocion_coro', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('semestre', self.gf('django.db.models.fields.IntegerField')()),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('promocion', ['Coro'])

        # Adding model 'Pintura'
        db.create_table('promocion_pintura', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('semestre', self.gf('django.db.models.fields.IntegerField')()),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('promocion', ['Pintura'])

    def backwards(self, orm):
        # Deleting model 'Musica'
        db.delete_table('promocion_musica')

        # Deleting model 'Teatro'
        db.delete_table('promocion_teatro')

        # Deleting model 'Danza'
        db.delete_table('promocion_danza')

        # Deleting model 'Coro'
        db.delete_table('promocion_coro')

        # Deleting model 'Pintura'
        db.delete_table('promocion_pintura')

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
        }
    }

    complete_apps = ['promocion']