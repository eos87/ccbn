# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'RegistroBecaPrimaria.tutoria'
        db.add_column('registro_registrobecaprimaria', 'tutoria',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'RegistroBecaPrimaria.rendimiento_academico'
        db.add_column('registro_registrobecaprimaria', 'rendimiento_academico',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'RegistroBecaPrimaria.recibio_suplemento'
        db.add_column('registro_registrobecaprimaria', 'recibio_suplemento',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'RegistroBecaPrimaria.recibio_atencion_psicologica'
        db.add_column('registro_registrobecaprimaria', 'recibio_atencion_psicologica',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'RegistroBecaPrimaria.mejoro_habilidades'
        db.add_column('registro_registrobecaprimaria', 'mejoro_habilidades',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'RegistroBecaPrimaria.reconoce_capacidad'
        db.add_column('registro_registrobecaprimaria', 'reconoce_capacidad',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'RegistroBecaPrimaria.perc_derecho'
        db.add_column('registro_registrobecaprimaria', 'perc_derecho',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

    def backwards(self, orm):
        # Deleting field 'RegistroBecaPrimaria.tutoria'
        db.delete_column('registro_registrobecaprimaria', 'tutoria')

        # Deleting field 'RegistroBecaPrimaria.rendimiento_academico'
        db.delete_column('registro_registrobecaprimaria', 'rendimiento_academico')

        # Deleting field 'RegistroBecaPrimaria.recibio_suplemento'
        db.delete_column('registro_registrobecaprimaria', 'recibio_suplemento')

        # Deleting field 'RegistroBecaPrimaria.recibio_atencion_psicologica'
        db.delete_column('registro_registrobecaprimaria', 'recibio_atencion_psicologica')

        # Deleting field 'RegistroBecaPrimaria.mejoro_habilidades'
        db.delete_column('registro_registrobecaprimaria', 'mejoro_habilidades')

        # Deleting field 'RegistroBecaPrimaria.reconoce_capacidad'
        db.delete_column('registro_registrobecaprimaria', 'reconoce_capacidad')

        # Deleting field 'RegistroBecaPrimaria.perc_derecho'
        db.delete_column('registro_registrobecaprimaria', 'perc_derecho')

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
        'registro.colegio': {
            'Meta': {'object_name': 'Colegio'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'registro.inscripcioncurso': {
            'Meta': {'object_name': 'InscripcionCurso'},
            'becado': ('django.db.models.fields.IntegerField', [], {}),
            'calidad_contenido': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'calificacion': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'curso': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['formacion.Curso']"}),
            'date_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'estado': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'fecha': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2012, 4, 26, 0, 0)'}),
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
            'fecha': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2012, 4, 26, 0, 0)'}),
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
            'fecha': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2012, 4, 26, 0, 0)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'persona': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['registro.Persona']"})
        },
        'registro.registrobecauniversitaria': {
            'Meta': {'object_name': 'RegistroBecaUniversitaria'},
            'beca': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['atencionintegral.BecaUniversitaria']"}),
            'fecha': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2012, 4, 26, 0, 0)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'persona': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['registro.Persona']"})
        },
        'registro.registrobiblioteca': {
            'Meta': {'object_name': 'RegistroBiblioteca'},
            'fecha': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2012, 4, 26, 0, 0)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'persona': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['registro.Persona']", 'unique': 'True'})
        },
        'registro.registrocoro': {
            'Meta': {'object_name': 'RegistroCoro'},
            'fecha': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2012, 4, 26, 0, 0)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'persona': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['registro.Persona']"})
        },
        'registro.registrodanza': {
            'Meta': {'object_name': 'RegistroDanza'},
            'fecha': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2012, 4, 26, 0, 0)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'persona': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['registro.Persona']"})
        },
        'registro.registromusica': {
            'Meta': {'object_name': 'RegistroMusica'},
            'fecha': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2012, 4, 26, 0, 0)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'persona': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['registro.Persona']"})
        },
        'registro.registropintura': {
            'Meta': {'object_name': 'RegistroPintura'},
            'fecha': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2012, 4, 26, 0, 0)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'persona': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['registro.Persona']"})
        },
        'registro.registroteatro': {
            'Meta': {'object_name': 'RegistroTeatro'},
            'fecha': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2012, 4, 26, 0, 0)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'persona': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['registro.Persona']"})
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