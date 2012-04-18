# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Colegio'
        db.create_table('registro_colegio', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('registro', ['Colegio'])

        # Adding model 'Oficio'
        db.create_table('registro_oficio', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(unique=True, max_length=200)),
        ))
        db.send_create_signal('registro', ['Oficio'])

        # Adding model 'Pariente'
        db.create_table('registro_pariente', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
        ))
        db.send_create_signal('registro', ['Pariente'])

        # Adding model 'Persona'
        db.create_table('registro_persona', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('primer_nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('segundo_nombre', self.gf('django.db.models.fields.CharField')(default='', max_length=50, blank=True)),
            ('primer_apellido', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('segundo_apellido', self.gf('django.db.models.fields.CharField')(default='', max_length=50, blank=True)),
            ('codigo', self.gf('django.db.models.fields.IntegerField')()),
            ('sexo', self.gf('django.db.models.fields.IntegerField')()),
            ('fecha_nacimiento', self.gf('django.db.models.fields.DateField')()),
            ('cedula', self.gf('django.db.models.fields.CharField')(default='', max_length=20, blank=True)),
            ('personal_ccbn', self.gf('django.db.models.fields.IntegerField')()),
            ('docente_ccbn', self.gf('django.db.models.fields.IntegerField')()),
            ('municipio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lugar.Municipio'])),
            ('ciudad', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lugar.Ciudad'])),
            ('barrio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lugar.Barrio'])),
            ('distrito', self.gf('django.db.models.fields.IntegerField')()),
            ('direccion', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('telefono', self.gf('django.db.models.fields.CharField')(default='', max_length=12, blank=True)),
            ('celular', self.gf('django.db.models.fields.CharField')(default='', max_length=12, blank=True)),
            ('nivel_academico', self.gf('django.db.models.fields.IntegerField')()),
            ('nivel_estudio', self.gf('django.db.models.fields.IntegerField')()),
            ('centro_actual', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['registro.Colegio'], null=True, blank=True)),
            ('oficio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['registro.Oficio'], null=True, blank=True)),
            ('tipo_familia', self.gf('django.db.models.fields.IntegerField')()),
            ('jefe_familia', self.gf('django.db.models.fields.IntegerField')()),
            ('j_primer_nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('j_segundo_nombre', self.gf('django.db.models.fields.CharField')(default='', max_length=50, blank=True)),
            ('j_primer_apellido', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('j_segundo_apellido', self.gf('django.db.models.fields.CharField')(default='', max_length=50, blank=True)),
            ('j_oficio', self.gf('django.db.models.fields.related.ForeignKey')(related_name='oficio_jefe', blank=True, to=orm['registro.Oficio'])),
        ))
        db.send_create_signal('registro', ['Persona'])

        # Adding M2M table for field con_quien_vive on 'Persona'
        db.create_table('registro_persona_con_quien_vive', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('persona', models.ForeignKey(orm['registro.persona'], null=False)),
            ('pariente', models.ForeignKey(orm['registro.pariente'], null=False))
        ))
        db.create_unique('registro_persona_con_quien_vive', ['persona_id', 'pariente_id'])


    def backwards(self, orm):
        
        # Deleting model 'Colegio'
        db.delete_table('registro_colegio')

        # Deleting model 'Oficio'
        db.delete_table('registro_oficio')

        # Deleting model 'Pariente'
        db.delete_table('registro_pariente')

        # Deleting model 'Persona'
        db.delete_table('registro_persona')

        # Removing M2M table for field con_quien_vive on 'Persona'
        db.delete_table('registro_persona_con_quien_vive')


    models = {
        'lugar.barrio': {
            'Meta': {'object_name': 'Barrio'},
            'ciudad': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Ciudad']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'tipo': ('django.db.models.fields.IntegerField', [], {})
        },
        'lugar.ciudad': {
            'Meta': {'object_name': 'Ciudad'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'municipio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Municipio']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'tipo': ('django.db.models.fields.IntegerField', [], {})
        },
        'lugar.departamento': {
            'Meta': {'object_name': 'Departamento'},
            'extension': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'unique': 'True', 'null': 'True', 'db_index': 'True'})
        },
        'lugar.municipio': {
            'Meta': {'ordering': "['departamento__nombre']", 'object_name': 'Municipio'},
            'departamento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Departamento']"}),
            'extension': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'latitud': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'longitud': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'unique': 'True', 'null': 'True', 'db_index': 'True'})
        },
        'registro.colegio': {
            'Meta': {'object_name': 'Colegio'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'registro.oficio': {
            'Meta': {'object_name': 'Oficio'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'})
        },
        'registro.pariente': {
            'Meta': {'object_name': 'Pariente'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        'registro.persona': {
            'Meta': {'object_name': 'Persona'},
            'barrio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Barrio']"}),
            'cedula': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '20', 'blank': 'True'}),
            'celular': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '12', 'blank': 'True'}),
            'centro_actual': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['registro.Colegio']", 'null': 'True', 'blank': 'True'}),
            'ciudad': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Ciudad']"}),
            'codigo': ('django.db.models.fields.IntegerField', [], {}),
            'con_quien_vive': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['registro.Pariente']", 'symmetrical': 'False'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'distrito': ('django.db.models.fields.IntegerField', [], {}),
            'docente_ccbn': ('django.db.models.fields.IntegerField', [], {}),
            'fecha_nacimiento': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'j_oficio': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'oficio_jefe'", 'blank': 'True', 'to': "orm['registro.Oficio']"}),
            'j_primer_apellido': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'j_primer_nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'j_segundo_apellido': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'blank': 'True'}),
            'j_segundo_nombre': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'blank': 'True'}),
            'jefe_familia': ('django.db.models.fields.IntegerField', [], {}),
            'municipio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Municipio']"}),
            'nivel_academico': ('django.db.models.fields.IntegerField', [], {}),
            'nivel_estudio': ('django.db.models.fields.IntegerField', [], {}),
            'oficio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['registro.Oficio']", 'null': 'True', 'blank': 'True'}),
            'personal_ccbn': ('django.db.models.fields.IntegerField', [], {}),
            'primer_apellido': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'primer_nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'segundo_apellido': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'blank': 'True'}),
            'segundo_nombre': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'blank': 'True'}),
            'sexo': ('django.db.models.fields.IntegerField', [], {}),
            'telefono': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '12', 'blank': 'True'}),
            'tipo_familia': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['registro']
