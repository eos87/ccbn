# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding M2M table for field personas on 'EventoExterno'
        db.create_table('prevencion_eventoexterno_personas', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('eventoexterno', models.ForeignKey(orm['prevencion.eventoexterno'], null=False)),
            ('persona', models.ForeignKey(orm['registro.persona'], null=False))
        ))
        db.create_unique('prevencion_eventoexterno_personas', ['eventoexterno_id', 'persona_id'])

    def backwards(self, orm):
        # Removing M2M table for field personas on 'EventoExterno'
        db.delete_table('prevencion_eventoexterno_personas')

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
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'unique': 'True', 'null': 'True'})
        },
        'lugar.municipio': {
            'Meta': {'ordering': "['departamento__nombre']", 'object_name': 'Municipio'},
            'departamento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Departamento']"}),
            'extension': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'latitud': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'longitud': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'unique': 'True', 'null': 'True'})
        },
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
            'personas': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['registro.Persona']", 'symmetrical': 'False'}),
            'tematica': ('django.db.models.fields.IntegerField', [], {})
        },
        'prevencion.eventointerno': {
            'Meta': {'object_name': 'EventoInterno'},
            'actividad': ('django.db.models.fields.IntegerField', [], {}),
            'acuerdos': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'aprendizaje': ('django.db.models.fields.IntegerField', [], {}),
            'apropiacion': ('django.db.models.fields.IntegerField', [], {}),
            'comentarios': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'fecha': ('django.db.models.fields.DateTimeField', [], {}),
            'foto': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lugar': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'metodologia': ('django.db.models.fields.IntegerField', [], {}),
            'participacion': ('django.db.models.fields.IntegerField', [], {}),
            'participantes': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'tematica': ('django.db.models.fields.IntegerField', [], {})
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
            'barrio': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': "orm['lugar.Barrio']"}),
            'cedula': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '20', 'blank': 'True'}),
            'celular': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '12', 'blank': 'True'}),
            'centro_actual': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['registro.Colegio']", 'null': 'True', 'blank': 'True'}),
            'ciudad': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': "orm['lugar.Ciudad']"}),
            'codigo': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'con_quien_vive': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['registro.Pariente']", 'symmetrical': 'False'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'distrito': ('django.db.models.fields.IntegerField', [], {}),
            'docente_ccbn': ('django.db.models.fields.IntegerField', [], {}),
            'fecha_nacimiento': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'j_oficio': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'oficio_jefe'", 'null': 'True', 'to': "orm['registro.Oficio']"}),
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

    complete_apps = ['prevencion']