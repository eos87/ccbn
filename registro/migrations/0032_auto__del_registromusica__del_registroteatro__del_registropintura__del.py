# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'RegistroMusica'
        db.delete_table('registro_registromusica')

        # Deleting model 'RegistroTeatro'
        db.delete_table('registro_registroteatro')

        # Deleting model 'RegistroPintura'
        db.delete_table('registro_registropintura')

        # Deleting model 'RegistroCoro'
        db.delete_table('registro_registrocoro')

        # Deleting model 'RegistroDanza'
        db.delete_table('registro_registrodanza')


    def backwards(self, orm):
        # Adding model 'RegistroMusica'
        db.create_table('registro_registromusica', (
            ('razon_no_continuar', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('persona', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['registro.Persona'])),
            ('genero', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('calificacion', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('calidad_creativa', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('perspectiva', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('valores_ccbn', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('asistencia', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('mejora_capacidad', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('grupo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['promocion.Musica'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fecha', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2012, 8, 21, 0, 0))),
            ('utilidad_para_vida', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('metodologia', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('registro', ['RegistroMusica'])

        # Adding model 'RegistroTeatro'
        db.create_table('registro_registroteatro', (
            ('razon_no_continuar', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('persona', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['registro.Persona'])),
            ('genero', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('calificacion', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('calidad_creativa', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('perspectiva', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('valores_ccbn', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('asistencia', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('mejora_capacidad', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('grupo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['promocion.Teatro'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fecha', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2012, 8, 21, 0, 0))),
            ('utilidad_para_vida', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('metodologia', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('registro', ['RegistroTeatro'])

        # Adding model 'RegistroPintura'
        db.create_table('registro_registropintura', (
            ('razon_no_continuar', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('persona', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['registro.Persona'])),
            ('genero', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('calificacion', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('calidad_creativa', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('perspectiva', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('valores_ccbn', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('asistencia', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('mejora_capacidad', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('grupo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['promocion.Pintura'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fecha', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2012, 8, 21, 0, 0))),
            ('utilidad_para_vida', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('metodologia', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('registro', ['RegistroPintura'])

        # Adding model 'RegistroCoro'
        db.create_table('registro_registrocoro', (
            ('razon_no_continuar', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('persona', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['registro.Persona'])),
            ('genero', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('calificacion', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('calidad_creativa', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('perspectiva', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('valores_ccbn', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('asistencia', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('mejora_capacidad', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('grupo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['promocion.Coro'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fecha', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2012, 8, 21, 0, 0))),
            ('utilidad_para_vida', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('metodologia', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('registro', ['RegistroCoro'])

        # Adding model 'RegistroDanza'
        db.create_table('registro_registrodanza', (
            ('razon_no_continuar', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('persona', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['registro.Persona'])),
            ('genero', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('calificacion', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('calidad_creativa', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('perspectiva', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('valores_ccbn', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('asistencia', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('mejora_capacidad', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('grupo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['promocion.Danza'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fecha', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2012, 8, 21, 0, 0))),
            ('utilidad_para_vida', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('metodologia', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('registro', ['RegistroDanza'])


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
        'atencionintegral.familiabecado': {
            'Meta': {'object_name': 'FamiliaBecado'},
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
            'primaria_year': ('django.db.models.fields.IntegerField', [], {'default': '4'}),
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
        'promocion.grupo': {
            'Meta': {'object_name': 'Grupo'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'semestre': ('django.db.models.fields.IntegerField', [], {}),
            'submodulo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sistema.SubModulo']"}),
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
            'continua_estudiando': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'curso': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['formacion.Curso']"}),
            'date_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'estado': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'fecha': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2012, 8, 22, 0, 0)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mejora_autoestima': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'mejora_vida': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'metodologia': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'persona': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['registro.Persona']"}),
            'xq_no_termino': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'registro.inscripciongrupo': {
            'Meta': {'object_name': 'InscripcionGrupo'},
            'asistencia': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'calidad_creativa': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'calificacion': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'date_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'fecha': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2012, 8, 22, 0, 0)'}),
            'genero': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'grupo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['promocion.Grupo']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mejora_capacidad': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'metodologia': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'persona': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['registro.Persona']"}),
            'perspectiva': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'razon_no_continuar': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'utilidad_para_vida': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'valores_ccbn': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
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
            'acompanante': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
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
            'j_primer_apellido': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'blank': 'True'}),
            'j_primer_nombre': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'blank': 'True'}),
            'j_segundo_apellido': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'blank': 'True'}),
            'j_segundo_nombre': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'blank': 'True'}),
            'jefe_familia': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
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
        },
        'registro.registrobecaprimaria': {
            'Meta': {'object_name': 'RegistroBecaPrimaria'},
            'beca': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['atencionintegral.BecaPrimaria']"}),
            'fecha': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2012, 8, 22, 0, 0)'}),
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
            'fecha': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2012, 8, 22, 0, 0)'}),
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
            'fecha': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2012, 8, 22, 0, 0)'}),
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
            'fecha': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2012, 8, 22, 0, 0)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'persona': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['registro.Persona']", 'unique': 'True'})
        },
        'registro.registrofamiliabecado': {
            'Meta': {'object_name': 'RegistroFamiliaBecado'},
            'beca': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['atencionintegral.FamiliaBecado']"}),
            'fecha': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2012, 8, 22, 0, 0)'}),
            'formacion_acompa': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'hermano_en_curso': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'madre_en_curso': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'mejora_relacion': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'padre_en_curso': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'part_soya': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'persona': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['registro.Persona']"}),
            'sens_derecho_edu': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
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