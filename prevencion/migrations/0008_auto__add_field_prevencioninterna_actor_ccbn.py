# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'PrevencionInterna.actor_ccbn'
        db.add_column('prevencion_prevencioninterna', 'actor_ccbn',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'PrevencionInterna.actor_ccbn'
        db.delete_column('prevencion_prevencioninterna', 'actor_ccbn')


    models = {
        'lugar.barrio': {
            'Meta': {'object_name': 'Barrio'},
            'ciudad': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Ciudad']"}),
            'distrito': ('django.db.models.fields.IntegerField', [], {}),
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
            'facilitadores': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'fecha': ('django.db.models.fields.DateTimeField', [], {}),
            'foto': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jovenes_hombres': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'jovenes_mujeres': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'lugar': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'ninas': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'ninos': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'personas': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['registro.Persona']", 'symmetrical': 'False', 'blank': 'True'}),
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
        },
        'prevencion.inscripcionprevencioninterna': {
            'Meta': {'object_name': 'InscripcionPrevencionInterna'},
            'asistencia': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'calidad_contenido': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'calificacion': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'empoderamiento': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'fecha': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2012, 8, 6, 0, 0)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mejora_autoestima': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'metodologia': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'nivel_conocimiento': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'persona': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['registro.Persona']"}),
            'pvbg_interna': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['prevencion.PrevencionInterna']"}),
            'razon_no_asistir': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'prevencion.prevencioninterna': {
            'Meta': {'object_name': 'PrevencionInterna'},
            'actor_ccbn': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'semestre': ('django.db.models.fields.IntegerField', [], {}),
            'year': ('django.db.models.fields.IntegerField', [], {})
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
            'alumno': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'barrio': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': "orm['lugar.Barrio']"}),
            'becado': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'beneficiario': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'cedula': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '20', 'blank': 'True'}),
            'celular': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '12', 'blank': 'True'}),
            'centro_actual': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['registro.Colegio']", 'null': 'True', 'blank': 'True'}),
            'ciudad': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': "orm['lugar.Ciudad']"}),
            'codigo': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'con_quien_vive': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['registro.Pariente']", 'null': 'True', 'blank': 'True'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'docente': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'fecha_nacimiento': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'integrante': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
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
            'personal': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'primer_apellido': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'primer_nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'promotor': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'segundo_apellido': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'blank': 'True'}),
            'segundo_nombre': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'blank': 'True'}),
            'sexo': ('django.db.models.fields.IntegerField', [], {}),
            'telefono': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '12', 'blank': 'True'}),
            'tipo_familia': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'visitante': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['prevencion']