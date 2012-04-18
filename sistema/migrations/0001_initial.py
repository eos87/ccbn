# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Modulo'
        db.create_table('sistema_modulo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('sistema', ['Modulo'])

        # Adding model 'SubModulo'
        db.create_table('sistema_submodulo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('parent_module', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sistema.Modulo'])),
        ))
        db.send_create_signal('sistema', ['SubModulo'])


    def backwards(self, orm):
        
        # Deleting model 'Modulo'
        db.delete_table('sistema_modulo')

        # Deleting model 'SubModulo'
        db.delete_table('sistema_submodulo')


    models = {
        'sistema.modulo': {
            'Meta': {'object_name': 'Modulo'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'sistema.submodulo': {
            'Meta': {'object_name': 'SubModulo'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'parent_module': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sistema.Modulo']"})
        }
    }

    complete_apps = ['sistema']
