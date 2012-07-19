# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'InscripcionCurso.aporte_sociedad'
        db.add_column('registro_inscripcioncurso', 'aporte_sociedad',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

    def backwards(self, orm):
        # Deleting field 'InscripcionCurso.aporte_sociedad'
        db.delete_column('registro_inscripcioncurso', 'aporte_sociedad')

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
        },
        'formacion.curso': {
            'Meta': {'object_name': 'Curso'},
            'fecha_fin': ('django.db.models.fields.DateField', [], {}),
            'fecha_inicio': ('django.db.models.fields.DateField', [], {}),
            'frecuencia': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['formacion.Frecuencia']"}),
            'horario': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'submodulo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sistema.SubModulo']"})
        },
        'formacion.frecuencia': {
            'Meta': {'object_name': 'Frecuencia'},
            'cantidad': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        },
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
        },
        'registro.colegio': {
            'Meta': {'object_name': 'Colegio'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'registro.inscripcioncurso': {
            'Meta': {'object_name': 'InscripcionCurso'},
            'aporte_sociedad': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'becado': ('django.db.models.fields.IntegerField', [], {}),
            'calidad_contenido': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'calificacion': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'curso': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['formacion.Curso']"}),
            'date_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'estado': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'fecha': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2012, 7, 19, 0, 0)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mejora_autoestima': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'mejora_vida': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'metodologia': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'persona': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['registro.Persona']"}),
            'xq_no_termino': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'registro.modulopersona': {
            'Meta': {'object_name': 'ModuloPersona'},
            'atencion_integral': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'atencion_integral'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['sistema.SubModulo']"}),
            'biblioteca': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'biblioteca'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['sistema.SubModulo']"}),
            'formacion': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'formacion'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['sistema.SubModulo']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'persona': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['registro.Persona']", 'unique': 'True'}),
            'promocion_artistica': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'promocion_artistica'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['sistema.SubModulo']"}),
            'pv_externa': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'pv_externa'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['sistema.SubModulo']"}),
            'pv_interna': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'pv_interna'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['sistema.SubModulo']"})
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
        },
        'registro.registrobecaprimaria': {
            'Meta': {'object_name': 'RegistroBecaPrimaria'},
            'beca': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['atencionintegral.BecaPrimaria']"}),
            'fecha': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2012, 7, 19, 0, 0)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mejoro_habilidades': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'perc_derecho': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'persona': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['registro.Persona']"}),
            'recibio_atencion_psicologica': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'recibio_suplemento': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'reconoce_capacidad': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rendimiento_academico': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tutoria': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'registro.registrobecasecundaria': {
            'Meta': {'object_name': 'RegistroBecaSecundaria'},
            'beca': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['atencionintegral.BecaSecundaria']"}),
            'bibliotecario': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'esp_propos': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'fecha': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2012, 7, 19, 0, 0)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'persona': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['registro.Persona']"}),
            'promotor': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'servicio_social': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'solidario_centro': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'solidario_comunidad': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'solidario_famila': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'solidario_sociedad': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'registro.registrobecauniversitaria': {
            'Meta': {'object_name': 'RegistroBecaUniversitaria'},
            'beca': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['atencionintegral.BecaUniversitaria']"}),
            'bibliotecario': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'esp_propos': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'fecha': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2012, 7, 19, 0, 0)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'persona': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['registro.Persona']"}),
            'promotor': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'servicio_social': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'solidario_centro': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'solidario_comunidad': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'solidario_famila': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'solidario_sociedad': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'registro.registrobiblioteca': {
            'Meta': {'object_name': 'RegistroBiblioteca'},
            'fecha': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2012, 7, 19, 0, 0)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'persona': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['registro.Persona']", 'unique': 'True'})
        },
        'registro.registrocoro': {
            'Meta': {'object_name': 'RegistroCoro'},
            'asistencia': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'calidad_creativa': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'calificacion': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'fecha': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2012, 7, 19, 0, 0)'}),
            'genero': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'grupo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['promocion.Coro']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mejora_capacidad': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'metodologia': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'persona': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['registro.Persona']"}),
            'perspectiva': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'razon_no_continuar': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'utilidad_para_vida': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'valores_ccbn': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'registro.registrodanza': {
            'Meta': {'object_name': 'RegistroDanza'},
            'asistencia': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'calidad_creativa': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'calificacion': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'fecha': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2012, 7, 19, 0, 0)'}),
            'genero': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'grupo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['promocion.Danza']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mejora_capacidad': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'metodologia': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'persona': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['registro.Persona']"}),
            'perspectiva': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'razon_no_continuar': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'utilidad_para_vida': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'valores_ccbn': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'registro.registromusica': {
            'Meta': {'object_name': 'RegistroMusica'},
            'asistencia': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'calidad_creativa': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'calificacion': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'fecha': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2012, 7, 19, 0, 0)'}),
            'genero': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'grupo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['promocion.Musica']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mejora_capacidad': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'metodologia': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'persona': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['registro.Persona']"}),
            'perspectiva': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'razon_no_continuar': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'utilidad_para_vida': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'valores_ccbn': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'registro.registropintura': {
            'Meta': {'object_name': 'RegistroPintura'},
            'asistencia': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'calidad_creativa': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'calificacion': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'fecha': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2012, 7, 19, 0, 0)'}),
            'genero': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'grupo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['promocion.Pintura']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mejora_capacidad': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'metodologia': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'persona': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['registro.Persona']"}),
            'perspectiva': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'razon_no_continuar': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'utilidad_para_vida': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'valores_ccbn': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'registro.registroteatro': {
            'Meta': {'object_name': 'RegistroTeatro'},
            'asistencia': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'calidad_creativa': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'calificacion': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'fecha': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2012, 7, 19, 0, 0)'}),
            'genero': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'grupo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['promocion.Teatro']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mejora_capacidad': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'metodologia': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'persona': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['registro.Persona']"}),
            'perspectiva': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'razon_no_continuar': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'utilidad_para_vida': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'valores_ccbn': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'registro.relacion': {
            'Meta': {'object_name': 'Relacion'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'owner'", 'to': "orm['registro.Persona']"}),
            'parentesco': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'persona': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'persona'", 'to': "orm['registro.Persona']"})
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

    complete_apps = ['registro']