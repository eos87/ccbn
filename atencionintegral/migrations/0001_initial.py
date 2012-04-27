# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'BecaPrimaria'
        db.create_table('atencionintegral_becaprimaria', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('atencionintegral', ['BecaPrimaria'])

        # Adding model 'BecaSecundaria'
        db.create_table('atencionintegral_becasecundaria', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('atencionintegral', ['BecaSecundaria'])

        # Adding model 'BecaUniversitaria'
        db.create_table('atencionintegral_becauniversitaria', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('atencionintegral', ['BecaUniversitaria'])

    def backwards(self, orm):
        # Deleting model 'BecaPrimaria'
        db.delete_table('atencionintegral_becaprimaria')

        # Deleting model 'BecaSecundaria'
        db.delete_table('atencionintegral_becasecundaria')

        # Deleting model 'BecaUniversitaria'
        db.delete_table('atencionintegral_becauniversitaria')

    models = {
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
        }
    }

    complete_apps = ['atencionintegral']